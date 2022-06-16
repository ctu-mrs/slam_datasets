#!/bin/bash

echo "waiting for ROS"
until timeout 6s rosparam get /run_id > /dev/null 2>&1; do
  echo "waiting for /run_id"
  sleep 1;
done

sleep 1;
