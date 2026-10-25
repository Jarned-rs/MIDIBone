import usb_midi
from state import state
from config import BASE_NOTE, OFFSETS, VELOCITY

midi = usb_midi.ports[1]

def send(status, data1, data2):
    midi.write(bytes([status, data1, data2]))

def target_note():
    if state.held_note is None:
        return None
    note = BASE_NOTE + OFFSETS[state.held_note]
    note += (state.octave * 12)
    if state.flat == True:
        note -= 1
    return note

def update():
    want = target_note()
    if want == state.sounding:
        return 
    if state.sounding is not None:
        send(0x80, state.sounding, 0)
    if want != None:
        send(0x90, want, VELOCITY)
    state.sounding = want
    state.dirty = True

#sending instrument number to midi ports
def startup():
    midi.write(bytes([0xC0, 56]))
    
