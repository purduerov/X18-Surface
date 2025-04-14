#!/usr/bin/env python3

import pygame
import sys
import time

# ROS
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool, Empty
from shared_msgs.msg import RovVelocityCommand, ToolsCommandMsg
from geometry_msgs.msg import Twist

from config import *
from config_manager import ConfigManager
from utils.heartbeat_helper import HeartbeatHelper

class Controller(Node):
    def __init__(self):
        super().__init__("controller")
        # Setup heartbeat
        self.heartbeat_helper = HeartbeatHelper(self)

        # Pygame variables
        self.joystick_1 = None
        self.joystick_2 = None

        # Get and set the current configuration
        self.config_reader = ConfigManager(self.get_logger())
        self.config = self.config_reader.load_config("default")
        self.config_name = "default"

        # Joystick and throttle states
        self.joystick_1_axis_state = joystick_axis_state
        self.joystick_2_axis_state = joystick_axis_state
        self.joystick_1_button_state = joystick_button_state
        self.joystick_2_button_state = joystick_button_state

        # Pilot variables
        self.reverse = 1
        self.lockout = True
        self.is_fine = 0
        self.is_pool_centric = False
        self.depth_lock = False
        self.pitch_lock = False
        self.tools = [0, 0, 0, 0, 0]
        
        try:
            self.init_pygame()
        except:
            self.get_logger().error("Could not initialize pygame. Exiting...")

        # Create the publishers
        self.pub = self.create_publisher(RovVelocityCommand, "rov_velocity", 10)
        # self.pub_tools = self.create_publisher(ToolsCommandMsg, "tools", 10)

        # Create subscriber
        self.create_subscription(String, "controller_mapping", self.update_mapping, 10)

        # Create the timers
        self.data_thread = self.create_timer(0.1, self.pub_data)
        self.gamepad_thread = self.create_timer(0.001, self.update)
        self.get_logger().info("Controllers initialized")


    def init_pygame(self):
        """Initializes pygame and the joystick"""
        pygame.init()
        pygame.joystick.init()
        # assert pygame.joystick.get_count() == 2, "There should be two identical joystick devices"
        self.joystick_1 = pygame.joystick.Joystick(0)
        self.joystick_2 = pygame.joystick.Joystick(1)


    def update_mapping(self, msg):
        """Updates the controller mapping"""
        self.config = self.config_reader.load_config(msg.data)
        self.config_name = msg.data


    def update(self):
        """Updates the gamepad state"""
        # Get all the events from pygame and process them
        for event in pygame.event.get():
            self.process_event(event)


    def correct_raw(self, raw):
        """Corrects the raw value from the gamepad to be in the range [-1.0, 1.0]"""
        raw = float(raw)
        if abs(raw) >= STICK_DEAD_ZONE:
            return max(-1, min(1, raw))
        return 0
    

    def handle_button_event(self, event):
        self.get_logger().info(f"Button {event.button} {'pressed' if event.type == pygame.JOYBUTTONDOWN else 'released'}")
        pass


    def process_event(self, event):
        """Processes a pygame event"""
        # Check if the event is a joyaxismotion event
        if event.type == pygame.JOYAXISMOTION:
            # self.get_logger().info(f"New JOYAXISMOTION event: {event}")
            # Check if the event is from the joystick or the throttle
            if event.joy == self.joystick_1.get_id():
                self.joystick_1_axis_state[event.axis] = self.correct_raw(event.value)
            elif event.joy == self.joystick_2.get_id():
                self.joystick_2_axis_state[event.axis] = self.correct_raw(event.value)

        # Check if the event is a joybuttondown event
        elif event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP:
            self.handle_button_event(event)


    def pub_data(self):
        """Publishes the data to the rov_velocity topic and the tools topic"""
        # Get a message to publish for the rov_velocity topic
        self.pub.publish(self.getMessage())
        # Get a message to publish for the tools topic
        # self.pub_tools.publish(self.getTools())

    def getMessage(self):
        """Returns a RovVelocityCommand message based on the current gamepad state"""
        t = Twist()

        # Set default values for the twist message
        t.linear.x = t.linear.y = t.linear.z = 0.0
        t.angular.x = t.angular.y = t.angular.z = 0.0
        
        # Use configuration if available
        if True:
            # Get scale factors and trims from the configuration
            trims = self.config_reader.get_trims()

            # Process linear axes
            for axis_name in ["x", "y", "z"]:
                mapping = self.config_reader.get_axis_mapping("linear", axis_name)
                if mapping:
                    device = mapping["device"]
                    axis_idx = mapping["axis"]
                    scale = mapping["scale"]
                    invert = mapping["invert"]
                    self.get_logger().info(f"Linear axis {axis_name} mapped to {device} on axis: {axis_idx}")
                    
                    # Get the value from the appropriate device
                    if device == "joystick_left":
                        value = float(self.joystick_1_axis_state[axis_idx])
                    elif device == "joystick_right":
                        value = float(self.joystick_2_axis_state[axis_idx])
                    else:
                        self.get_logger().warn(f"Unknown device in configuration: {device}")
                    
                    # Apply scale and inversion
                    value = value * scale * (-1 if invert else 1)
                    
                    # Apply trim
                    value += trims[axis_name]
                    
                    # Apply reverse setting
                    value *= self.reverse
                    
                    # Set the value in the twist message
                    if axis_name == "x":
                        t.linear.x = value
                    elif axis_name == "y":
                        t.linear.y = value
                    elif axis_name == "z":
                        t.linear.z = value
            
            # Process angular axes
            for axis_name in ["x", "y", "z"]:
                mapping = self.config_reader.get_axis_mapping("angular", axis_name)
                if mapping:
                    self.get_logger().info(f"Angular axis {axis_name} mapped to {device} on axis: {axis_idx}")
                    device = mapping["device"]
                    axis_idx = mapping["axis"]
                    scale = mapping["scale"]
                    invert = mapping["invert"]
                    
                    # Get the value from the appropriate device
                    if device == "joystick_left":
                        value = float(self.joystick_1_axis_state[axis_idx])
                    elif device == "joystick_right":
                        value = float(self.joystick_2_axis_state[axis_idx])
                    else:
                        self.get_logger().warn(f"Unknown device in configuration: {device}")
                    
                    # Apply scale and inversion
                    value = value * scale * (-1 if invert else 1)
                    
                    # Apply reverse setting
                    value *= self.reverse
                    
                    # Set the value in the twist message
                    if axis_name == "x":
                        t.angular.x = value
                    elif axis_name == "y":
                        t.angular.y = value
                    elif axis_name == "z":
                        t.angular.z = value

        new_msg = RovVelocityCommand()
        new_msg.twist = t
        new_msg.is_fine = self.is_fine
        new_msg.is_pool_centric = self.is_pool_centric
        new_msg.depth_lock = self.depth_lock
        new_msg.pitch_lock = self.pitch_lock
        new_msg.current_config = self.config_name

        return new_msg

    def getTools(self):
        """Returns a ToolsCommandMsg message based on the current gamepad state"""

        tm = ToolsCommandMsg()
        tm.tools = [i for i in self.tools]

        return tm

    def normalize_controller_val(self, val, max_val=255.0):
        val = float(val)
        val /= float(max_val)
        return val


def main():
    rclpy.init(args=None)
    controller = Controller()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
