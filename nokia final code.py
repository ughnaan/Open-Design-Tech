# Write your code here :-)
from machine import Pin
from hid_services import Keyboard
import time

keyboard = Keyboard("Nokia")
keyboard.start()
keyboard.start_advertising()

bt_connected = False

# HID keycodes
key_map = {
    'a': 0x04, 'b': 0x05, 'c': 0x06,
    'd': 0x07, 'e': 0x08, 'f': 0x09,
    'g': 0x0A, 'h': 0x0B, 'i': 0x0C,
    'j': 0x0D, 'k': 0x0E, 'l': 0x0F,
    'm': 0x10, 'n': 0x11, 'o': 0x12,
    'p': 0x13, 'q': 0x14, 'r': 0x15, 's': 0x16,
    't': 0x17, 'u': 0x18, 'v': 0x19,
    'w': 0x1A, 'x': 0x1B, 'y': 0x1C, 'z': 0x1D,
    'enter': 0x28,
    'space': 0x2C,
    'backspace': 0x2A
}

# Button setup
buttons = {
    1: {'pin': Pin(27, Pin.IN, Pin.PULL_UP), 'chars': ['space']},
    2: {'pin': Pin(25, Pin.IN, Pin.PULL_UP), 'chars': ['a', 'b', 'c']},
    3: {'pin': Pin(18, Pin.IN, Pin.PULL_UP), 'chars': ['d', 'e', 'f']},
    4: {'pin': Pin(14, Pin.IN, Pin.PULL_UP), 'chars': ['g', 'h', 'i']},
    5: {'pin': Pin(32, Pin.IN, Pin.PULL_UP), 'chars': ['j', 'k', 'l']},
    6: {'pin': Pin(5, Pin.IN, Pin.PULL_UP), 'chars': ['m', 'n', 'o']},
    7: {'pin': Pin(12, Pin.IN, Pin.PULL_UP), 'chars': ['p', 'q', 'r', 's']},
    8: {'pin': Pin(26, Pin.IN, Pin.PULL_UP), 'chars': ['t', 'u', 'v']},
    9: {'pin': Pin(15, Pin.IN, Pin.PULL_UP), 'chars': ['w', 'x', 'y', 'z']},
    10: {'pin': Pin(13, Pin.IN, Pin.PULL_UP), 'chars': ['backspace']}
}

# Add state tracking per button
debounce_time = 0.01
timeout = 1.5
for b in buttons.values():
    b['press_count'] = 0
    b['last_press'] = 0
    b['waiting'] = False

# Wait for Bluetooth to connect
while True:
    val = keyboard.get_state()
    print("BT state:", val)
    time.sleep(1)
    if val == 1:
        keyboard.start_advertising()
    if val == 3:
        bt_connected = True
        break

# Main loop
while True:
    for button in buttons.values():
        pin = button['pin']
        if pin.value() == 0:
            current_time = time.time()
            if current_time - button['last_press'] > debounce_time:
                button['press_count'] += 1
                button['last_press'] = current_time
                while pin.value() == 0:
                    time.sleep(0.01)
                button['waiting'] = True

        if button['waiting'] and time.time() - button['last_press'] > timeout:
            press_count = button['press_count']
            chars = button['chars']
            if 1 <= press_count <= len(chars):
                char = chars[press_count - 1]
                code = key_map[char]
                print(f"Typing: {char}")
                keyboard.set_keys(code)
                keyboard.notify_hid_report()
                keyboard.set_keys()
                keyboard.notify_hid_report()
            else:
                print("Too many presses for", chars)
            button['press_count'] = 0
            button['waiting'] = False

    time.sleep(0.01)
