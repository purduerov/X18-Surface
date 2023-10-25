#! /usr/bin/python3

import rclpy
import rclpy.node as Node
import json
import sys
#ROS
from shared_msgs.msg import ImuMsg
from std_msgs.msg import String
import numpy as np

imu = [0, 0, 0]

def _imu(comm):
    global imu
    imu[0] = comm.gyro[0]
    imu[1] = (abs(comm.gyro[1]) - 180) / 180
    imu[2] = comm.gyro[2]
    for i in range(len(imu)):
        imu[i] = imu[i].item()
    print(json.dumps(imu))

if __name__ == '__main__':
    rclpy.init()
    node = rclpy.create_node('surface_imu')
    stat = node.create_subscription(ImuMsg,'/rov/imu', _imu,10)

    rclpy.spin(node)