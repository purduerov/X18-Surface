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
# Values are added to the translational axis values after scaling
TRIM_X = 0.0
TRIM_Y = 0.0
TRIM_Z = 0.0

GAMEPAD_TIMEOUT = 20 # seconds

JOYSTICK_NAME = "Thrustmaster T.16000M"
THROTTLE_NAME = "Thrustmaster TWCS Throttle"

# Store the states of the throttle axies
throttle_axis_state = {
    0: 0.0, # throttle back joystick x axis (left-to-right)
    1: 0.0, # throttle back joystick y axis (up-and-down)
    2: 0.0, # throttle slide 
    3: 0.0, # unknown
    4: 0.0, # unknown
    5: 0.0, # throttle back paddle
    6: 0.0, # unknown
    7: 0.0 # throttle left slider
}

# Store the states of the throttle buttons
throttle_button_state = {
    0: 0, # throttle right bottom (orange) button
    1: 0, # throttle back left (orange) button
    2: 0, # throttle back right (orange) button
    3: 0, # throttle back right rocker button up
    4: 0, # throttle back right rocker button down
    5: 0, # throttle back joystick button
    6: 0, # throttle right middle button up
    7: 0, # throttle right middle button forward
    8: 0, # throttle right middle button down
    9: 0, # throttle right middle button back
    10: 0, # throttle right bottm button up
    11: 0, # throttle right bottom button forward
    12: 0, # throttle right bottom button down
    13: 0 # throttle right bottom button back
}

# Store the state of throttle hats
throttle_hat_state = { 
    0: 0, # throttle hat (right top button) front-to-back (left-to-right)
    1: 0  # throttle hat (right top button) up-and-down
}

# Store the states of the joystick axes
joystick_axis_state = {
    0: 0.0, # joystick y axis movement (left-to-right)
    1: 0.0, # joystick x axis movement (front-to-back)
    2: 0.0, # joystick yaw movement (twist)
    3: 0.0 # bottom controller slider
}

# Store the states of the joystick buttons
joystick_button_state = {
    0: 0, # joystick trigger
    1: 0, # joystick top bottom button
    2: 0, # joystick top left button
    3: 0, # joystick top right button
    4: 0, # joystick left top left button
    5: 0, # joystick left top middle button
    6: 0, # joystick left top right button
    7: 0, # joystick left bottom right button
    8: 0, # joystick left bottom middle button
    9: 0, # joystick left bottom left button
    10: 0, # joystick right top right button
    11: 0, # joystick right top middle button
    12: 0, # joystick right top left button
    13: 0, # joystick right bottom left button
    14: 0, # joystick right bottom middle button
    15: 0 # joystick right bottom right button
}

# Stores the states of the joystick hats
joystick_hat_state = {
    0: 0, # joystick hat y axis position (left-to-right)
    1: 0 # joystick hat x axis position (front-to-back)
}
