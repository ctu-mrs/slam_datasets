#!/bin/bash

SCRIPT_PATH="$( cd "$(dirname "$0")" ; pwd -P )"

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

## #{ Argument parsing
FINALS_PATH=$1

if [ "$#" -ne 1 ]; then
    echo "./tarData.sh finals_path"
    exit -1
fi

if [ ! -d "$FINALS_PATH" ]; then
  echo -e "Is not directory: ${RED}${FINALS_PATH}${NC}"
  exit -1
fi
## #}

## #{ Paths to input data
DATASETS=( "uav21_2" "$FINALS_PATH/post_event_testing/day_1/green/7_2021_09_28_12_53_02_metro_flight_15_min/slam_dataset"
           "uav21_3" "$FINALS_PATH/post_event_testing/day_1/green/3_2021_09_28_11_33_50_urban_localization_dataset/slam_dataset"
           "uav21_4" "$FINALS_PATH/post_event_testing/day_1/green/19_2021_09_28_16_10_54_mine_flight_crash_at_the_end/slam_dataset"
           "uav21_5" "$FINALS_PATH/post_event_testing/day_1/green/13_2021_09_28_14_28_35_last_flight_hit_something_lol/slam_dataset"
           "uav21_6" "$FINALS_PATH/post_event_testing/day_2/green/1_2021_09_29_14_06_19_tunnel_to_cave_loop_closure/slam_dataset"
           "uav22_1" "$FINALS_PATH/post_event_testing/day_2/blue/46_2021_09_29_21_12_11_tunnel_crash_do_rohu_chodby/slam_dataset"
           "uav22_2" "$FINALS_PATH/post_event_testing/day_2/blue/44_2021_09_29_20_57_39_tunnel_druhej_crash_do_plachty/slam_dataset"
           "uav22_3" "$FINALS_PATH/post_event_testing/day_1/blue/36_2021_09_28_19_52_26_post_event_metro_flight_blue/slam_dataset"
           "uav24_1" "$FINALS_PATH/post_event_testing/day_2/pink/23_2021_09_29_22_48_13_sklad/slam_dataset" )

MAPS=("subt_finals.pcd" "$FINALS_PATH/systems_final.pcd"
      "subt_finals.asc" "$FINALS_PATH/systems_final.asc" )

## #}

## #{ tar maps

# Tar
MAPS_TAR="${FINALS_PATH}/maps.tar.gz"
if [ ! -f "${MAPS_TAR}" ]; then
  cp -f "${MAPS[1]}" "${FINALS_PATH}/${MAPS[0]}"
  cp -f "${MAPS[3]}" "${FINALS_PATH}/${MAPS[2]}"
  tar -czvf "${MAPS_TAR}" -C "${FINALS_PATH}" "${MAPS[0]}" "${MAPS[2]}"
fi

## #}

## #{ tar datasets
for (( i=0; i<${#DATASETS[@]}; i+=2 ));
do

  NAME="${DATASETS[$i]}"
  DIR_DATASET="${DATASETS[$i+1]}"

  if [ ! -d "${SCRIPT_PATH}/../${NAME}" ]; then
    echo -e "Directory does not exist: ${RED}${SCRIPT_PATH}/../${NAME}${NC}"
    continue
  fi

  if [ ! -d "$DIR_DATASET" ]; then
    echo -e "Directory does not exist: ${RED}${DIR_DATASET}${NC}"
    continue
  fi

  TAR_NAME="${DIR_DATASET}/${NAME}.tar.gz"
  if [ -f "${TAR_NAME}" ]; then
    echo -e "File already exists: ${RED}${TAR_NAME}${NC}"
    continue
  fi

  BAG_NAME="${NAME}.bag"
  if [ -f "${TAR_NAME}" ]; then
    echo -e "File does not exist: ${RED}${DIR_DATASET}/${BAG_NAME}${NC}"
    continue
  fi

  # Tar
  echo -e "Running tar on file: ${GREEN}${DIR_DATASET}/${BAG_NAME}${NC}"
  tar -czvf "${TAR_NAME}" -C "${DIR_DATASET}" "${BAG_NAME}"

done
## #}
