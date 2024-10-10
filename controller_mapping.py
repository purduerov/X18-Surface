import pygame
import sys
import time


'''
TODO: 
-move mappings to config file and code to sender file
-delete this file after everything is done
'''

'''x-axis is foward and backward, y-axis is side to side, z-axis is twisting'''
JOY_AXIS = {
    'X':1, 'Y':0, 'Z':2, 'WHEEL':3
}

JOY_AXIS_KEY = {
    1:'X', 0:'Y', 2:'Z', 3:'WHEEL'
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
    'Z':0.0,
    'WHEEL':0.0
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

hat_state = [
    0, 0
]


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
        if event.type == pygame.JOYAXISMOTION:
            axis_state[JOY_AXIS_KEY[event.axis]] = event.value
        elif event.type == pygame.JOYBUTTONDOWN:
            button_state[JOY_BUTTON_KEY[event.button]] = 1
        elif event.type == pygame.JOYBUTTONUP:
            button_state[JOY_BUTTON_KEY[event.button]] = 0
        elif event.type == pygame.JOYHATMOTION:
            hat_state[0] = event.value[0]
            hat_state[1] = event.value[1]
        elif event.type == pygame.JOYDEVICEREMOVED:
            no_controller = True
            pygame.quit()
            sys.exit(0)
            state_logger()

'''logger to log the axis states to the command line'''
def state_logger():
    for i,j in enumerate(axis_state):
        print(f"Axis {JOY_AXIS_KEY[i]} value: {axis_state[JOY_AXIS_KEY[i]]}")
    for i,j in enumerate(button_state):
        print(f"Button {JOY_BUTTON_KEY[i]} value: {button_state[JOY_BUTTON_KEY[i]]}")
    print(f"Hat Y: {hat_state[0]}, HAT X: {hat_state[1]}")
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
    