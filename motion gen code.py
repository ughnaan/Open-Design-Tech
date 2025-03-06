# Write your code here :-)
from machine import Pin
import time

IN1 = Pin(22, Pin.OUT)
IN2 = Pin(21, Pin.OUT)
IN3 = Pin(19, Pin.OUT)
IN4 = Pin(18, Pin.OUT)

# Half-step sequence for faster and smoother movement
step_sequence = [
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (0, 1, 0, 0),
    (0, 1, 1, 0),
    (0, 0, 1, 0),
    (0, 0, 1, 1),
    (0, 0, 0, 1),
    (1, 0, 0, 1),
]

while True:
    for step in step_sequence:
        IN1.value(step[0])
        IN2.value(step[1])
        IN3.value(step[2])
        IN4.value(step[3])
        time.sleep(0.001)
