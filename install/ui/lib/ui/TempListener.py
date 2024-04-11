#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class TempListenerNode(Node):
    def __init__(self, window):
        super().__init__("temp_listener")
        self.subscription = self.create_subscription(
            Float32, "water_temp", self.callback, 10
        )
        
        self.window = window

    def callback(self, data):
        add = self.window.ui.offsetinput.value()
        sub = self.window.ui.offsetinput_2.value()
        self.window.ui.tempoutput.display(data.data + add - sub)


def main(args=None):
    rclpy.init(args=args)
    node = TempListenerNode()
    rclpy.spin(node)
    rclpy.shutdown()
        

if __name__ == "__main__":
    main()