"""
Task-04: Simple Ethical Keylogger - Prodigy InfoTech
FOR EDUCATIONAL PURPOSE ONLY - USE ONLY ON YOUR OWN DEVICE
With explicit user consent.
"""

from pynput import keyboard
import datetime

LOG_FILE = "keylog.txt"

print("="*50)
print("ETHICAL KEYLOGGER - Task 04")
print("FOR EDUCATIONAL USE ONLY")
print("This will log keys YOU type to keylog.txt")
print("Press ESC to stop logging")
print("="*50)

# Consent check
consent = input("Type 'I AGREE TO USE ON MY OWN DEVICE ONLY' to continue: ")
if consent != "I AGREE TO USE ON MY OWN DEVICE ONLY":
    print("Consent not given. Exiting.")
    exit()

# Create log file with timestamp
with open(LOG_FILE, "a") as f:
    f.write(f"\n\n--- Logging started at {datetime.datetime.now()} ---\n")

def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            # Log normal keys
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            else:
                # Log special keys in brackets
                f.write(f" [{key.name}] ")
        print(f"Logged: {key}")
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    # Stop on ESC
    if key == keyboard.Key.esc:
        print("\nESC pressed. Stopping keylogger.")
        print(f"Log saved to {LOG_FILE}")
        return False

print("\nKeylogger STARTED... Type something. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()