#! /usr/bin/python3

import rclpy
from rclpy.node import Node
from shared_msgs.msg import ToolsCommandMsg

class ReceiveNode(Node):
    def __init__(self):
        super().__init__("Receive")
        self.sub = self.create_subscription(ToolsCommandMsg, '/tools', self.message, 10)
        self.get_logger().info("Initialized")

    def message(self, msg):
        self.get_logger().info(msg.message)

def main(args = None):
    rclpy.init(args = args)

    node = ReceiveNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()