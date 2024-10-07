import pygame
import sys
import time


'''
TODO: 
-test and debug code with actual joystick
-map all of the buttons to their pygame id
-find out how to access the thing on top of the joystick
-move mappings to config file and code to sender file
-delete this file after everything is done
'''

'''x-axis is foward and backward, y-axis is side to side, z-axis is twisting'''
JOY_AXIS = {
    'X':1, 'Y':0, 'Z':2
}

'''mappping from button identifier to pygame id'''
JOY_BUTTON = {
    'trigger':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, '10':9, '11':10, '12':11
}

'''mapping from pygame id button identifier i don't know why we need this'''
JOY_BUTTON_KEY = {
    0:'trigger', 1:'2', 2:'3', 3:'4', 4:'5', 5:'6', 6:'7', 7:'8', 8:'9', 9:'10', 10:'11', 11:'12'
}

'''dict to store the state of the axis as floats'''
axis_state = {
    'X':0.0,
    'Y':0.0,
    'Z':0.0
}

'''dict to store the state of the buttons as booleans'''
button_state = {
    'trigger':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0,
    '9':0,
    '10':0,
    '11':0,
    '12':0
}

no_controller = False
wtf = False


def init_pygame():
    '''Initializes pygame and the joystick'''
    global controller
    pygame.init()
    pygame.joystick.init()
    '''check if controller connected'''
    if(pygame.joystick.get_count() == 0):
        print("No controller found")
        pygame.quit()
        sys.exit(0)
    controller = pygame.joystick.Joystick(0)

'''get the controller events and update the various states accodingly'''
def check_event():
    global no_controller, wtf
    for event in pygame.event.get():
        wtf = False
        if event.type == pygame.JOYAXISMOTION:
            axis_state[event.axis] = event.value
        elif event.type == pygame.JOYBUTTONDOWN:
            button_state[event.button] = 1
        elif event.type == pygame.JOYBUTTONUP:
            button_state[event.button] = 0
        elif event.type == pygame.JOYDEVICEREMOVED:
            no_controller = True
            pygame.quit()
            sys.exit(0)
            state_logger()
        else:
            wtf = True

'''logger to log the axis states to the command line'''
def state_logger():
    for i, axis in enumerate(axis_state):
        print(f"Axis{i} value: {axis_state[axis]}", end = '')
    print()
    for i, button in enumerate(button_state):
        print(f"Button{i} value: {button_state[button]}", end = '')
    print()
    if no_controller == True :
        print("No controller connected")
    if wtf == True :
        print("Unkown event")






if __name__ == '__main__':
    init_pygame()
    while(True):
        check_event()
        state_logger()
        pygame.time.wait(1000)
    