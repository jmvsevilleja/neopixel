# Bounce effect
# The bounce() function creates a bounce effect and accepts the r, g and b parameters to set the color, and the waiting time.
# The waiting time determines how fast the bouncing effect is.

from machine import Pin
from neopixel import NeoPixel
import time

pin = 4 # pin digital out
n = 32 # number of leds
np = NeoPixel(Pin(pin,Pin.OUT), n)

def bounce(r, g, b, wait):
    for i in range(4 * n):
        for j in range(n):
            np[j] = (r, g, b)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(wait)


bounce(10,10,10,10)