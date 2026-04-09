#!/usr/bin/env python3

import pygame
import sys
import time
import signal
import numpy as np

from pygame import event  # Add signal module import

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
        self.pub_tools = self.create_publisher(ToolsCommandMsg, "tools_motor", 10) # enable tools publisher

        # Add a flag to track shutdown state
        self.shutting_down = False

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
        self.joystick_1_axis_state = joystick_axis_state.copy()
        self.joystick_2_axis_state = joystick_axis_state.copy()
        self.joystick_1_button_state = joystick_button_state.copy()
        self.joystick_2_button_state = joystick_button_state.copy()
        self.joystick_1_hat = (0, 0)
        self.joystick_2_hat = (0, 0)

        self.get_logger().info("ROV Controller Node Initialized")

        # Pilot variables
        self.reverse = 1
        self.lockout = True
        self.is_fine = 0
        self.is_pool_centric = False
        self.depth_lock = False
        self.pitch_lock = False
        self.tools = np.asarray([127, 127, 127, 127, 127, 127], dtype=np.uint8)

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
        #self.controller_thread = self.create_timer(0.001, self.update)
        self.controller_thread = self.create_timer(0.02, self.update)  # 50 Hz
        self.get_logger().info("Controllers initialized")

    def init_pygame(self):
        """Initializes pygame and the joystick"""
        pygame.init()
        pygame.joystick.init()

        # Make sure we have joysticks connected
        if pygame.joystick.get_count() < 1:
            self.get_logger().error("No joystick devices found!")
            raise Exception("No joystick devices found!")

        # Print information about all connected joysticks
        for i in range(pygame.joystick.get_count()):
            joy = pygame.joystick.Joystick(i)
            joy.init()
            self.get_logger().info(f"Found joystick {i}: {joy.get_name()}")
            self.get_logger().info(f"  - Number of axes: {joy.get_numaxes()}")
            self.get_logger().info(f"  - Number of buttons: {joy.get_numbuttons()}")

        # Initialize the joysticks and identify them by name
        if pygame.joystick.get_count() >= 2:
            joy1 = pygame.joystick.Joystick(0)
            joy2 = pygame.joystick.Joystick(1)
            joy1.init()
            joy2.init()

            # Identify which joystick is which based on name
            if JOYSTICK_NAME in joy1.get_name():
                self.joystick_1 = joy1
                self.joystick_2 = joy2
                self.get_logger().info(
                    f"Joystick 1 is {joy1.get_name()}, Joystick 2 is {joy2.get_name()}"
                )
            elif JOYSTICK_NAME in joy2.get_name():
                self.joystick_1 = joy2
                self.joystick_2 = joy1
                self.get_logger().info(
                    f"Joystick 1 is {joy2.get_name()}, Joystick 2 is {joy1.get_name()}"
                )
            else:
                # If neither matches the expected name, use default order
                self.joystick_1 = joy1
                self.joystick_2 = joy2
                self.get_logger().warn(
                    f"Could not identify joysticks by name. Using default order."
                )
        else:
            # If only one joystick, use it as joystick_1
            self.joystick_1 = pygame.joystick.Joystick(0)
            self.joystick_1.init()
            self.joystick_2 = None
            self.get_logger().warn("Only one joystick detected!")

    def update_mapping(self, msg):
        """Updates the controller mapping"""
        self.config = self.config_reader.load_config(msg.data)
        self.config_name = msg.data

    # Modify the update method to check for shutdown state
    def update(self):
        """Updates the controller state"""
        if self.shutting_down:
            return

        pygame.event.pump() 
        print("UPDATE RUNNING")

        if self.joystick_1:
            self.joystick_1_hat = self.joystick_1.get_hat(0)
            #self.get_logger().info(f"[HAT1] {self.joystick_1_hat}")

        if self.joystick_2:
            self.joystick_2_hat = self.joystick_2.get_hat(0)
            #self.get_logger().info(f"[HAT2] {self.joystick_2_hat}")

        # DEBUG: poll axes directly
        # if self.joystick_1:
        #     for i in range(self.joystick_1.get_numaxes()):
        #         val = self.joystick_1.get_axis(i)
        #         if abs(val) > 0.1:
        #             print(f"[POLL] Joy1 Axis {i} = {val:.3f}")

        # if self.joystick_2:
        #     for i in range(self.joystick_2.get_numaxes()):
        #         val = self.joystick_2.get_axis(i)
        #         if abs(val) > 0.1:
        #             print(f"[POLL] Joy2 Axis {i} = {val:.3f}")

        # Get all the events from pygame and process them
        for event in pygame.event.get():
            self.process_event(event)

    def correct_raw(self, raw):
        """Corrects the raw value from the controller to be in the range [-1.0, 1.0]"""
        raw = float(raw)
        if abs(raw) >= STICK_DEAD_ZONE:
            return max(-1, min(1, raw))
        return 0

    def handle_button_event(self, event):
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 3:
                self.is_fine += 1
                if self.is_fine > 3:
                    self.is_fine = 0
            elif event.button == 2:
                self.is_fine -= 1
                if self.is_fine < 0:
                    self.is_fine = 3

    def process_event(self, event):
        """Processes a pygame event"""
        # Check if the event is a joyaxismotion event
        if event.type == pygame.JOYAXISMOTION:
            # Get the joystick instance that generated this event
            joy_instance = pygame.joystick.Joystick(event.joy)

            # DEBUGGING - print for tools
            print(f"[AXIS] Joystick {event.joy} | Axis {event.axis} = {event.value:.3f}")

            # Determine if this is joystick_1 or joystick_2
            if self.joystick_1 and joy_instance.get_id() == self.joystick_1.get_id():
                self.joystick_1_axis_state[event.axis] = self.correct_raw(event.value)
                self.get_logger().debug(
                    f"Joystick 1 axis {event.axis} = {self.joystick_1_axis_state[event.axis]}"
                )
            elif self.joystick_2 and joy_instance.get_id() == self.joystick_2.get_id():
                self.joystick_2_axis_state[event.axis] = self.correct_raw(event.value)
                self.get_logger().debug(
                    f"Joystick 2 axis {event.axis} = {self.joystick_2_axis_state[event.axis]}"
                )
            else:
                self.get_logger().warn(f"Event from unknown joystick {event.joy}")

        # Check if the event is a joybuttondown event
        # elif event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP:
        #     self.handle_button_event(event)

        # DEBUGGING - print button events for tools
        elif event.type == pygame.JOYBUTTONDOWN:
            print(f"[BUTTON DOWN] Joystick {event.joy} | Button {event.button}")

            if self.joystick_1 and event.joy == self.joystick_1.get_id():
                self.joystick_1_button_state[event.button] = 1
            elif self.joystick_2 and event.joy == self.joystick_2.get_id():
                self.joystick_2_button_state[event.button] = 1

        elif event.type == pygame.JOYBUTTONUP:
            print(f"[BUTTON UP] Joystick {event.joy} | Button {event.button}")

            if self.joystick_1 and event.joy == self.joystick_1.get_id():
                self.joystick_1_button_state[event.button] = 0
            elif self.joystick_2 and event.joy == self.joystick_2.get_id():
                self.joystick_2_button_state[event.button] = 0

    # Modify the pub_data method to check for shutdown state
    def pub_data(self):
        """Publishes the data to the rov_velocity topic and the tools topic"""
        if self.shutting_down:
            return

        tm = self.getTools()
        self.pub_tools.publish(tm)
        self.get_logger().info(f"Published tools: {tm.tools}")

        # Get a message to publish for the rov_velocity topic
        self.pub.publish(self.getMessage())
        # Get a message to publish for the tools topic
        self.pub_tools.publish(self.getTools())

    def getMessage(self):
        """Returns a RovVelocityCommand message based on the current controller state"""
        t = Twist()

        # Set default values for the twist message
        t.linear.x = t.linear.y = t.linear.z = 0.0
        t.angular.x = t.angular.y = t.angular.z = 0.0

        # Use configuration if available
        if True:
            # Get scale factors and trims from the configuration
            trims = self.config_reader.get_trims()

            # Process linear axes with their own local variables
            for axis_name in ["x", "y", "z"]:
                mapping = self.config_reader.get_axis_mapping("linear", axis_name)
                if mapping:
                    device = mapping["device"]
                    axis_idx = mapping["axis"]
                    scale = mapping["scale"]
                    invert = mapping["invert"]

                    # Get the value from the appropriate device
                    linear_value = 0.0
                    if device == "joystick_left" and self.joystick_1:
                        linear_value = float(self.joystick_1_axis_state[axis_idx])
                    elif device == "joystick_right" and self.joystick_2:
                        linear_value = float(self.joystick_2_axis_state[axis_idx])
                    else:
                        self.get_logger().warn(
                            f"Unknown device in configuration for linear.{axis_name}: {device}"
                        )

                    # Apply scale and inversion
                    linear_value = linear_value * scale * (-1 if invert else 1)

                    # Apply trim
                    linear_value += trims[axis_name]

                    # Apply reverse setting
                    linear_value *= self.reverse

                    # Set the value in the twist message
                    if axis_name == "x":
                        t.linear.x = linear_value
                    elif axis_name == "y":
                        t.linear.y = linear_value
                    elif axis_name == "z":
                        t.linear.z = linear_value

            # Process angular axes with their own local variables
            for axis_name in ["x", "y", "z"]:
                mapping = self.config_reader.get_axis_mapping("angular", axis_name)
                if mapping:
                    device = mapping["device"]
                    axis_idx = mapping["axis"]
                    scale = mapping["scale"]
                    invert = mapping["invert"]

                    # Get the value from the appropriate device
                    angular_value = 0.0
                    if device == "joystick_left" and self.joystick_1:
                        angular_value = float(self.joystick_1_axis_state[axis_idx])
                    elif device == "joystick_right" and self.joystick_2:
                        angular_value = float(self.joystick_2_axis_state[axis_idx])
                    else:
                        self.get_logger().warn(
                            f"Unknown device in configuration for angular.{axis_name}: {device}"
                        )

                    # Apply scale and inversion
                    angular_value = angular_value * scale * (-1 if invert else 1)

                    # Apply reverse setting
                    angular_value *= self.reverse

                    # Set the value in the twist message
                    if axis_name == "x":
                        t.angular.x = angular_value
                    elif axis_name == "y":
                        t.angular.y = angular_value
                    elif axis_name == "z":
                        t.angular.z = angular_value

        new_msg = RovVelocityCommand()
        new_msg.twist = t
        new_msg.is_fine = self.is_fine
        new_msg.is_pool_centric = self.is_pool_centric
        new_msg.depth_lock = self.depth_lock
        new_msg.pitch_lock = self.pitch_lock
        new_msg.current_config = self.config_name

        return new_msg

    #@staticmethod
    def hat_to_pwm(self, hat_val):
        # hat_val is -1, 0, or 1
        temp = self.tools
        self.tools = max(0, min(255, self.tools_last + hat_val))
        self.tools_last = temp
        return self.tools

    def getTools(self):
        """Returns a ToolsCommandMsg message based on the current hat/button state"""
        tm = ToolsCommandMsg()

        # Wrist (hat up/down)
        w1 = self.joystick_1_hat[1]
        w2 = self.joystick_2_hat[1]
        wrist = w2 if w2 != 0 else w1  # use joystick 2 if active, else joystick 1

        # Pitch (hat left/right)
        p1 = self.joystick_1_hat[0]
        p2 = self.joystick_2_hat[0]
        pitch = w2 if w2 != 0 else w1  # same logic

        # Claw (button 0)
        c1 = 1 if self.joystick_1_button_state.get(0, 0) else 0
        c2 = 1 if self.joystick_2_button_state.get(0, 0) else 0
        claw = max(c1, c2)  # either joystick pressed

        # --- Differential wrist mapping ---
        # Convert inputs to servo positions
        servo1 = wrist + pitch
        servo2 = wrist - pitch
        # Clamp PWM 0-255
        change = np.asarray([servo1, servo2, claw, 127, 127, 127], dtype=np.uint8)

     
        self.tools = np.clip(self.tools + change, 0, 255)

        # Compose tools array
        tm.tools = self.tools  # padding to match 6 element msg
        #tm.motor_tools = 0  # or whatever your motor_tools field is for

        self.get_logger().info(f"[TOOLS] servo1={servo1} servo2={servo2} claw={claw}")
        return tm

        #tm.tools = [vertical, horizontal, claw, 127, 127, 127]

        #self.get_logger().info(f"[TOOLS] vertical={vertical} horizontal={horizontal} claw={claw}")
        #return tm
    
    def _get_axis_value(self, mapping):
        device = mapping["device"]
        axis = mapping["axis"]

        if device == "joystick_left" and self.joystick_1:
            return self.joystick_1_axis_state[axis]

        elif device == "joystick_right" and self.joystick_2:
            return self.joystick_2_axis_state[axis]

        elif device == "both":
            val1 = self.joystick_1_axis_state[axis] if self.joystick_1 else 0.0
            val2 = self.joystick_2_axis_state[axis] if self.joystick_2 else 0.0

            # Return whichever has stronger input (avoids conflict)
            return val1 if abs(val1) > abs(val2) else val2

        return 0.0


    def _get_button_value(self, mapping):
        device = mapping["device"]
        button = mapping["button"]

        if device == "joystick_left" and self.joystick_1:
            return self.joystick_1_button_state[button]

        elif device == "joystick_right" and self.joystick_2:
            return self.joystick_2_button_state[button]

        elif device == "both":
            val1 = self.joystick_1_button_state[button] if self.joystick_1 else 0
            val2 = self.joystick_2_button_state[button] if self.joystick_2 else 0
            return val1 or val2  # pressed if either is pressed

        return 0
    
    def _get_hat_value(self, mapping):
        device = mapping["device"]

        hat = (0, 0)
        if device == "joystick_left" and self.joystick_1:
            hat = self.joystick_1_hat
        elif device == "joystick_right" and self.joystick_2:
            hat = self.joystick_2_hat

        return hat

    def normalize_controller_val(self, val, max_val=255.0):
        val = float(val)
        val /= float(max_val)
        return val

    # Add a cleanup method for graceful shutdown
    def cleanup(self):
        """Clean shutdown logic"""
        if self.shutting_down:
            return

        self.shutting_down = True

        # Clean up pygame resources
        if pygame.get_init():
            pygame.joystick.quit()
            pygame.quit()

        # Stop all timers
        if hasattr(self, "data_thread"):
            self.data_thread.cancel()
        if hasattr(self, "controller_thread"):
            self.controller_thread.cancel()


def main():
    rclpy.init(args=None)
    controller = Controller()

    # Set up signal handler for graceful shutdown
    def signal_handler(sig, frame):
        controller.get_logger().info(f"Received signal {sig}, shutting down...")
        controller.cleanup()
        # Exit the program
        sys.exit(0)

    # Register signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        #rclpy.spin(controller)
        while rclpy.ok():
            tm = controller.getTools()
            controller.pub_tools.publish(tm)
            rclpy.spin_once(controller, timeout_sec=0.01)
            controller.update()
    except KeyboardInterrupt:
        # This should be caught by the signal handler, but just in case
        pass
    finally:
        # Clean up resources
        controller.cleanup()
        controller.destroy_node()
        rclpy.shutdown()
        sys.exit(0)


if __name__ == "__main__":
    main()
