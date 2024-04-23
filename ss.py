import pyautogui
import keyboard
import os
import time
import random
import string

# Set the directory where screenshots will be saved
save_directory = r"D:\Desktop\cheat\images"

# Ensure the directory exists, create it if not
os.makedirs(save_directory, exist_ok=True)

def generate_random_string(length):
    """Generate a random string of specified length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def take_screenshot():
    # Generate a unique filename
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    random_suffix = generate_random_string(6)
    filename = f"screenshot_{timestamp}_{random_suffix}.png"
    
    # Capture screenshot
    screenshot = pyautogui.screenshot()

    # Save screenshot to specified directory
    screenshot.save(os.path.join(save_directory, filename))

# Define a function to check for key press
def check_hotkey():
    # Check if Ctrl and I are pressed simultaneously
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('i'):
        take_screenshot()

# Continuously check for the hotkey
while True:
    check_hotkey()
