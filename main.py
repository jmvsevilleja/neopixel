from machine import Pin
from neopixel import NeoPixel

# pwm = PWM(Pin(2))
# pwm.freq(1)
# pwm.duty(512)
# def rainbow_cycle(wait, leds):
#     for j in range(leds):
#         for i in range(n):
#             rc_index = (i * 256 // n) + j
#             np[i] = wheel(rc_index & 255)
#     np.write()
#     time.sleep_ms(wait)

pin = 4 # pin digital out
num = 10 # number of leds
np = NeoPixel(Pin(pin,Pin.OUT), num)
# rainbow_cycle(1,10)

# np led array
#np[0] = (255, 0, 0)
#np[1] = (0, 255, 0)
#np[2] = (0, 0, 255)
#np.write()

def clear(num):
    for i in range(num):
        np[i] = (0, 0, 0)
    np.write()
#clear(5)
def set_color(num, r, g, b):
    for i in range(num):
        np[i] = (r, g, b)
    np.write()
# set 10 led colors to white
set_color(num, 1, 1, 1) # max 10 led USB connected
#clear(5)

# leds = range(32)
# pin = Pin(4, Pin.OUT)   # set GPIO4 to output to drive NeoPixels
# np = NeoPixel(pin, len(leds))   # create NeoPixel driver on GPIO0 for 8 pixels

# for led in leds:
#     np[led] = (255, 255, 255)

# np.write()