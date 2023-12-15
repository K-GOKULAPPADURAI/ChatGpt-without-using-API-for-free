import pyautogui
import time

# Sleep duration between steps (adjust as needed)
sleep_duration = 4
time.sleep(sleep_duration)
pyautogui.doubleClick(x=196, y=429)
time.sleep(sleep_duration)

# Open the ChatGPT web interface (replace with the actual coordinates)
pyautogui.doubleClick(x=643, y=58)
time.sleep(sleep_duration)

pyautogui.write("https://chat.openai.com/")
pyautogui.hotkey('enter')
time.sleep(3)

# Click on the login button (replace with the actual coordinates)
pyautogui.click(x=575, y=705)
pyautogui.write("who are you bastrad")
pyautogui.hotkey('enter')
time.sleep(sleep_duration)
