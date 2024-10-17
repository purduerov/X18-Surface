MIN_ABS_DIFFERENCE = 0
# New ranges for the triggers and sticks (Probably need to adjust these values)
STICK_DEAD_ZONE = 0.09
AXIS_RANGE = 1.0
# Scale factors for the translational and rotational axes
SCALE_TRANSLATIONAL_X = 1.0
SCALE_TRANSLATIONAL_Y = 1.0
SCALE_TRANSLATIONAL_Z = 1.0
SCALE_ROTATIONAL_X = 1.0
SCALE_ROTATIONAL_Y = 1.0
SCALE_ROTATIONAL_Z = 1.0
# Trim values for the translational axes
TRIM_X = 0.0
TRIM_Y = 0.0
TRIM_Z = 0.0

GAMEPAD_TIMEOUT = 20 # seconds

JOYSTICK_NAME = "Thrustmaster T.16000M"
THROTTLE_NAME = "Thrustmaster TWCS Throttle"

# Store the states of the throttle axies
throttle_axis_state = {
    0: 0.0,
    1: 0.0,
    2: 0.0,
    3: 0.0,
    4: 0.0,
    5: 0.0,
    6: 0.0,
    7: 0.0
}

# Store the states of the throttle buttons
throttle_button_state = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
    13: 0
}

# Store the state of throttle hats
throttle_hat_state = {
    0: 0,
    1: 0
}

# Store the states of the joystick axes
joystick_axis_state = {
    0: 0.0,
    1: 0.0,
    2: 0.0,
    3: 0.0
}

# Store the states of the joystick buttons
joystick_button_state = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
    13: 0
}

# Stores the states of the joystick hats
joystick_hat_state = {
    0: 0,
    1: 0
}
