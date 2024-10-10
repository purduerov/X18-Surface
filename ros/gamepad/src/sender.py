#!/usr/bin/env python3

'''WIP: WILL NOT RUN -Lucas'''

import pygame
import syss
import time

#ROS
import rclpy
from std_msgs.msg import String, Bool, Empty
from shared_msgs.msg import RovVelocityCommand, ToolsCommandMsg
from geometry_msgs.msg import Twist

from config import *


tools = [0, 0, 0, 0, 0]

SCALE_TRANSLATIONAL_X = 1.0
SCALE_TRANSLATIONAL_Y = 1.0
SCALE_TRANSLATIONAL_Z = 1.0

SCALE_ROTATIONAL_X = 1.0
SCALE_ROTATIONAL_Y = 1.0
SCALE_ROTATIONAL_Z = 1.0

TRIM_X = 0.0
TRIM_Y = 0.0
TRIM_Z = 0.0

REVERSE = 1
LOCKOUT = True
#is fine = 0 = std_mode
#is_fine = 1 = fine_mode
#is_fine = 2 = yeet mode
is_fine = 0
is_pool_centric = False
depth_lock = False
pitch_lock = False
GAMEPAD_TIMEOUT = 20 # seconds


def getMessage():
    '''Returns a RovVelocityCommand message based on the current gamepad state'''
    global gamepad_state
    global is_fine
    global is_pool_centric
    global pitch_lock
    global depth_lock

    t = Twist()

    t.linear.x = -(gamepad_state['X'] * SCALE_TRANSLATIONAL_X + TRIM_X) * REVERSE
    t.linear.y = -(gamepad_state['Y'] * SCALE_TRANSLATIONAL_Y + TRIM_Y) * REVERSE
    t.linear.z = ((gamepad_state['RT'] - gamepad_state['LT']) / 2.0) * SCALE_TRANSLATIONAL_Z + TRIM_Z

    if gamepad_state['3'] == 1:
        x = 1 * SCALE_ROTATIONAL_X
    elif gamepad_state['3'] == 1:
        x = -1 * SCALE_ROTATIONAL_X
    else:
        x = 0.0

    t.angular.x = -x
    t.angular.y = (-gamepad_state['Z'] * SCALE_ROTATIONAL_Y) * REVERSE
    t.angular.z = -gamepad_state['RSX'] * SCALE_ROTATIONAL_Z

    new_msg = RovVelocityCommand()
    new_msg.twist = t
    new_msg.is_fine = is_fine
    new_msg.is_pool_centric = is_pool_centric
    new_msg.depth_lock = depth_lock
    new_msg.pitch_lock = pitch_lock

    return(new_msg)


def getTools():
    '''Returns a ToolsCommandMsg message based on the current gamepad state'''
    global tools

    tm = ToolsCommandMsg()
    tm.tools = [i for i in tools]

    return tm


def correct_raw(raw, abbv):
    '''Corrects the raw value from the gamepad to be in the range [-1.0, 1.0]'''
    if abs(raw) > AXIS_RANGE:
        raw  = raw/abs(raw)
    
    if abbv == 'WHEEL':
        return raw
    else:
        if raw <= STICK_DEAD_ZONE:
            raw  = 0
        return raw


def process_event(event):
    '''Processes a pygame event'''
    global tools
    global is_fine
    global button_state
    global axis_state
    global is_pool_centric
    global depth_lock
    global pitch_lock

    # Button pressed down events
    if event.type == pygame.JOYBUTTONDOWN:
        button_state[JOY_BUTTON_KEY[event.button]] = 1
        
    # Button released events    
    elif event.type == pygame.JOYBUTTONUP:
        button_state[JOY_BUTTON_KEY[event.button]] = 0

    # DPAD buttons
    elif event.type == pygame.JOYHATMOTION:
        if event.value[1] == 1:
            if is_fine < 3:
                is_fine +=1
        elif event.value[1] == -1:
            if is_fine > 0:
                is_fine -=1
        else:
            pass
        if event.value[0] == -1:
            pitch_lock = not pitch_lock
        elif event.value[0] == 1:
            depth_lock = not depth_lock
            is_pool_centric = True
        else:
            pass

    # Joysticks
    elif event.type == pygame.JOYAXISMOTION:
        axis_state[JOY_AXIS_KEY[event.axis]] = correct_raw(event.value, JOY_AXIS_KEY[event.axis])

    
    # If the gamepad is disconnected, try to reconnect it
    elif event.type == pygame.JOYDEVICEREMOVED:
        if not reconnect_gamepad():
            node.get_logger().info("\nNo gamepad found, exiting")
            pygame.quit()
            rclpy.shutdown()
            sys.exit(0)

def pub_data():
    '''Publishes the data to the rov_velocity topic and the tools topic'''
    # Get a message to publish for the rov_velocity topic
    pub.publish(getMessage())
    # Get a message to publish for the tools topic
    pub_tools.publish(getTools())

def update_gamepad():
    '''Updates the gamepad state'''
    # Get all the events from pygame and process them
    for event in pygame.event.get():
        process_event(event)


def init_pygame():
    '''Initializes pygame and the joystick'''
    global joystick
    pygame.init()
    pygame.joystick.init()
    assert pygame.joystick.get_count() == 1
    joystick = pygame.joystick.Joystick(0)


def reconnect_gamepad():
    '''Tries to reconnect the gamepad'''
    global joystick
    reconnected = False
    i = GAMEPAD_TIMEOUT
    while i >= 0 and not reconnected:
        try:
            node.get_logger().info('Gamepad disconnected, reconnect within {:2} seconds'.format(i))
            pygame.init()
            pygame.joystick.init()
            # make sure there is only one joystick
            if pygame.joystick.get_count() == 1:
                # get the first joystick
                joystick = pygame.joystick.Joystick(0)
                reconnected = True
            else:
                pygame.quit()
                assert False
        except:
            # wait 1 second
            pygame.time.wait(1000)
            i -= 1

    if reconnected:
        node.get_logger().info('\nGamepad reconnected')
        joystick = pygame.joystick.Joystick(0)
        
    return reconnected


if __name__ == '__main__':
    global pub, pub_tools, data_thread, gamepad_thread, node

    # Initialize the ros node
    rclpy.init()
    node = rclpy.create_node('gp_pub')
    
    try:
        init_pygame()
    except:
        node.get_logger().info('No gamepad found, please connect a gamepad')
        if not reconnect_gamepad():
            node.get_logger().info("\nNo gamepad found, exiting")
            pygame.quit()
            sys.exit(0)
    
    

    # Create the publishers
    pub = node.create_publisher(RovVelocityCommand, '/rov_velocity', 10)
    pub_tools = node.create_publisher(ToolsCommandMsg, 'tools', 10)

    # Create the timers
    data_thread = node.create_timer(0.1, pub_data)
    gamepad_thread = node.create_timer(0.001, update_gamepad)

    print('ready')

    rclpy.spin(node)

    data_thread.destroy()
    gamepad_thread.destroy()

    # Stop the pygame library
    pygame.quit()

    node.destroy_node()
    rclpy.shutdown()