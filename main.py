import pygetwindow
import time
import os
import pyautogui
from PIL import Image
from pytesseract import pytesseract
import win32api, win32con


SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1200

def screenshot(name, x, y):
    p = pyautogui.screenshot(region=(0,0, x, y))
    p.save(r'screenshots\\' + name +'.png')

def click(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, int(x/SCREEN_WIDTH*65535.0), int(y/SCREEN_HEIGHT*65535.0))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def text(image_path):
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pytesseract.tesseract_cmd = path_to_tesseract
    img = Image.open(image_path)
    return pytesseract.image_to_string(img)

screenshot('input', 1980, 1080)
x = 100
y = 100
click(x, y)
time.sleep(0.1)
screenshot('output', 200, 200)
text = text('screenshots\\output.png')
print("success" if 'output' in text else "fail")
