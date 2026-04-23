#!/usr/bin/env python3

# Import necessary libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool
import socketio
import json

sio = socketio.Client()


class LeakSubscriberNode(Node):
    def __init__(self):
        super().__init__("leak_subscriber_node")
        self.topics = {"leak": self.rov_leak_callback}
        self.create_subscription(Bool, "leak_sensor", self.rov_leak_callback, 10)

    def rov_leak_callback(self, msg):
        msg_json = rosmsg_to_dict(msg)
        sio.emit("leak_sensor", msg_json)
        self.get_logger().info(f"Received leak sensor data: {msg.data}, emitted to SocketIO: {msg_json}")


def main():
    rclpy.init()

    sio.connect("http://127.0.0.1:5013")

    leak_subscriber_node = LeakSubscriberNode()
    rclpy.spin(leak_subscriber_node)

    # Clean up after spinning finishes
    leak_subscriber_node.destroy_node()
    rclpy.shutdown()

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


if __name__ == "__main__":
    main()
