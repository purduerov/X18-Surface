import pygame
import sys
import time

'''instance_id attribute for events does not work and i don't know why'''

'''x-axis is foward and backward, y-axis is side to side, z-axis is twisting'''
CONT_AXIS_KEY = {
    'X':1, 'Y':0, 'Z':2, 'SLIDE':3
}

THR_AXIS_KEY = {
    'THR':2, 'YAW':3, 'SCR':4, 'SX':0, 'SY':1
}

CONT_AXIS = {
    1:'X', 0:'Y', 2:'Z', 3:'SLIDE'
}

THR_AXIS = {
    2:'THR', 3:'YAW', 4:'SCR', 0:'SX', 1:'SY'
}


CONT_BUTTON_KEY = {
    'trigger':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, '10':9, '11':10, '12':11, '13':12, '14':13,
    '15':14, '16':15
}

CONT_BUTTON = {
    0:'trigger', 1:'2', 2:'3', 3:'4', 4:'5', 5:'6', 6:'7', 7:'8', 8:'9', 9:'10', 10:'11', 11:'12', 12:'13', 13:'14', 
    14:'15', 15:'16'
}

THR_BUTTON_KEY = {
    0:'T1', 1:'T2', 2:'T3', 3:'T4', 4:'T5', 5:'T6', 6:'T7', 7:'T8', 8:'T9', 9:'T10', 10:'T11', 11:'T12', 12:'T13', 13:'T14' 
}

THR_BUTTON = {
    'T1':0, 'T2':1, 'T3':2, 'T4':3, 'T5':4, 'T6':5, 'T7':6, 'T8':7, 'T9':8, 'T10':9, 'T11':10, 'T12':11, 'T13':12, 'T14':13
}

axis_state = {
    'X':0.0,
    'Y':0.0,
    'Z':0.0,
    'SLIDE':0.0,
    'THR':0.0,
    'SCR':0.0,
    'YAW':0.0,
    'SX':0.0,
    'SY':0.0
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
    '12':0,
    '13':0,
    '14':0,
    '15':0,
    '16':0,
    'T1':0,
    'T2':0,
    'T3':0,
    'T4':0,
    'T5':0,
    'T6':0,
    'T7':0,
    'T8':0,
    'T9':0,
    'T10':0,
    'T11':0,
    'T12':0,
    'T13':0,
    'T14':0
}

hat_state = [
    0, 0
]


no_controller = False
wtf = False


def init_pygame():
    '''Initializes pygame and the joystick'''
    global controller
    global throttle
    pygame.init()
    pygame.joystick.init()
    '''check if controller connected'''
    if(pygame.joystick.get_count() != 2):
        print("Not two controllers")
        pygame.quit()
        sys.exit(0)
    controller = pygame.joystick.Joystick(0)
    throttle = pygame.joystick.Joystick(1)


'''get the controller events and update the various states accodingly'''
def check_event():
    for event in pygame.event.get():
        print(event.instance_id)
        if event.instance_id == 0:
            if event.type == pygame.JOYAXISMOTION:
                axis_state[CONT_AXIS[event.axis]] = event.value
            elif event.type == pygame.JOYBUTTONDOWN:
                button_state[CONT_BUTTON[event.button]] = 1
            elif event.type == pygame.JOYBUTTONUP:
                button_state[CONT_BUTTON[event.button]] = 0
            elif event.type == pygame.JOYDEVICEREMOVED:
                print('Disconnect')
                pygame.quit()
                sys.exit(0)
        if event.instance_id == 1:
            if event.type == pygame.JOYAXISMOTION:
                axis_state[THR_AXIS[event.axis]] = event.value
            elif event.type == pygame.JOYBUTTONDOWN:
                button_state[THR_BUTTON[event.button]] = 1
            elif event.type == pygame.JOYBUTTONUP:
                button_state[THR_BUTTON[event.button]] = 0
            elif event.type == pygame.JOYDEVICEREMOVED:
                print('Disconnect')
                pygame.quit()
                sys.exit(0)



    

'''logger to log the axis states to the command line'''
def state_logger():
    for axis, state in axis_state.items():
        print(f"Axis {axis} = {state}", end='  ')
    print()

    # for button, state in button_state.items():
    #     print(f"Button {button} = {state}")
    
    





if __name__ == '__main__':
    init_pygame()
    print(pygame.__version__)
    while True:
        try:
            check_event()
            state_logger()
        except KeyboardInterrupt:
            pygame.quit()
            sys.exit(0)
        except:
            pass
        time.sleep(1)


    