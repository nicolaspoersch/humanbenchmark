import pyautogui
import time
import random
import keyboard
import winsound

target_color = (75, 219, 106)
active = True

def toggle_program():
    global active
    active = not active
    if active:
        print("Program activated. Use 'Ctrl+Alt+P' to disable.")
        winsound.Beep(1000, 200)
    else:
        print("Program deactivated. Use 'Ctrl+Alt+P' to activate.")
        winsound.Beep(500, 200)

keyboard.add_hotkey('ctrl+alt+p', toggle_program)

banner = """
 █████   █████ ███████████   █████████  ███████████  
░░███   ░░███ ░░███░░░░░███ ███░░░░░███░░███░░░░░███ 
 ░███    ░███  ░███    ░███░███    ░░░  ░███    ░███ 
 ░███████████  ░██████████ ░░█████████  ░██████████  
 ░███░░░░░███  ░███░░░░░███ ░░░░░░░░███ ░███░░░░░███ 
 ░███    ░███  ░███    ░███ ███    ░███ ░███    ░███ 
 █████   █████ ███████████ ░░█████████  █████   █████
░░░░░   ░░░░░ ░░░░░░░░░░░   ░░░░░░░░░  ░░░░░   ░░░░░ 

Program activated. Use 'Ctrl+Alt+P' to deactivate.

Script for the Human Benchmark Reaction Time
by @nicolaspoersch (GitHub)
"""

print(banner)

while True:
    if active:
        x, y = pyautogui.position()
        pixel_color = pyautogui.pixel(x, y)

        if pixel_color == target_color:
            delay = random.uniform(0.15, 0.16)
            time.sleep(delay)
            pyautogui.click(x, y)
