import pyautogui
import keyboard
import os
import time
import random
import string
import pytesseract
import asyncio
from PIL import Image
from twilio.rest import Client as TwilioClient
import google.generativeai as genai
import pyperclip
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Twilio credentials and numbers from environment variables
twilio_sid = os.getenv("TWILIO_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_NUMBER")
recipient_number = os.getenv("RECIPIENT_NUMBER")
google_api_key = os.getenv("GOOGLE_API_KEY")

# Set the root directory where screenshots will be saved
root_directory = r"D:\Desktop\cheat"
save_directory = os.path.join(root_directory, "images")

# Ensure the directories exist, create them if not
os.makedirs(save_directory, exist_ok=True)

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Initialize Twilio client
twilio_client = TwilioClient(twilio_sid, twilio_auth_token)

# Configure Google Generative AI
genai.configure(api_key=google_api_key)
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

async def generate_random_string(length):
    """Generate a random string of specified length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

async def take_screenshot_and_send(extract_text_flag=True):
    try:
        # Generate a unique filename
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        random_suffix = await generate_random_string(6)
        filename = f"lirscreenshot_{timestamp}_{random_suffix}.png"

        # Capture screenshot
        screenshot = pyautogui.screenshot()

        # Save screenshot to specified directory
        screenshot_path = os.path.join(save_directory, filename)
        screenshot.save(screenshot_path)

        if extract_text_flag:
            print("Ctrl+I detected. Extracting text from screenshot...")
            # Extract text from screenshot
            extracted_text = await extract_text(filename)
            print("Extracted text:")
            
            # Replace newlines with spaces
            extracted_text = extracted_text.replace('\n', ' ')

            # Copy text to clipboard
            pyperclip.copy(extracted_text)

            # Send the extracted text via Twilio WhatsApp
            send_whatsapp_message(extracted_text)
        else:
            print("Ctrl+M detected. Sending screenshot to Gemini AI...")
            # Send the image to Gemini AI and get the response
            gemini_response = await send_to_gemini(screenshot_path)
            print("Received response from Gemini AI.")
            
            # Copy Gemini response to clipboard
            pyperclip.copy(gemini_response)
            
            send_whatsapp_message(gemini_response)
    except Exception as e:
        print(f"Error in take_screenshot_and_send: {str(e)}")
    finally:
        # Ensure the screenshot file is deleted after processing
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)

async def extract_text(filename):
    try:
        # Use Tesseract-OCR to extract text from image
        text = pytesseract.image_to_string(Image.open(os.path.join(save_directory, filename)))
        return text
    except Exception as e:
        print(f"Error in extract_text: {str(e)}")
        return ""

async def send_to_gemini(image_path):
    try:
        print("Sending image to Gemini AI for processing...")
        convo = model.start_chat(history=[
            {
                "role": "user",
                "parts": [genai.upload_file(image_path)]
            },
        ])
        convo.send_message("Solve this question very accurately, and tell the correct option in the end")
        print("Waiting for response from Gemini AI...")
        return convo.last.text
    except Exception as e:
        print(f"Error in send_to_gemini: {str(e)}")
        return "Failed to process image with Gemini AI."

def send_whatsapp_message(message):
    try:
        start_time = time.time()
        print("Sending message via WhatsApp...")
        twilio_client.messages.create(
            from_="whatsapp:" + twilio_number,
            body=message,
            to="whatsapp:" + recipient_number
        )
        # Record the end time
        end_time = time.time()

        # Calculate the time taken
        elapsed_time = end_time - start_time

        # Print the time taken
        print(f"Took {elapsed_time:.2f} seconds to send it to WhatsApp")
    except Exception as e:
        print(f"Failed to send message via WhatsApp: {str(e)}")

async def check_hotkey():
    try:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('i'):
            await take_screenshot_and_send(extract_text_flag=True)
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('m'):
            await take_screenshot_and_send(extract_text_flag=False)
    except Exception as e:
        print(f"Error in check_hotkey: {str(e)}")

# Continuously check for the hotkey asynchronously
async def main():
    while True:
        try:
            await check_hotkey()
            await asyncio.sleep(0.1)  # Adjust the sleep time as needed for performance
        except Exception as main_loop_error:
            print(f"Error in main loop: {str(main_loop_error)}")
            print("Restarting detection loop...")

# Run the asynchronous event loop
asyncio.run(main())
