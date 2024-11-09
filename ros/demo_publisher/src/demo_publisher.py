#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Create a publisher node that will publish a message counting up and down from 100 repeatedly
class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(String, 'count', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 100

    def timer_callback(self):
        msg = String()
        msg.data = str(self.count)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.count = self.count - 1 if self.count > 0 else 100


def main():
    rclpy.init()
    publisher_node = PublisherNode()
    rclpy.spin(publisher_node)
    publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
