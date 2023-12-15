import pyautogui
from pynput.mouse import Listener

print("Press Ctrl+C to exit the loop.")

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse Clicked! Position: x={x}, y={y}")

# Start the listener
with Listener(on_click=on_click) as listener:
    try:
        while True:
            # Wait for a short duration to avoid excessive checking
            pyautogui.sleep(0.5)

    except KeyboardInterrupt:
        print("\nExiting the loop.")
