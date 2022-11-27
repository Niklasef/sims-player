# Code to check if left or right mouse buttons were pressed
import win32api
import time
import os

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128
state = ['1', '2', '3', '4']

while True:
    os.system('cls')
    print('________________(' + state[0] + ')____________(' + state[1] + ')_____________(' + state[2] + ')_______(' + state[3] + ')__')
    clicked = False
    while not clicked:
        a = win32api.GetKeyState(0x01)
        if a != state_left:  # Button state changed
            state_left = a
            if a >= 0:
                clicked = True
                state[0] = 'X'
                ox, oy = win32api.GetCursorPos()
        time.sleep(0.001)
