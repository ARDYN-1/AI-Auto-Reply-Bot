import pyautogui
import pyperclip
import time
import google.generativeai as genai

# GEMINI SETUP
genai.configure(api_key="AIzaSyDNu32Dlz685PfqYV0asADapL5fNE5wpiA")

def is_last_message_from_sender(chat_log, sender_name="Lina"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2026] ")[-1]
    if sender_name in messages:
        return True 
    return False

model = genai.GenerativeModel(
    "gemini-3-flash-preview",
    system_instruction="You are a boy named Amit and you can speak hindi ,bengali and as well as English, passionate about coding. Reply shortly and casually."
)

def aiProcess(command):
    response = model.generate_content(command)
    return response.text.strip()

print("🚀 Script started...")
print("👉 Switching to WhatsApp window...")

# Switch to WhatsApp
time.sleep(2)
pyautogui.hotkey("alt", "tab")
time.sleep(2)

# SELECT CHAT

start_x, start_y = 722, 207
end_x, end_y = 1385, 976

while True:
    pyautogui.click(start_x, start_y)
    time.sleep(0.2)

    pyautogui.mouseDown(start_x, start_y)
    pyautogui.moveTo(end_x, end_y, duration=1.5)
    pyautogui.mouseUp()

        # Copy
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)

    copied_text = pyperclip.paste().strip()


    print("📥 Copied Text:\n", copied_text)

        # Deselect CHAT
    pyautogui.click(930, 1021)
    print(is_last_message_from_sender(copied_text))


    if is_last_message_from_sender(copied_text):
        # GEMINI PROCESS
        print("🤖 Sending to Gemini...")
        response = aiProcess(copied_text)

        print("📤 Gemini Reply:\n", response)

            # COPY RESPONSE TO CLIPBOARD (THIS WAS MISSING)
        pyperclip.copy(response)
            # PASTE & SEND
        time.sleep(1)
        pyautogui.click(930, 1021)  
        time.sleep(0.2)

        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.2)
        pyautogui.press("enter")

        print("\n✅ Message sent successfully!")
