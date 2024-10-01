# Worksheet 2: Line Following

## Introduction

In this worksheet you will learn how to make the robot follow a line. You will learn how to make the robot follow a line using a bank of sensors.

## What is required

- The making the robot move motors.py file.
- Thonny
- A robot kit with a maker-line connected. Mentors an help check the connections.

## Connecting to the line sensor

In the code, we need to try the line sensor pins, and see that we can read which are seeing black and which are seeing white.

```python
from machine import Pin
import time

line_1 = Pin(10, Pin.IN)
line_2 = Pin(11, Pin.IN)
line_3 = Pin(12, Pin.IN)
line_4 = Pin(13, Pin.IN)
line_5 = Pin(14, Pin.IN)

while True:
    print(line_1.value(), line_2.value(), line_3.value(), line_4.value(), line_5.value())
    time.sleep(0.1)
```

Explain this code

## Using 1 sensor to detect a line

Use the bang/bang method, and sweep.

## Using 5 seconds with an if

Using 5 sensors, converting them to a number, and using an if to steer

## Smooth line following with proportional control

Using proportional control to follow the line
