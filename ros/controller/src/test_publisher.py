#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

def main():
    rclpy.init()
    node = Node("test_pub")
    pub = node.create_publisher(String, "hello_topic", 10)
    try:
        while rclpy.ok():
            msg = String()
            msg.data = "test"
            pub.publish(msg)
            rclpy.spin_once(node, timeout_sec=0.1)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()