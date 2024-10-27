#!/usr/bin/env python3

# Import necessary libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import socketio

sio = socketio.Client()

# Create a subscriber node that will listen to multiple ROS topics
class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')  # Initialize the node with a name
        
        # Dictionary to map topic names to their corresponding callback functions
        self.topics = {
            'count': self.count_callback
            # Add more topics and their respective callbacks here
        }
        
        # Subscribe to each topic in the topics dictionary
        for topic_name, callback in self.topics.items():
            self.create_subscription(String, topic_name, callback, 10)

    def count_callback(self, msg):
        # General callback for all subscribed topics
        self.get_logger().info(f'Received from count topic: "{msg.data}"')
        # Emit the received message to the frontend using SocketIO
        sio.emit('count', msg.data)

def main():
    rclpy.init()
    subscriber_node = SubscriberNode()
    
    # Connect to the SocketIO server
    sio.connect('http://127.0.0.1:5000')  # Adjust the URL if necessary

    rclpy.spin(subscriber_node)
    subscriber_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
