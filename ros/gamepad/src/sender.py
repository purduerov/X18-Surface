#!/usr/bin/env python3

from inputs import get_gamepad
import pygame
import sys

#ROS
import rclpy
from std_msgs.msg import String, Bool, Empty
from shared_msgs.msg import RovVelocityCommand, ToolsCommandMsg
from geometry_msgs.msg import Twist

from config import *

# Mapping of JoyAxisMotion events to gamepad_state keys
# The number is the axis given by pygame
JOY_AXIS = {1: 'LSY', 0: 'LSX', 4: 'RSY', 3: 'RSX', 2: 'LT', 5: 'RT'}

# Mapping of JoyButton events to gamepad_state keys
# The number is the button given by pygame
JOY_BUTTON = {3: 'Y', 1: 'B', 0: 'A', 2: 'X', 9: 'LSZ', 10: 'RSZ', 4: 'LB', 5: 'RB', 8: 'XBOX', 6: 'START', 7: 'MENU'}
JOY_BUTTON_KEY = {'Y': 3, 'B': 1, 'A': 0, 'X': 2, 'LSZ': 9, 'RSZ': 10, 'LB': 4, 'RB': 5, 'XBOX': 8, 'START': 6, 'MENU': 7}

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
    global gamepad_state
    global is_fine
    global is_pool_centric
    global pitch_lock
    global depth_lock

    t = Twist()

    t.linear.x = -(gamepad_state['LSY'] * SCALE_TRANSLATIONAL_X + TRIM_X) * REVERSE
    t.linear.y = -(gamepad_state['LSX'] * SCALE_TRANSLATIONAL_Y + TRIM_Y) * REVERSE
    t.linear.z = (gamepad_state['RT'] - gamepad_state['LT']) * SCALE_TRANSLATIONAL_Z + TRIM_Z

    if gamepad_state['LB'] == 1:
        x = 1 * SCALE_ROTATIONAL_X
    elif gamepad_state['RB'] == 1:
        x = -1 * SCALE_ROTATIONAL_X
    else:
        x = 0.0

    t.angular.x = -x
    t.angular.y = (-gamepad_state['RSY'] * SCALE_ROTATIONAL_Y) * REVERSE
    t.angular.z = -gamepad_state['RSX'] * SCALE_ROTATIONAL_Z

    new_msg = RovVelocityCommand()
    new_msg.twist = t
    new_msg.is_fine = is_fine
    new_msg.is_pool_centric = is_pool_centric
    new_msg.depth_lock = depth_lock
    new_msg.pitch_lock = pitch_lock

    return(new_msg)

def getTools():
    global tools

    tm = ToolsCommandMsg()
    tm.tools = [i for i in tools]

    return tm

def correct_raw(raw, abbv):
    # Separate the sign from the value
    sign = (raw >= 0) * 2 - 1
    raw = abs(raw)
    # Old code to check if the input is a trigger or a stick
    # if abbv[1] == 'T':
    #     dead_zone = TRIGGER_DEAD_ZONE
    #     value_range = TRIGGER_RANGE
    # else:
    #     dead_zone = STICK_DEAD_ZONE
    #     value_range = STICK_RANGE

    # New code to check if the input is a trigger or a stick
    if abbv == 'LT' or abbv == 'RT':
        dead_zone = TRIGGER_DEAD_ZONE
        value_range = TRIGGER_RANGE
    else:
        dead_zone = STICK_DEAD_ZONE
        value_range = STICK_RANGE

    if raw < dead_zone:
        return 0.0

    # Remove dead zone and scale the value
    raw -= dead_zone
    raw *= value_range / (value_range - dead_zone)
    raw = 1.0 if raw > value_range else raw / value_range
    corrected = round(raw, 3)
    corrected *= sign
    return corrected

