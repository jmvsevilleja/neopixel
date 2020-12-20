from machine import Pin
from neopixel import NeoPixel

pin = 4 # pin digital out
n = 32 # number of leds
np = NeoPixel(Pin(pin,Pin.OUT), n)

# always clear
def clear(num):
    for i in range(num):
        np[i] = (0, 0, 0)
    np.write()