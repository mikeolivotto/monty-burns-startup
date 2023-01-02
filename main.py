import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4
from startup import mr_burns

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4, rotate=0)
display.set_backlight(0.6)

# function to clear the screen
def clear():
    display.set_pen(display.create_pen(0, 0, 0))
    display.clear()
    display.update()

# Calls and runs the startup sequence
mr_burns()
clear()