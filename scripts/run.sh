#!/usr/bin/bash

. install/setup.bash
export ROS_DOMAIN_ID=69
ros2 launch frontend surface_launch.yaml
