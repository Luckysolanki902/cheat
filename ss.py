import pyautogui
import keyboard
import os

# Set the directory where screenshots will be saved
save_directory = r"D:\Desktop\cheat"

# Ensure the directory exists, create it if not
os.makedirs(save_directory, exist_ok=True)
import random
screenshot_index = str(random.randint(1000, 9999))
# Initialize index for naming screenshots
screenshot_index = 1

def take_screenshot():
    global screenshot_index
    # Capture screenshot
    screenshot = pyautogui.screenshot()

    # Save screenshot to specified directory with unique name
    screenshot_name = f"ril{screenshot_index}.png"
    screenshot_path = os.path.join(save_directory, screenshot_name)
    screenshot.save(screenshot_path)

    # Increment index for the next screenshot
    screenshot_index += 1

# Define a function to check for key press
def check_hotkey():
    # Check if Ctrl and I are pressed simultaneously
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('i'):
        take_screenshot()

# Continuously check for the hotkey
while True:
    check_hotkey()
