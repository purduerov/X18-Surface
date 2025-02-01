#!/usr/bin/env python3

# Import necessary libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Header
from shared_msgs.msg import RovVelocityCommand
import socketio
import json
import os
from dotenv import load_dotenv
from utils.heartbeat_helper import HeartbeatHelper

sio = socketio.Client()

class UISubscriber(Node):
    def __init__(self):
        super().__init__('ui_subscriber')

        # Setup the heartbeat helper
        self.heartbeat_helper = HeartbeatHelper(self)
        
        # Dictionary of topics to subscribe to and their message types
        self.topics = {
            # Frontend published topics
            'rov_velocity': RovVelocityCommand,
            'heartbeat': Header,
            # Core published topics
        }
        
        # Subscribe to each topic in the topics dictionary
        for topic in self.topics:
            self.get_logger().info(f'Subscribing to {topic} topic with message type {self.topics[topic].__name__}')
            self.create_subscription(self.topics[topic], topic, lambda msg, topic_name=topic: self.msg_callback(msg, topic_name), 10)

    def msg_callback(self, msg, topic_name):
        # Convert the ROS message to JSON
        msg_dict = rosmsg_to_dict(msg)
        msg_json = json.dumps(msg_dict)
        # Log the received message
        self.get_logger().info(f'Received from {topic_name} topic: "{msg}"')
        # Emit the received message to the frontend using SocketIO
        sio.emit(topic_name, msg_json)


def rosmsg_to_dict(msg):
    """
    Convert any ROS message to a Python dictionary (recursive for nested messages).
    """
    msg_dict = {}

    if not hasattr(msg, '__slots__'):
        # If the attribute is not a ROS message (i.e., primitive or list), return its value
        return msg

    for field in msg.__slots__:  # Iterate over all fields in the message
        field_value = getattr(msg, field)

        # Remove leading underscore from the field name
        clean_field = field.lstrip('_')

        # If the field is a list of messages, process each item in the list
        if isinstance(field_value, list):
            msg_dict[clean_field] = [rosmsg_to_dict(item) for item in field_value]
        else:
            msg_dict[clean_field] = rosmsg_to_dict(field_value)  # Recurse for nested messages

    return msg_dict


def main():
    rclpy.init()
    ui_subscriber = UISubscriber()
    
    # Connect to the SocketIO server
    load_dotenv(dotenv_path=f"/workspaces/X17-Surface/.env")
    port = str(os.getenv("FLASK_PORT", 5013))
    sio.connect('http://127.0.0.1:' + port)  # Adjust the URL if necessary

    rclpy.spin(ui_subscriber)
    ui_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
