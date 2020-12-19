# Simple Blink of Pin2 LED

from machine import Pin
from machine import PWM
import time

pwm = PWM(Pin(2))
pwm.freq(1)
pwm.duty(512)
