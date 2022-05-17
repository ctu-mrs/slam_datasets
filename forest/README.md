# Forest dataset

This dataset contains approx 1.25 km-long flight throught a sparse forest.
It was created for develoment and testing of large-scale localization and mapping techniques, that often struggle with other then the small, clean and feature-full laboratory environments.
This dataset containes intermited recording of RTG GPS with Integer FIX solution.

![](.fig/forest_dataset.png)

The rosbags contain unsynchronized LiDAR points, IMU measurements and RGBD data.
Ground thruth is provided via onboard GPS (Pixhaw) and RTK GPS (Emlid Reach) with intermitend INT FIX.

## Sensors

- OS0-128 LiDAR (128 rows, 90 deg vFoV) (top-mounted):
  - lidar packets: `/uav11/os_nodelet/lidar_packets` of type `ouster_ros/PacketMsg`
  - imu: `/uav11/os_nodelet/imu_packets` of type `ouster_ros/PacketMsg`
  - use the [ouster_ros](https://github.com/ctu-mrs/ouster/) to decode the packets into point cloud data
- Realsense d435 (forward-facing):
  - color camera: `/uav11/rgbd/color/image_raw/compressed` of type `sensor_msgs/CompressedImage`
  - depth camera: `/uav11/rgbd/aligned_depth_to_color/image_raw/compressedDepth` of type `sensor_msgs/CompressedImage`
- Garmin Lidar Lite (down-facing):
  - data: `/uav11/mavros/distance_sensor/garmin` of type `sensor_msgs/Range`

## Frames

Sensor frames:
- baselink: `uav11/body`
- points: `uav11/os_sensor/os_lidar`
- imu: `uav11/os_sensor/os_imu`
- rgbd optical: `uav11/rgbd/color_optical`
- rgbd link: `uav11/rgbd/link`
GPS frames:
- RTK frame: `uav11/rtk_origin`
- GPS frame: `uav11/gps_origin`

```
uav11/common_origin
├───> uav11/rtk_origin
│     └───> uav11/rtk_body
└───> uav11/gps_origin
      └───> uav11/gps_body

uav11/body
├───> uav11/os_sensor
│     ├───> uav11/os_lidar
│     └───> uav11/os_imu
├───> uav11/rgbd/color_optical
├───> uav11/rgbd/link
└───> uav11/garmin
```

## Multimedia

### Photo of the UAV

![](.fig/uav11_1.jpg)

### Hand-held video of the flight