def process_event(event):
    global tools
    global is_fine
    global gamepad_state
    global is_pool_centric
    global depth_lock
    global pitch_lock
    # if event.ev_type in ignore_events:
    #     return

    # A, B, X, and Y buttons
    # OLD CODE USING INPUTS LIBRARY
    # if event.ev_type == EVENT_KEY:
    #     gamepad_state[EVENTS[event.code]] = event.state
    #     if event.code == 'BTN_SOUTH' and event.state:
    #         tools[0] = not tools[0]
    #
    #     if event.code == 'BTN_EAST' and event.state:
    #         tools[1] = not tools[1]
    #
    #     if event.code == 'BTN_WEST' and event.state:
    #         tools[2] = not tools[2]
    #
    #     if event.code == 'BTN_NORTH' and event.state and LOCKOUT:
    #         tools[3] = not tools[3]
    #
    #     if event.code == 'BTN_SELECT' and event.state:
    #         is_pool_centric = not is_pool_centric

    # All the buttons
    # NEW CODE USING PYGAME LIBRARY (Includes bumpers, joystick buttons, view, and start)
    if event.type == pygame.JOYBUTTONDOWN:
        gamepad_state[JOY_BUTTON[event.button]] = 1
        if event.button == JOY_BUTTON_KEY['A']:
            tools[0] = not tools[0]

        elif event.button == JOY_BUTTON_KEY['B']:
            tools[1] = not tools[1]

        elif event.button == JOY_BUTTON_KEY['X']:
            tools[2] = not tools[2]
        
        elif event.button == JOY_BUTTON_KEY['Y'] and LOCKOUT:
            tools[3] = not tools[3]
        
        elif event.button == JOY_BUTTON_KEY['MENU']:
            is_pool_centric = not is_pool_centric
        
        

    elif event.type == pygame.JOYBUTTONUP:
        gamepad_state[JOY_BUTTON[event.button]] = 0

    # DPAD buttons
    # OLD CODE USING INPUTS LIBRARY
    # elif event.ev_type == EVENT_ABSOLUTE:
    #     if event.code == 'ABS_HAT0Y' and event.state==-1:
    #         if is_fine < 2:
    #             is_fine +=1
    #     elif event.code == 'ABS_HAT0Y' and event.state==1:
    #         if is_fine > 0:
    #             is_fine -=1
    #     else:
    #         pass
    #     if event.code == 'ABS_HAT0X' and event.state==-1:
    #         pitch_lock = not pitch_lock
    #     elif event.code == 'ABS_HAT0X' and event.state==1:
    #         depth_lock = not depth_lock
    #         is_pool_centric = True
    #     else:
    #         pass

    # DPAD buttons
    # NEW CODE USING PYGAME LIBRARY
    elif event.type == pygame.JOYHATMOTION:
        if event.value[1] == -1:
            if is_fine < 2:
                is_fine +=1
        elif event.value[1] == 1:
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

    # Joysticks?
    # OLD CODE USING INPUTS LIBRARY
    #     gamepad_state[EVENTS[event.code]] = correct_raw(event.state, EVENTS[event.code])

    # Joysticks
    # NEW CODE USING PYGAME LIBRARY
    elif event.type == pygame.JOYAXISMOTION:
        gamepad_state[JOY_AXIS[event.axis]] = correct_raw(event.value, JOY_AXIS[event.axis])

    
    # If the gamepad is disconnected, reconnect it
    elif event.type == pygame.JOYDEVICEREMOVED:
        reconnect_gamepad()
        

    # Not sure what the other events might be
    # else:
    #     gamepad_state[EVENTS[event.code]] = event.state

def pub_data():
    pub.publish(getMessage())
    pub_tools.publish(getTools())

def update_gamepad():
    try:
        event = pygame.event.poll()
        process_event(event)
    except Exception:
        pass
        # logger = node.get_logger().info('no gamepad')
        # rclpy.shutdown()

def init_pygame():
    pygame.init()
    pygame.joystick.init()
    assert pygame.joystick.get_count() == 1

def reconnect_gamepad():
    for i in range(GAMEPAD_TIMEOUT):
        try:
            pygame.init()
            pygame.joystick.init()
            # make sure there is only one joystick
            if pygame.joystick.get_count() == 1:
                # get the first joystick
                joystick = pygame.joystick.Joystick(0)
            else:
                pygame.quit()
                assert False
            # break out of the loop
            reconnected = True
            print('Gamepad reconnected')
            break
        except:
            # wait 1 second
            pygame.time.wait(1000)
    if not reconnected:
        print('Gamepad not reconnected')
        pygame.quit()
        rclpy.shutdown()
        sys.exit(0)


if __name__ == '__main__':
    global pub, pub_tools, data_thread, gamepad_thread

    try:
       get_gamepad()
    except:
        sys.exit(0)

    rclpy.init()
    node = rclpy.create_node('gp_pub')

    pub = node.create_publisher(RovVelocityCommand, 'rov_velocity', 10)
    pub_tools = node.create_publisher(ToolsCommandMsg, 'tools', 10)


    data_thread = node.create_timer(0.1, pub_data)
    gamepad_thread = node.create_timer(0.001, update_gamepad)

    print('ready')

    rclpy.spin(node)

    data_thread.destroy()
    gamepad_thread.destroy()

    # Stop the pygame library
    pygame.quit()

    rclpy.shutdown()