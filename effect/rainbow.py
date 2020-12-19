# Moving raibow effect
# To produce a moving rainbow effect, you need two functions.
# The wheel() function generates the rainbow color spectrum by varying each color parameter between 0 and 255.

from machine import Pin
from neopixel import NeoPixel
import time

pin = 4 # pin digital out
n = 32 # number of leds
np = NeoPixel(Pin(pin,Pin.OUT), n)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def rainbow_cycle(wait):
  for j in range(255):
    for i in range(n):
      rc_index = (i * 256 // n) + j
      np[i] = wheel(rc_index & 255)
    np.write()
    time.sleep_ms(wait)