#!/usr/bin/env python3

import json
import rclpy
from rclpy.node import Node
from shared_msgs.msg import FinalThrustMsg
from std_msgs.msg import Float64
import json


class DepthSurfaceNode(Node):
    def __init__(self, window):
        super().__init__("surface_depth")
        self.subscription = self.create_subscription(
            Float64, "/depth", self.callback, 10
        )

        # Initialize the thrust array
        self.thrust = [0, 0, 0, 0, 0, 0, 0, 0]
        self.window = window
        print("initialized")

    def callback(self, data):
        depth = json.dumps(data.data)
        self.window.ui.depthoutput.display(data.data)

        print(depth, flush=True, end=" ")


def main(args=None):
    rclpy.init(args=args)
    node = ThrustersSurfaceNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
