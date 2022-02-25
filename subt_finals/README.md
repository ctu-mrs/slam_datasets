# DARPA Subterranean Challenge: Finals

Two datasets (red and green trajectories in the figure below) recorded onboard a UAV [1, 2] flying within the DARPA Subterranean Challenge Finals (primarily in mines).
Mid-range flighs in narrow subterranean environments (mines and caves), one dataset contains loop, average speed ~0.5 m/s.
%% Long flights in narrow subterranean environment, no loops, average speed ~0.5 m/s, dynamic obstacle (a safety operator walking behind the UAV).

![](.fig/subt_finals.png)

The rosbags contain unsynchronized LiDAR points and IMU measurements.
The groundtruth trajectory was estimated ([code](https://github.com/ctu-mrs/mrs_pcl_tools/blob/master/src/executables/EstimateLidarSlamDrift.cpp)) during post-processing: registration of on-board data onto map of the cave using ICP set with high-precision parameters.

## Datasets
| Dataset   | Length (m, s)    | Environment       | Loop   | Dust perception  | Autonomy                               | GoPro                                  |
| --------- | ---------------- | ----------------- | ------ | ---------------- | -------------------------------------- | -------------------------------------- |
| green 2   | 306, 757         | metro             | no     | no               | (link)[https://youtu.be/tkGsCteX3Ns]   | N/A                                    |
| green 3   | 23, 58           | cave              | no     | no               | (link)[https://youtu.be/OOW50sTCzLY]   | N/A                                    |
| green 4   | 196, 432         | mine              | no     | yes              | (link)[https://youtu.be/sCGyxbgCa_E]   | N/A                                    |
| green 5   | 377, 914         | metro             | no     | no               | (link)[https://youtu.be/alTvBpJoxpw]   | N/A                                    |
| green 6   | 164, 432         | mine and cave     | yes    | yes              | (link)[https://youtu.be/WG3CthG6XuU]   | (link)[https://youtu.be/7MFX66mnS50]   |
| blue 1    | 131, 332         | mine              | no     | yes              | (link)[https://youtu.be/u2O5nsBRvBU]   | N/A                                    |
| blue 2    | 347, 347         | mine              | no     | yes              | (link)[https://youtu.be/MNnfMZDNs-w]   | (link)[https://youtu.be/H9P09uPBGps]   |
| blue 3    | 266, 644         | metro             | no     | no               | (link)[https://youtu.be/HepOcH5c1Jg]   | N/A                                    |
| pink 1    | 162, 475         | urban storeroom   | no     | no               | (link)[https://youtu.be/lcehGjB4-HI]   | (link)[https://youtu.be/aFqolM6R-4s]   |

## Sensors
- OS0-128 LiDAR (128 rows, 90 deg vFoV) topics:
  - raw points: `/UAV_NAME/os_cloud_nodelet/points`
    - to filter out the UAV frame, use points with minimal distance of `0.5 m` from the sensor origin
  - imu: `/UAV_NAME/os_cloud_nodelet/imu`

## Frames
- baselink: `UAV_NAME/fcu`
- points: `UAV_NAME/os_lidar`
- imu: `UAV_NAME/os_imu`
```
UAV_NAME/fcu
└───> UAV_NAME/os_sensor
      └───> UAV_NAME/os_lidar
      └───> UAV_NAME/os_imu
```

## Folder structure
```
subt_finals
│   download.sh
│   subt_finals.pcd
│
└───DATASET
│       mission_data.txt
│       trajectory_groundtruth.txt
│       rosbag.bag
│       fcu_in_map.mat
│    
└───...
```
- Script to download large data: `download.sh`
  - ground truth map of the environment: `subt_finals.pcd`
  - datasets: `rosbag.bag`
- Ground truth trajectory: `trajectory_groundtruth.txt`
  - in local origin (use `fcu_in_map.mat` to transform to the map frame): zero-pose initialization
  - format: `timestamp x y z qx qy qz qw`
- General mission information: `mission_data.txt`
- Initial transformation `map->UAV_NAME/fcu`: `fcu_in_map.mat`
  - 4x4 transformation matrix
 
## References
[1] Petracek, P.; Kratky, V.; Petrlik, M.; Baca, T.; Kratochvil, R.; Saska, M. *Large-Scale Exploration of Cave Environments by Unmanned Aerial Vehicles,* IEEE Robotics and Automation Letters 2021, 6, 7596–7603.
[2] V. Kratky, P. Petracek, T. Baca and M. Saska, *An autonomous unmanned aerial vehicle system for fast exploration of large complex indoor environments,* Journal of field robotics, May 2021.
