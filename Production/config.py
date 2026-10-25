import board

#note names, offsets, octaves and velocity defining
NOTE_NAMES = ["C", "D", "E", "F", "G", "A", "B"]
OFFSETS = [0, 2, 4, 5, 7, 9, 11]
BASE_NOTE = 48
OCTAVE_MIN = -1
OCTAVE_MAX = 1
VELOCITY = 100

#press and release ratios (untested)
PRESS_RATIO = 0.1
RELEASE_RATIO = 0.05

#defining the keys from the board
MIDI_KEYS_PINS = (
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13,
) 

KEYS_PINS = (
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
)

#display definition
I2C_SDA = board.GP6
I2C_SCL = board.GP5

#adding the MIDI and the KEYS
PADS = MIDI_KEYS_PINS + KEYS_PINS