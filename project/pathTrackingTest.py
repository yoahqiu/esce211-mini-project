
""" Path tracking test file """

from utils.brick import wait_ready_sensors, TouchSensor, Motor, EV3ColorSensor
from utils.sound import Sound
from time import sleep
from constants import *
from colorDetectionService import *
from pathTrackingService import *

#1. Identify the color mix
#2. Change left/right steering vector 
#3. Adjust motor speeds

motorL = Motor("C")          # Motor port C (left)
motorR = Motor("B")          # Motor port B (right)
colorSensorPath = EV3ColorSensor(1)   # Color sensor 

wait_ready_sensors()


startMotors(motorL, motorR)

while (True):

    pathRBG = getRGB(colorSensorPath)
    sColor = getColorDetected(pathRBG)
    
    adjustHeading(sColor, motorL, motorR)

    sleep(0.1)


