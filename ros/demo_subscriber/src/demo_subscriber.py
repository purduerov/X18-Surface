#!/usr/bin/env python3

# Import necessary libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import socketio

sio = socketio.Client()

# Create a subscriber node that will listen to messages published on the 'count' topic
class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node') # Initialize the node with a name
        self.subscription = self.create_subscription(String, 'count', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')
        # Emit the received message to the frontend using SocketIO
        sio.emit('count', msg.data)

def main():
    rclpy.init()
    subscriber_node = SubscriberNode()
    # Connect to the SocketIO server
    sio.connect('http://127.0.0.1:5000')  # Adjust the URL if necessary

    # Check if the connection was successful
    if sio.connected:
        subscriber_node.get_logger().info("Connected to SocketIO server")
    else:
        subscriber_node.get_logger().error("Failed to connect to SocketIO server")

    rclpy.spin(subscriber_node)
    subscriber_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
