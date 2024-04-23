import asyncio
import os
import pyautogui
import keyboard
from git import Repo

# Set the directory where screenshots will be saved
save_directory = r"D:\Desktop\cheat\images"

# Ensure the directory exists, create it if not
os.makedirs(save_directory, exist_ok=True)

# Initialize index for naming screenshots
screenshot_index = 1

# Initialize git repo
repo = Repo(save_directory)
git = repo.git

async def take_screenshot_and_push():
    global screenshot_index
    # Capture screenshot
    screenshot = pyautogui.screenshot()

    # Save screenshot to specified directory with unique name
    screenshot_name = f"ril{screenshot_index}.png"
    screenshot_path = os.path.join(save_directory, screenshot_name)
    screenshot.save(screenshot_path)

    # Increment index for the next screenshot
    screenshot_index += 1

    # Add, commit, and push changes
    git.add("--all")
    git.commit("-m", "Added new screenshot")
    await asyncio.sleep(1)  # wait for any previous push to finish if any
    git.push()

# Define a function to check for key press
def check_hotkey():
    # Check if Ctrl and I are pressed simultaneously
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('i'):
        asyncio.ensure_future(take_screenshot_and_push())

# Continuously check for the hotkey
while True:
    check_hotkey()
