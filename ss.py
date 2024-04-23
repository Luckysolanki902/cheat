import pyautogui
import keyboard
import os
import time
import random

# Set the directory where screenshots will be saved
save_directory = r"D:\Desktop\cheat\images"

# Ensure the directory exists, create it if not
os.makedirs(save_directory, exist_ok=True)

def take_screenshot():
    # Generate a random 6-digit number for unique filenames
    random_number = random.randint(100000, 999999)
    # Capture screenshot
    screenshot = pyautogui.screenshot()
    
    # Save screenshot with a unique name
    screenshot_name = f"screenshot_{random_number}.png"
    screenshot.save(os.path.join(save_directory, screenshot_name))

# Define a function to check for key press
def check_hotkey():
    # Check if Ctrl and I are pressed simultaneously
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('i'):
        take_screenshot()

# Keep track of the previous state of hotkeys
prev_hotkey_state = False

# Continuously check for the hotkey
while True:
    # Check for hotkey
    hotkey_state = keyboard.is_pressed('ctrl') and keyboard.is_pressed('i')
    
    # Check for a change in hotkey state
    if hotkey_state and not prev_hotkey_state:
        take_screenshot()
    
    # Update previous hotkey state
    prev_hotkey_state = hotkey_state
    
    # Sleep for a short time to avoid high CPU usage
    time.sleep(0.1)
