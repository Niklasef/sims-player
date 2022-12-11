# Code to check if left or right mouse buttons were pressed
import win32api
import time
import os
import random


# First
# 162, 320 - 160, 330 (8x10)
# Second
# 197, 320 - 211, 330
# Third
# 442, 320 - 456, 330
# Fourth
# 525, 320 - 533, 330

# game are: 950, 565
# origo offset: 8, 41

def inside(ox, oy, currentStateX):
    return ox > currentStateX and ox < (currentStateX+8) and oy > 320 and oy < 330

# def step(state):

def render(state):
    os.system('cls')
    print(str(state[1]))
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('________________(' + state[0][0] + ')____________(' + state[0][1] + ')_____________(' + state[0][2] + ')_______(' + state[0][3] + ')__')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('_______________________________________________________________')

def run():
    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128
    positions = [162, 297, 442, 531]
    
    state = (['1', '2', '3', '4'], 0)
    random.shuffle(state[0])
    current = 1
    currentI = [i for i, x in enumerate(state[0]) if int(x) == current][0]
    while True:
        render(state)
        clicked = False
        if current > 4:
            return
        while not clicked:
            a = win32api.GetKeyState(0x01)
            if a != state_left:  # Button state changed
                state_left = a
                if a >= 0:
                    state[1] += 1
                    ox, oy = win32api.GetCursorPos()
                    isInside = inside(ox, oy, positions[currentI])
                    clicked = True
                    if isInside:
                        current += 1
                        state[0][currentI] = 'X'
                        if current <= 4:
                            currentI = [i for i, x in enumerate(state[0]) if x != 'X' and int(x) == current][0]
            time.sleep(0.001)

run()
print("Won")
