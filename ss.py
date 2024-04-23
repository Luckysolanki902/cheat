import pyautogui
import keyboard
import os

# Set the directory where screenshots will be saved
save_directory = r"D:\Desktop\cheat\images"

# Ensure the directory exists, create it if not
os.makedirs(save_directory, exist_ok=True)

def take_screenshot():
    # Capture screenshot
    screenshot = pyautogui.screenshot()

    # Save screenshot to specified directory
    screenshot.save(os.path.join(save_directory, "screenshot.png"))

# Define a function to check for key press
def check_hotkey():
    # Check if Ctrl and I are pressed simultaneously
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('i'):
        take_screenshot()

# Continuously check for the hotkey
while True:
    check_hotkey()
