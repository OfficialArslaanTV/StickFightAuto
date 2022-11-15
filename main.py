# IF IT DOESN'T WORK, TRY TYPING "pip install pynput pyautogui" IN WINDOWS CMD OR MAC TERMINAL.
import time
import threading
import pyautogui
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char=";")
EXIT_KEY = KeyCode(char="]")

clicking = False
running = True


def clicker():
    while running:
        if clicking:
            pyautogui.press('c') #Replace "c" with your custom stick fight keybind if you have one.
        else:
            cache = ""
            cache.join(cache)
        time.sleep(0.2)


def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking
    if key == EXIT_KEY:
        global running
        clicking = False
        running = False
        exit(0)


print('To start/stop spamming, press ";"')
print('To quit the program, press "]"')
click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()

