from PIL import Image
import pyautogui as pag
import time 
import keyboard

time.sleep(2)

filepath = 'C:\\Users\\visio\\OneDrive\\Desktop\\Yihyun\\2_screenshot\\images'

running = True 
while running:
    if keyboard.is_pressed("ctrl"):
        curr_time = time.strftime("_%Y%m%d_%H%M%S")
        pag.screenshot(f"{filepath}/image{curr_time}.png")
    elif keyboard.is_pressed("esc"):
        running = False

for i in range(1, 4):
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(f"{filepath}/image{curr_time}.png")
    time.sleep(2)
    