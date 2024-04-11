#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool

class LeakListenerNode(Node):
    def __init__(self, window):
        super().__init__("leak_listener")
        self.subscription = self.create_subscription(
            Bool, "leak_sensor", self.callback, 10
        )
        
        self.window = window

    def callback(self, data):
        self.window.ui.leakoutput.display(data.data)



def main(args=None):
    rclpy.init(args=args)
    node = LeakListenerNode()
    rclpy.spin(node)
    rclpy.shutdown()
        

if __name__ == "__main__":
    main()