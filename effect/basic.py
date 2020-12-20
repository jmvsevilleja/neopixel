from machine import Pin
from neopixel import NeoPixel
from all.functions import clear

# clear
clear(32)

pin = Pin(4, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 3)   # create NeoPixel driver on GPIO0 for 3 pixels
np[0] = (255, 0, 0) # set the first pixel to white
np[1] = (0, 255, 0) # set the first pixel to white
np[2] = (0, 0, 255) # set the first pixel to white
np.write()              # write data to all pixels
r, g, b = np[0]         # get first pixel colour
print(r,g,b)