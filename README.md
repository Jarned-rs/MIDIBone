# MIDIBone
a MIDI trombone using basic components to play every note possible! It uses an ESP32-S3-Zero by Waveshare with 4 keys and 7 MIDI keys.

# Features
- An ESP32-S3-Zero
- 7 MIDI note pads that are capacitive and
- 2 keys for octave up&down
- A key for Flats
- An OLED display to show the current note being played

# Hardware and Software
- An ESP32-S3-Zero
- 4 Cherry MX Switxhes
- 7 capacitive and are based on your touch
- A 0.96" OLED to show the note
- Python code to bind the notes to keys ect.

# Python
- code.py           | initializes the main controller
- config.py         | Stores pin assignments
- state.py          | Tracks the current note, flats and octave
- midi_out          | Sends the MIDI messages
- touch_scanner.py  | Reads inputs on the capacitive inputs
- display_ext.py    | Updates the OLED

# Schematic
<img width="1249" height="625" alt="Screenshot 2026-10-25 201132" src="https://github.com/user-attachments/assets/7fab5999-c63c-4a93-a094-c6901aefe526" />

# PCB
<img width="1042" height="459" alt="Screenshot 2026-10-25 201138" src="https://github.com/user-attachments/assets/618f900f-7424-4c97-a60a-2c003fae6251" />

