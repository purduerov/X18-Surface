#!/bin/bash

# Check if mediamtx executable exists in /ros/mediamtx
if [ ! -f ./ros/mediamtx_node/src/mediamtx ]; then
    echo "mediamtx executable not found in ./ros/mediamtx_node/src"
    echo "Please run scripts/install_mediamtx.sh first"
    exit 1
fi

# Build the ROS 2 workspace
source /opt/ros/humble/setup.bash
colcon build
. install/setup.bash
export ROS_DOMAIN_ID=69