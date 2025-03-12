#!/usr/bin/bash

. install/setup.bash
export ROS_DOMAIN_ID=69

# Set logs directory at the root of where the script is executed
LOG_DIR="$(pwd)/logs"
mkdir -p "$LOG_DIR"  # Ensure the logs directory exists

# Create a timestamped log file
LOG_FILE="$LOG_DIR/ros_log_$(date +'%Y-%m-%d_%H-%M-%S').txt"

# Create a symlink to the latest log BEFORE starting ROS 2
ln -sf "$LOG_FILE" "$LOG_DIR/latest.log"

# Ensure immediate output by using stdbuf, redirect both stdout and stderr to tee
stdbuf -oL ros2 launch frontend surface_launch.py 2>&1 | (trap '' SIGINT; tee "$LOG_FILE")

# Keep only the 10 most recent log files
ls -t "$LOG_DIR"/ros_log_*.txt | tail -n +11 | xargs rm -f
