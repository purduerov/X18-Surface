#!/usr/bin/env python3

import rclpy
from std_msgs.msg import Float32
import json


def callback(data):
    jsonstuff = json.dumps(data.data)
    # jsonstuff = json.dumps(None)
    print(jsonstuff, flush=True, end=" ")


if __name__ == "__main__":
    rclpy.init()
    node = rclpy.create_node("surface_depth")

    sub = node.create_subscription(Float32, "/rov/depth", callback, 10)

    rclpy.spin(node)
