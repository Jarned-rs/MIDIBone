class State:
    def __init__(self):
        self.held_note = None
        self.flat = False
        self.octave = 0
        self.sounding = None
        self.dirty= True

state = State()