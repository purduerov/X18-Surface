import pygame
import sys
import time
#axis 0 side to side
#axis 1 forward-backward
#axis 2 rotation


def init_pygame():
    '''Initializes pygame and the joystick'''
    global controller
    pygame.init()
    pygame.joystick.init()
    controller = pygame.joystick.Joystick(0)

def check_axis():
    print(controller.get_axis(0))
    print(controller.get_axis(1))
    print(controller.get_axis(2))

def check_buttons():
    num_of_buttons = controller.get_numbuttons()
    for i in range(0, num_of_buttons):
        print(controller.get_button(i))
def check_button():
    print(controller.get_numbuttons())

def check_joystick():
    pygame.init()
    pygame.joystick.init()

    joystick_count  = pygame.joystick.get_count()

    if joystick_count == 0:
        print("no joystick")

        pygame.quit()
        sys.exit()
    else:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(f"Joystick detected: {joystick.get_name()}")


if __name__ == '__main__':
    init_pygame()
    i = 0
    while i < 30:
        
        check_axis()
        pygame.time.wait(1000)
        i = i + 1

    pygame.quit()
    sys.exit()



        
