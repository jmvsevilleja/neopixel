# Cycle effect
# The cycle effect works similarly to the bounce effect.
# There is a pixel on that runs through all the strip positions while the other pixels are off.

from machine import Pin
from neopixel import NeoPixel
import time

pin = 4 # pin digital out
n = 32 # number of leds
np = NeoPixel(Pin(pin,Pin.OUT), n)

def cycle(r, g, b, wait):
  for i in range(4 * n):
      for j in range(n):
        np[j] = (0, 0, 0)
      np[i % n] = (r, g, b)
      np.write()
      time.sleep_ms(wait)

cycle(10,10,10,10)