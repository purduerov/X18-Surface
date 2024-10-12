MIN_ABS_DIFFERENCE = 0
# New ranges for the triggers and sticks (Probably need to adjust these values)
STICK_DEAD_ZONE = 0.09
AXIS_RANGE = 1.0




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
