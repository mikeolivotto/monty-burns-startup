from time import sleep
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4
import jpegdec

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, rotate=0)

# Create a new JPEG decoder for our PicoGraphics
j = jpegdec.JPEG(display)

white = display.create_pen(255, 255, 255)
black = display.create_pen(0, 0, 0)

def get_start_position(text):
    width = display.measure_text(text, 1) * 1.95 # Text scale is set to 2, but in reality ~1.95
    return int((240 - width) / 2)

def write(text, position):
    display.set_pen(black)
    display.text(text, position + 2, 117, 220) # Duplicate the text in black with slight offset for shadow effect
    display.set_pen(white)
    display.text(text, position, 115, 220)

def set_image(file):
    j.open_file(file)
    j.decode(0, 0, jpegdec.JPEG_SCALE_FULL)
    
def update_and_pause(time):
    display.update()
    sleep(time)
    
def image_pause(file, time):
    set_image(file)
    update_and_pause(time)
    
def text_over_image(file, text, start_position, time):
    set_image(file)
    write(text, start_position)
    update_and_pause(time)

def speak(text, start_position, open_time, close_time):
    text_over_image("img/open.jpeg", text, start_position, open_time)
    text_over_image("img/closed.jpeg", text, start_position, close_time)

def mr_burns():
    static = ["img/static1.jpeg", "img/static2.jpeg", "img/static3.jpeg", "img/static4.jpeg"]
    for image in static:
        image_pause(image, 0.0005)
    image_pause("img/closed.jpeg", 0.8)

    # Print line 1 to screen
    line_1 = "Hello, Smithers."
    start_position = get_start_position(line_1)
    
    speak("Hello,", start_position, 0.35, 0.2)
    speak("Hello, Smithers.", start_position, 0.25, 0.25)
    
    # Print line 2 to screen
    line_2 = "You're quite good at"
    start_position = get_start_position(line_2)
    
    speak("You're,", start_position, 0.2, 0.1)
    speak("You're quite", start_position, 0.2, 0.1)
    speak("You're quite good", start_position, 0.1, 0.1)
    speak("You're quite good at", start_position, 0.1, 0.2)
    
    # Print line 3 to screen
    line_3 = "turning me on."
    start_position = get_start_position(line_3)
    
    speak("turning", start_position, 0.3, 0.2)
    speak("turning me", start_position, 0.15, 0.15)
    speak("turning me on.", start_position, 0.1, 0.5)
    
    image_pause("img/closed.jpeg", 1.2)
