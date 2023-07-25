#! /usr/bin/python3

import json
#ROS
import rclpy
from shared_msgs.msg import FinalThrustMsg

thrust = [0, 0, 0, 0, 0, 0, 0, 0]

def _thruster(comm):
    global thrust
    thrust[0] = int(comm.thrusters[0])
    thrust[1] = int(comm.thrusters[1])
    thrust[2] = int(comm.thrusters[2])
    thrust[3] = int(comm.thrusters[3])
    thrust[4] = int(comm.thrusters[4])
    thrust[5] = int(comm.thrusters[5])
    thrust[6] = int(comm.thrusters[6])
    thrust[7] = int(comm.thrusters[7])
    print(json.dumps(thrust))

if __name__ == '__main__':
    rclpy.init()
    node = rclpy.create_node('thrusters_surface')
    stat = node.create_subscription(FinalThrustMsg,'/rov/final_thrust', _thruster,10)

    rclpy.spin(node)
