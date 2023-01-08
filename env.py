from game import step, render
import win32api, win32con
from threading import Thread
import time
import pyautogui
from PIL import Image
import random


SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1200

def click(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, int(x/SCREEN_WIDTH*65535.0), int(y/SCREEN_HEIGHT*65535.0))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def screenshot(name, x, y):
    p = pyautogui.screenshot(region=(8, 41, x, y))
    p.save(r'screenshots\\' + name +'.png')

def game_step(state, new_state):
    new_state = step(state)

def step_env(x, y, state):
    game_thread = Thread(target=game_step, args=(state, state))
    game_thread.start()
    time.sleep(0.1)
    click(x, y)
    time.sleep(0.1)
    game_thread.join()
    screenshot('new_state', 950, 565)
    image_state = Image.open('screenshots\\new_state.png').convert('RGB')
    return (image_state, state)

def create_state():
    state = (['1', '2', '3', '4'], 0, False)
    random.shuffle(state[0])
    return state
    

def main():    
    state = (['1', '2', '3', '4'], 0, False)
    state = step_env(165, 325, state)

# main()
