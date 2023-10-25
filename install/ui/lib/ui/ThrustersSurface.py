#!/usr/bin/env python3

import json
import rclpy
from rclpy.node import Node
from shared_msgs.msg import FinalThrustMsg

class ThrustersSurfaceNode(Node):

    def __init__(self, window):
        super().__init__('thrusters_surface')
        self.subscription = self.create_subscription(
            FinalThrustMsg, '/final_thrust', self.thrust_callback, 10)

        # Initialize the thrust array
        self.thrust = [0, 0, 0, 0, 0, 0, 0, 0]
        self.window = window
        print("initialized")

    def thrust_callback(self, comm):
        self.window.readout_widget.thruster1.setValue(int(comm.thrusters[0]))
        self.window.readout_widget.thruster2.setValue(int(comm.thrusters[1]))
        self.window.readout_widget.thruster3.setValue(int(comm.thrusters[2]))
        self.window.readout_widget.thruster4.setValue(int(comm.thrusters[3]))
        self.window.readout_widget.thruster5.setValue(int(comm.thrusters[4]))
        self.window.readout_widget.thruster6.setValue(int(comm.thrusters[5]))
        self.window.readout_widget.thruster7.setValue(int(comm.thrusters[6]))
        self.window.readout_widget.thruster8.setValue(int(comm.thrusters[7]))
        self.thrust[0] = int(comm.thrusters[0])
        self.thrust[1] = int(comm.thrusters[1])
        self.thrust[2] = int(comm.thrusters[2])
        self.thrust[3] = int(comm.thrusters[3])
        self.thrust[4] = int(comm.thrusters[4])
        self.thrust[5] = int(comm.thrusters[5])
        self.thrust[6] = int(comm.thrusters[6])
        self.thrust[7] = int(comm.thrusters[7])

        # Print the thrust array as JSON
        self.get_logger().info(json.dumps(self.thrust))
        print("running")

def main(args=None):
    rclpy.init(args=args)
    node = ThrustersSurfaceNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()