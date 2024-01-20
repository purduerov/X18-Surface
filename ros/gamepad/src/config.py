MIN_ABS_DIFFERENCE = 0
<<<<<<< HEAD
=======
# Old ranges for the triggers and sticks
# TRIGGER_DEAD_ZONE = 50
# TRIGGER_RANGE = 1025
# STICK_DEAD_ZONE = 4000
# STICK_RANGE = 32768
>>>>>>> 164d0b84518364b5c093126488319b24d4fd53a9
# New ranges for the triggers and sticks (Probably need to adjust these values)
TRIGGER_DEAD_ZONE = 0.09
TRIGGER_RANGE = 1.0
STICK_DEAD_ZONE = 0.09
STICK_RANGE = 1.0

# Mapping of JoyAxisMotion events to gamepad_state keys
# The number is the axis given by pygame
JOY_AXIS = {1: 'LSY', 0: 'LSX', 4: 'RSY', 3: 'RSX', 2: 'LT', 5: 'RT'}

# Mapping of JoyButton events to gamepad_state keys
# The number is the button given by pygame
JOY_BUTTON = {3: 'Y', 1: 'B', 0: 'A', 2: 'X', 9: 'LSZ', 10: 'RSZ', 4: 'LB', 5: 'RB', 8: 'XBOX', 6: 'START', 7: 'MENU'}
JOY_BUTTON_KEY = {'Y': 3, 'B': 1, 'A': 0, 'X': 2, 'LSZ': 9, 'RSZ': 10, 'LB': 4, 'RB': 5, 'XBOX': 8, 'START': 6, 'MENU': 7}

gamepad_state = {
    "LSX": 0.0,
    "LSY": 0.0,
    "RSX": 0.0,
    "RSY": 0.0,
    "LT": -1.0,
    "RT": -1.0,
    "DPADX": 0,
    "DPADY": 0,
    "Y": 0,
    "B": 0,
    "A": 0,
    "X": 0,
    "LSZ": 0,
    "RSZ": 0,
    "LB": 0,
    "RB": 0,
    "XBOX": 0,
    "START": 0,
    "MENU": 0,
}
