
from utils.brick import wait_ready_sensors, TouchSensor, Motor, EV3ColorSensor, reset_brick
from utils.sound import Sound
from time import sleep


from ast import literal_eval
from math import sqrt, e, pi
from statistics import mean, stdev

""" Convenience class to stop motors from spinning after carrying out a test.
"""

#1. Identify the color mix
#2. Change left/right steering vector 
#3. Adjust motor speeds

motorL = Motor("C")          # Motor port A (left)
motorR = Motor("B")          # Motor port B (right)
colorSensorPath = EV3ColorSensor(4)   # Color sensor 

wait_ready_sensors()

# variables to be calibrated
tresholdBlue = 0.5
tresholdRed = 0.85
tresholdGreen = 0.8
normalDps = 300
slowDownFactor = 0.60

motorL.set_dps(0)
motorR.set_dps(0)
print("stop")



reset_brick()