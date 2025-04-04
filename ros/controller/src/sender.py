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


class Controller(Node):
    def __init__(self):
        super().__init__("gp_pub")
        # Pygame variables
        self.joystick_1 = None
        self.joystick_2 = None

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

        # Mapping variables (TO CHANGE MAPPING: GO TO getMessage() AND MAKE YOUR CHANGES THERE)
        self.mapping = 1  # 0, 1, 2, 3

        try:
            self.init_pygame()
        except:
            self.get_logger().info(
                "Controllers not found. Please make sure both joysticks are connected"
            )

        # Create the publishers
        self.pub = self.create_publisher(RovVelocityCommand, "rov_velocity", 10)
        # self.pub_tools = self.create_publisher(ToolsCommandMsg, "tools", 10)

        # Create the timers
        self.data_thread = self.create_timer(0.1, self.pub_data)
        self.gamepad_thread = self.create_timer(0.001, self.update)
        self.get_logger().info("Controllers initialized")

    def init_pygame(self):
        """Initializes pygame and the joystick"""
        pygame.init()
        # There should be two identical joystick devices
        pygame.joystick.init()
        assert pygame.joystick.get_count() == 2, "There should be two identical joystick devices"
        self.joystick_1 = pygame.joystick.Joystick(0)
        self.joystick_2 = pygame.joystick.Joystick(1)

        
        # # Determine left from right joystick
        # if (pygame.joystick.Joystick(0).get_button(10) == 1 and
        #     pygame.joystick.Joystick(0).get_button(11) == 1):
        #     self.left_joystick = pygame.joystick.Joystick(0)
        #     self.right_joystick = pygame.joystick.Joystick(1)
        # elif (pygame.joystick.Joystick(1).get_button(10) == 1 and
        #         pygame.joystick.Joystick(1).get_button(11) == 1):
        #     self.left_joystick = pygame.joystick.Joystick(1)
        #     self.right_joystick = pygame.joystick.Joystick(0)
        # else:
        #     self.get_logger().error("Could not determine left and right joysticks."
        #     " Please check the controller configuration.")
        #     # Exit the program
        #     pygame.quit()
        #     sys.exit(0)


    def reconnect(self):
        """Tries to reconnect the gamepad"""
        reconnected = False
        i = GAMEPAD_TIMEOUT
        while i >= 0 and not reconnected:
            self.get_logger().info(
                "Gamepad disconnected, reconnect within {:2} seconds".format(i)
            )
            try:
                self.init_pygame()
                reconnected = True
            except:
                pygame.time.wait(1000)  # Wait 1 second
                i -= 1

        if reconnected:
            self.get_logger().info("Controllers reconnected")

        return reconnected

    def update(self):
        """Updates the gamepad state"""
        # Get all the events from pygame and process them
        for event in pygame.event.get():
            self.process_event(event)

    def correct_raw(self, raw):
        """Corrects the raw value from the gamepad to be in the range [-1.0, 1.0]"""
        if raw > 0:
            if raw >= STICK_DEAD_ZONE:
                return raw
            elif raw > 1:
                return 1
            else:
                return 0

        if raw < 0:
            if raw <= -STICK_DEAD_ZONE:
                return raw
            elif raw < -1:
                return -1
            else:
                return 0

    def process_event(self, event):
        """Processes a pygame event"""
        # Check if the event is a joyaxismotion event
        if event.type == pygame.JOYAXISMOTION:
            self.get_logger().info(f"New JOYAXISMOTION event: {event}")
            # Check if the event is from the joystick or the throttle
            if event.joy == 0:
                self.joystick_1_axis_state[event.axis] = self.correct_raw(event.value)
            elif event.joy == 1:
                self.joystick_2_axis_state[event.axis] = self.correct_raw(event.value)

        # Check if the event is a joybuttondown event
        # elif event.type == pygame.JOYBUTTONDOWN:
        #     # Check if the event is from the joystick or the throttle
        #     if event.joy == self.joystick_id:
        #         self.joystick_button_state[event.button] = 1

        #     elif event.joy == self.throttle_id:
        #         self.throttle_button_state[event.button] = 1

        # Check if the event is a joybuttonup event
        # elif event.type == pygame.JOYBUTTONUP:
        #     # Check if the event is from the joystick or the throttle
        #     if event.joy == self.joystick_id:
        #         self.joystick_button_state[event.button] = 0
        #     elif event.joy == self.throttle_id:
        #         self.throttle_button_state[event.button] = 0

        # self.changed_trigger = False
        # if self.joystick_button_state[0] == 1 and self.changed_trigger == False:
        #     self.tools[0] = not self.tools[0]
        #     self.changed_trigger = True

        # if self.joystick_button_state[0] == 0:
        #     self.changed_trigger = False

        # self.change_buttom = False
        # if self.joystick_button_state[1] == 1 and self.change_buttom == False:
        #     self.tools[2] = not self.tools[2]
        #     self.change_buttom = True

        # if self.joystick_button_state[1] == 0:
        #     self.change_buttom = False

    def pub_data(self):
        """Publishes the data to the rov_velocity topic and the tools topic"""
        # Get a message to publish for the rov_velocity topic
        self.pub.publish(self.getMessage())
        # Get a message to publish for the tools topic
        # self.pub_tools.publish(self.getTools())

    def getMessage(self):
        """Returns a RovVelocityCommand message based on the current gamepad state"""

        t = Twist()

        if self.mapping == 0:
            # Set linear velocities
            t.linear.x = (
                -(self.throttle_axis_state[2] * SCALE_TRANSLATIONAL_X + TRIM_X)
                * self.reverse
            )
            t.linear.y = (
                -(self.throttle_axis_state[5] * SCALE_TRANSLATIONAL_Y + TRIM_Y)
                * self.reverse
            )
            t.linear.z = (
                -(self.throttle_axis_state[1] * SCALE_TRANSLATIONAL_Y + TRIM_Y)
                * self.reverse
            )

            # Set angular velocities
            t.angular.x = (
                -(self.joystick_axis_state[1] * SCALE_ROTATIONAL_X) * self.reverse
            )
            t.angular.y = (
                -(self.joystick_axis_state[0] * SCALE_ROTATIONAL_Y) * self.reverse
            )
            t.angular.z = (
                -(self.joystick_axis_state[2] * SCALE_ROTATIONAL_Z) * self.reverse
            )

            # Set PM
            # PM_grab = self.joystick_button_state[0]
            # PM_pos = self.joystick_button_state[1]

        else:
            # Set linear velocities
            t.linear.x = (
                -(self.joystick_1_axis_state[1] * SCALE_TRANSLATIONAL_X + TRIM_X)
                * self.reverse
            )
            t.linear.y = (
                self.joystick_1_axis_state[0] * SCALE_TRANSLATIONAL_Y + TRIM_Y
            ) * self.reverse
            t.linear.z = (
                -(self.joystick_2_axis_state[2] * SCALE_TRANSLATIONAL_Y + TRIM_Y)
                * self.reverse
            )

            # Set angular velocities
            t.angular.x = 0.0  # no pitch
            t.angular.y = 0.0  # no roll
            t.angular.z = 0.0  # no yaw

            # Set PM
            # PM_grab = self.joystick_button_state[0]
            # PM_pos = self.joystick_button_state[1]

        new_msg = RovVelocityCommand()
        new_msg.twist = t
        new_msg.is_fine = self.is_fine
        new_msg.is_pool_centric = self.is_pool_centric
        new_msg.depth_lock = self.depth_lock
        new_msg.pitch_lock = self.pitch_lock

        return new_msg

    def getTools(self):
        """Returns a ToolsCommandMsg message based on the current gamepad state"""

        tm = ToolsCommandMsg()
        tm.tools = [i for i in self.tools]

        return tm


def main():
    rclpy.init(args=None)
    controller = Controller()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
