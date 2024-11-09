#!/usr/bin/env python3

# Import necessary libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from shared_msgs.msg import RovVelocityCommand
import socketio

sio = socketio.Client()

# Create a subscriber node that will listen to multiple ROS topics
class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')  # Initialize the node with a name
        
        # Dictionary to map topic names to their corresponding callback functions
        self.topics = {
            'count': self.count_callback,
            'rov_velocity': self.rov_velocity_callback
            # Add more topics and their respective callbacks here
        }
        
        # Subscribe to each topic in the topics dictionary
        self.create_subscription(String, 'count', self.count_callback, 10)
        self.create_subscription(RovVelocityCommand, 'rov_velocity', self.rov_velocity_callback, 10)

    def count_callback(self, msg):
        # General callback for all subscribed topics
        self.get_logger().info(f'Received from count topic: "{msg.data}"')
        # Emit the received message to the frontend using SocketIO
        sio.emit('count', msg.data)

    def rov_velocity_callback(self, msg):
        # General callback for all subscribed topics
        self.get_logger().info(f'Received from rov_velocity topic: "{msg.data}"')
        # Emit the received message to the frontend using SocketIO
        sio.emit('rov_velocity', msg.data)

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
