import pygame
import sys
import time
#axis 0 side to side
#axis 1 forward-backward
#axis 2 rotation


JOY_AXIS = {
    'X':1, 'Y':0, 'Z':2
}

JOY_BUTTON = {
    'trigger':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, '10':9, '11':10, '12':11
}

JOY_BUTTON_KEY = {
    0:'trigger', 1:'2', 2:'3', 3:'4', 4:'5', 5:'6', 6:'7', 7:'8', 8:'9', 9:'10', 10:'11', 11:'12'
}


axis_state = {
    'X':0.0,
    'Y':0.0,
    'Z':0.0
}


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
    controller = pygame.joystick.Joystick(0)


def check_event():
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


def state_logger():
    i = 0
    for axis in axis_state:
        print(f"Axis{i} value: {axis}", end = '')
        i = i + 1
    i = 0
    print()
    for button in button_state:
        print(f"Button{i} value: {button}", end = '')
        i = i + 1
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
    