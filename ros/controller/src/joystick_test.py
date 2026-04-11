import pygame
import time

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No joystick found")
    exit()

joy = pygame.joystick.Joystick(0)
joy.init()

print("Joystick:", joy.get_name())
print("Axes:", joy.get_numaxes())
print("Buttons:", joy.get_numbuttons())

while True:
    pygame.event.pump()

    for i in range(joy.get_numaxes()):
        val = joy.get_axis(i)
        if abs(val) > 0.1:
            print(f"Axis {i}: {val:.3f}")

    for i in range(joy.get_numbuttons()):
        if joy.get_button(i):
            print(f"Button {i} pressed")

    for i in range(joy.get_numhats()):
        hat = joy.get_hat(i)
        if hat != (0, 0):
            print(f"HAT {i}: {hat}")

    time.sleep(0.1)