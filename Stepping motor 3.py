# Write your code here :-)
from machine import Pin
import time

IN1=Pin(4,Pin.OUT)
IN2=Pin(5,Pin.OUT)
IN3=Pin(14,Pin.OUT)
IN4=Pin(13,Pin.OUT)

a=0.007
while True:
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)
    time.sleep(a)

    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(0)
    time.sleep(a)


    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)
    time.sleep(a)


    IN1.value(0)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)
    time.sleep(a)
