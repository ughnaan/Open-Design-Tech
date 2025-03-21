# Write your code here :-)
from machine import Pin, TouchPad
import neopixel
import time


vibe = Pin(13)
led = Pin(12)

np = neopixel.NeoPixel(Pin(4),16)
touch = TouchPad(Pin(32))
led = Pin(12,Pin.OUT)

def neo_on():
    for i in range(16):
        np[i]=(0,0,255)
        np.write()


def neo_off():
    for i in range(16):
        np[i]=(0,0,0)
        np.write()

while True :
    val = vibe.value()
    touch_val = touch.read()

    if val == 1:
        neo_on()
    else :
        neo_off()
    print(val)

    if touch_val<550:
        led.value(1)
    else :
        led.value(0)
    print(touch_val)

    time.sleep(0.3)



