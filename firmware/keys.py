from config import OCTAVE_MIN, OCTAVE_MAX
import state
import midi_out

def note_on(index):
    state.held_note = index
    midi_out.update()

def note_off(index):
    if state.held_note == index:
        state.held_note = None
        midi_out.update()

def flat_on():
    state.flat = True
    midi_out.update()

def flat_off():
    state.flat = False
    midi_out.update()

def octave_up():
    if state.octave < OCTAVE_MAX:
        state.octave += 1
        midi_out.update()

def octave_down():
    if state.octave > OCTAVE_MIN:
        state.octave -= 1
        midi_out.update()

def handle_pad(index, pressed):
    if index >= 0 and index <= 6:
        if pressed == True:
            note_on(index)
        else:
            note_off(index)
    elif index == 7:
        if pressed == True:
            flat_on()
        else:
            flat_off()
    elif index == 8:
        if pressed == True:
            octave_up()
    elif index == 9:
        if pressed == True:
            octave_down()