# Help Me Cheat

This Python script runs in the background and detects key presses. It facilitates the retrieval of answers or questions to your mobile device via WhatsApp:

- **Answer Retrieval**: Press `Ctrl+M` to receive the correct answer along with its solution.
- **Question Extraction**: Press `Ctrl+I` to extract the question text only.

## Features

- Take a screenshot and extract text using OCR (Ctrl + I)
- Take a screenshot and send it to Google Generative AI for processing, which sends the correct answer with solution (Ctrl + M)
- Automatically send the extracted text or AI response via WhatsApp
- Copy the extracted text or AI response to clipboard

## Setup

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Luckysolanki902/cheat
    ```

2. **Install the required Python packages:**

    ```bash
    pip install pyautogui keyboard pytesseract Pillow twilio google-generativeai pyperclip python-dotenv
    ```

3. **Install Tesseract OCR:**

    Download and install Tesseract OCR from [here](https://sourceforge.net/projects/tesseract-ocr-alt/files/tesseract-ocr-setup-3.02.02.exe/download), install it, and make the path availabe as system path variable.

4. **Create a `.env` file in the root directory:**

    ```plaintext
    TWILIO_SID=your_twilio_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    TWILIO_NUMBER=your_twilio_number
    RECIPIENT_NUMBER=recipient_whatsapp_number
    GOOGLE_API_KEY=your_google_api_key
    ```

    Replace the placeholder values with your actual credentials.

5. **Just run the python file and keep it run in background**

```bash
python ./main.py
```

6. **Give your text and press the hot keys**
    - Press ctrl + i to get just the question to your whatsapp
    - Press ctrl + m to get the solution to your whatsapp  


*-Made by Lucky Solanki*


  
