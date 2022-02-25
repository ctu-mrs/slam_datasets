#!/bin/bash

if [[ ! $# -gt 0 ]] ; then
  echo "Directory with bags and lidar_in_fcu.mat required."
  exit
fi

SCRIPT_PATH="$( cd "$(dirname "$0")" ; pwd -P )"

DATA_PATH=$1

# Path to ground truth map
if [ $# -eq 2 ]; then
  TF_LIDAR_IN_FCU="$2/lidar_in_fcu.mat"
else
  TF_LIDAR_IN_FCU="$DATA_PATH/lidar_in_fcu.mat"
fi

# uav21_3: green_3

## #{ Parse bag names
bags_str=$( find $DATA_PATH -name "*.bag" )
readarray -t BAGS <<< "$bags_str"
UAV_NAMES=()

for bag in "${BAGS[@]}"
do
  # echo "$bag"
  case "$bag" in 
    *red* | *uav20*)
      UAV_NAMES+=("uav20")
      ;;
    *green* | *uav21*)
      UAV_NAMES+=("uav21")
      ;;
    *blue* | *uav22*)
      UAV_NAMES+=("uav22")
      ;;
    *yellow* | *uav23*)
      UAV_NAMES+=("uav23")
      ;;
    *pink* | *uav24*)
      UAV_NAMES+=("uav24")
      ;;
  esac
done
## #}

# Options
BAGS_LEN=${#BAGS[@]}
for (( i=0; i<${BAGS_LEN}; i++ ));
do

  ROSBAG="${BAGS[$i]}"
  BAG_DIR="$(dirname $ROSBAG)"
  UAV_NAME="${UAV_NAMES[$i]}"

  TRAJ_GT="${BAG_DIR}/trajectory_gt.txt"
  TRAJ_LIDAR_IN_MAP="${BAG_DIR}/traj_lidar_in_map.txt"
  TRAJ_FCU_IN_MAP="traj_fcu_in_map.txt"
  TRAJ_FCU_IN_LOCAL="${BAG_DIR}/traj_fcu_in_local.txt"
  TF_FCU_IN_MAP="${BAG_DIR}/fcu_in_map.mat"

  BAG_FILTERED_WITH_TFS="${BAG_DIR}/data_filtered_with_tfs.bag"
  BAG_FILTERED_WO_TFS="${BAG_DIR}/rosbag.bag"

  if [[ "$ROSBAG" == "$BAG_FILTERED_WO_TFS" || "$ROSBAG" == "$BAG_FILTERED_WITH_TFS" ]]; then
    continue
  fi

  echo "Rosbag $((i+1))/$BAGS_LEN: $ROSBAG"

  # Filter rosbag topics
  if [[ ! -f "$BAG_FILTERED_WO_TFS" && ! -f "$BAG_FILTERED_WITH_TFS" ]]; then
    echo "Filtering rosbag topics"
    rosbag filter "${bag}" "${BAG_FILTERED_WITH_TFS}"\
      "topic == '/tf_static' or\
       topic == '/${UAV_NAME}/basler_left/camera_info' or\
       topic == '/${UAV_NAME}/basler_left/image_raw/compressed' or\
       topic == '/${UAV_NAME}/basler_right/camera_info' or\
       topic == '/${UAV_NAME}/basler_right/image_raw/compressed' or\
       topic == '/${UAV_NAME}/os_cloud_nodelet/points' or\
       topic == '/${UAV_NAME}/os_cloud_nodelet/points_processed'"
  fi

  # Filter rosbag static tfs
  if [ ! -f "$BAG_FILTERED_WO_TFS" ]; then
    echo "Filtering static TFs"
    python $HOME/git/general_tools/bag_tools/bag_filter_static_tfs.py "${BAG_FILTERED_WITH_TFS}" "${BAG_FILTERED_WO_TFS}" --whitelist "fcu,os_sensor,os_imu,os_lidar,basler_left,basler_right,basler_left_optical,basler_right_optical"
    rm "$BAG_FILTERED_WITH_TFS"
  fi

  # Transform trajectory to fcu_in_map
  echo "Transforming trajectory to fcu in map"
  cp "$TRAJ_GT" "$TRAJ_LIDAR_IN_MAP"
  python $HOME/git/general_tools/trajectory_tools/transform_trajectory.py "${TRAJ_LIDAR_IN_MAP}" "${TF_LIDAR_IN_FCU}" --invert-transform --output-file "${TRAJ_FCU_IN_MAP}"
  TRAJ_FCU_IN_MAP="${BAG_DIR}/${TRAJ_FCU_IN_MAP}"

  # Parsing origin
  echo "Parsing origin"
  python parseOrigin.py "${TRAJ_FCU_IN_MAP}" "${TF_FCU_IN_MAP}"

  # Transform trajectory to fcu_in_local
  python $HOME/git/general_tools/trajectory_tools/transform_trajectory.py "${TRAJ_FCU_IN_MAP}" "${TF_FCU_IN_MAP}" --invert-transform --output-file "${TRAJ_FCU_IN_LOCAL}"

  # Copy important files
  STORE_DIR="$BAG_DIR"/slam_dataset
  mkdir -p "$STORE_DIR"
  mv "$TF_FCU_IN_MAP" "${STORE_DIR}/fcu_in_map.mat"
  mv "$TRAJ_FCU_IN_LOCAL" "${STORE_DIR}/trajectory_groundtruth.txt"

  if [ ! -f "${STORE_DIR}/rosbag.bag" ]; then
    mv "$BAG_FILTERED_WO_TFS" "${STORE_DIR}/rosbag.bag"
    ln -s "${STORE_DIR}/rosbag.bag" "$BAG_FILTERED_WO_TFS"
  fi

done


