import busio
import displayio
import i2cdisplaybus
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from kmk.extensions import Extension
from state import state
import config

WHITE = 0xFFFFFF

NAMES = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]


def note_name(midi):
    return NAMES[midi % 12] + str(midi // 12 - 1)


class NoteDisplay(Extension):
    def __init__(self):
        displayio.release_displays()
        i2c = busio.I2C(config.I2C_SCL, config.I2C_SDA, frequency=400000)
        bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3C)
        self.display = adafruit_displayio_ssd1306.SSD1306(
            bus, width=128, height=64, auto_refresh=False
        )

        self.note_label = label.Label(
            terminalio.FONT, text="--", scale=4, color=WHITE,
            anchor_point=(0.5, 0.5), anchored_position=(64, 26),
        )
        self.octave_label = label.Label(
            terminalio.FONT, text="Oct 0", color=WHITE,
            anchor_point=(0.5, 0.5), anchored_position=(64, 56),
        )

        group = displayio.Group()
        group.append(self.note_label)
        group.append(self.octave_label)
        self.display.root_group = group

    def _draw(self):
        if state.sounding is None:
            self.note_label.text = "--"
        else:
            self.note_label.text = note_name(state.sounding)

        o = state.octave
        self.octave_label.text = "Oct " + ("+" if o > 0 else "") + str(o)

        self.display.refresh()

    def after_matrix_scan(self, sandbox):
        if not state.dirty:
            return
        self._draw()
        state.dirty = False

    # must exist but do nothing
    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, sandbox):
        return

    def before_matrix_scan(self, sandbox):
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        return

    def on_powersave_enable(self, sandbox):
        return

    def on_powersave_disable(self, sandbox):
        return
