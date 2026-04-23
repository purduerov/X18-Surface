#!/usr/bin/env python3

# Import necessary libraries
import os

import os

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from shared_msgs.msg import TempMsg
import socketio
import json
import os

sio = socketio.Client()


# Create a subscriber node that will listen to multiple ROS topics
class DepthSubscriber(Node):
    def __init__(self):
        super().__init__("depth_subscriber")

        # Dictionary to map topic names to their corresponding callback functions
        self.topics = {
            "depth": self.rov_depth_callback,
        }

        # Subscribe to each topic in the topics dictionary
        self.create_subscription(Float64, "depth", self.rov_depth_callback, 10)

    def rov_depth_callback(self, msg):
        msg_dict = rosmsg_to_dict(msg)
        #self.get_logger().info(f'test')
        msg_json = json.dumps(msg_dict)
        #self.get_logger().info(f'Received from depth topic: "{msg}"')
        if sio.connected:
            sio.emit('depth', msg_json)
            self.get_logger().info(f'Emitted depth data to SocketIO: {msg_json}')
        else:
            self.get_logger().warn("SocketIO not connected, skipping emit")


def rosmsg_to_dict(msg):
    """
    Convert any ROS message to a Python dictionary (recursive for nested messages).
    """
    msg_dict = {}

    if not hasattr(msg, "__slots__"):
        # If the attribute is not a ROS message (i.e., primitive or list), return its value
        return msg

    for field in msg.__slots__:  # Iterate over all fields in the message
        field_value = getattr(msg, field)

        # Remove leading underscore from the field name
        clean_field = field.lstrip("_")

        # If the field is a list of messages, process each item in the list
        if isinstance(field_value, list):
            msg_dict[clean_field] = [rosmsg_to_dict(item) for item in field_value]
        else:
            msg_dict[clean_field] = rosmsg_to_dict(
                field_value
            )  # Recurse for nested messages

    return msg_dict


def main():
    rclpy.init()
    depth_subscriber_node = DepthSubscriber()

    port = str(os.getenv("FLASK_PORT", 5013))

    try:
        sio.connect("http://127.0.0.1:" + port)
        depth_subscriber_node.get_logger().info(f"Connected to SocketIO server at port {port}")
    except Exception as e:
        depth_subscriber_node.get_logger().error(f"Failed to connect to SocketIO server: {e}")

    rclpy.spin(depth_subscriber_node)
    depth_subscriber_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
