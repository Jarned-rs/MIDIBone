from kmk.scanners import Scanner
from config import PADS, PRESS_MARGIN, RELEASE_MARGIN
import time
import touchio
import keypad

class TouchScanner(Scanner):
    def __init__(self):
        self.touch_inputs = ([touchio.TouchIn(pin) for pin in PADS])
        self.baselines = [ ]
        for sensor in self.touch_inputs:
            readings = []
            time.sleep(0.01)
            for x in range(0, 5):
                readings.append(sensor.raw_value)
                time.sleep(0.01)
            self.baselines.append(sum(readings)/len(readings))
        self.pressed = ([False] * len(PADS))
        super().__init__()
    @property
    def key_count(self):
        return len(PADS)

    def scan_for_changes(self):
        for index, sensor in enumerate(self.touch_inputs):
            reading = sensor.raw_value
            baseline = self.baselines[index]
            press_threshold = baseline + PRESS_MARGIN
            release_threshold = baseline + PRESS_MARGIN - RELEASE_MARGIN
            if self.pressed[index] != True and reading >= press_threshold:
                self.pressed[index] = True
                return keypad.Event(index, True)
            elif self.pressed[index] == True and reading < release_threshold:
                self.pressed[index] = False
                return keypad.Event(index, False)
        return None
