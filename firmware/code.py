from kmk.kmk_keyboard import KMKKeyboard

import config
import midi_out
from display_ext import StaffDisplay
from keys import NOTE_KEYS, flat_key, oct_up, oct_down
from touch_scanner import TouchScanner

keyboard = KMKKeyboard()

keyboard.matrix = TouchScanner(config.PADS)
keyboard.extensions.append(StaffDisplay())

keyboard.keymap = [
    list(NOTE_KEYS) + [flat_key, oct_up, oct_down]
]

midi_out.startup()

if __name__ == '__main__':
    keyboard.go()
