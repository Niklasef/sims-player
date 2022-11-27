import pygetwindow
import time
import os
import pyautogui
import PIL
import win32api, win32con

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1200

def screenshot():
    p = pyautogui.screenshot(region=(0,0, 1920, 1080))
    p.save(r'C:\\Users\\Niklas\\Projects\\sims-player\\pictures\\\\p.png')


def click(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, int(x/SCREEN_WIDTH*65535.0), int(y/SCREEN_HEIGHT*65535.0))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

screenshot()
x = 100
y = 100
click(x, y)
