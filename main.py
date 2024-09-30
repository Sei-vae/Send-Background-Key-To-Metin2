import subprocess
import time
import pyautogui

# Replace the path with the actual path to your application
application_path = r'C:\Users\iamse\Desktop\Zenit - Beyond Limits\Zenit-43.exe'

# Launch the application
subprocess.Popen(application_path)

# Give some time for the application to launch
time.sleep(2)

# Send the hotkey (e.g., Ctrl+C)
pyautogui.press('3')

# You can replace 'ctrl' and 'c' with the desired hotkey combination

# Optionally, you can close the application after sending the hotkey
# subprocess.Popen("taskkill /f /im Zenit-43.exe", shell=True)
