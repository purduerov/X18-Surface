#!/usr/bin/env python3

import json
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class DepthSurfaceNode(Node):
    def __init__(self, window):
        super().__init__("surface_depth")
        self.subscription = self.create_subscription(
            Float64, "/depth", self.callback, 10
        )

        # Initialize the thrust array
        self.window = window
        print("initialized")

    def callback(self, data):
        depth = json.dumps(data.data)
        self.window.ui.depthoutput.display(data.data)

        print(depth, flush=True, end=" ")


def main(args=None):
    rclpy.init(args=args)
    node = DepthSurfaceNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
