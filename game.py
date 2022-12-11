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

# game area: 950, 565
# origo offset: 8, 41

def inside(ox, oy, currentStateX):
    return ox > currentStateX and ox < (currentStateX+8) and oy > 320 and oy < 330

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

def await_click():
    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128
    while True:
        a = win32api.GetKeyState(0x01)
        if a != state_left:  # Button state changed
            state_left = a
            if a >= 0:
                ox, oy = win32api.GetCursorPos()
                return (ox, oy)
        time.sleep(0.001)

def step(state):
    positions = [162, 297, 442, 531]

    render(state)
    sorted_unclicked = sorted(map(lambda x: int(x), filter(lambda x: x != 'X', state[0])))
    if len(sorted_unclicked) == 0:
        return (state[0], state[1], True)
    current = sorted_unclicked[0]
    current_i = [i for i, x in enumerate(state[0]) if x != 'X' and int(x) == current][0]
    mouse_click_pos = await_click()
    if inside(mouse_click_pos[0], mouse_click_pos[1], positions[current_i]):
        state[0][current_i] = 'X'
    return (state[0], state[1] + 1, state[2])

def main():    
    state = (['1', '2', '3', '4'], 0, False)
    random.shuffle(state[0])
    while not state[2]:
        state = step(state)

main()
print("Won")
