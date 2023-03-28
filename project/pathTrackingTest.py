
""" Path tracking test file """

from utils.brick import wait_ready_sensors, TouchSensor, Motor, EV3ColorSensor, reset_brick
from utils.sound import Sound
from time import sleep
from constants import *
from colorDetectionService import *
from pathTrackingService import *

#1. Identify the color mix
#2. Change left/right steering vector 
#3. Adjust motor speeds

motorL = Motor("B")          # Motor port C (left)
motorR = Motor("C")          # Motor port B (right)
colorSensorPath = EV3ColorSensor(1) # Color sensor 
emergencyStop = TouchSensor(2)   

wait_ready_sensors()


startMotors(motorL, motorR)

try:
    while (True):

        pathRGB = getRGB(colorSensorPath)
        sColor = getColorDetected(pathRGB)
        print(pathRGB)
        print(getColorDetected(pathRGB))
    
        adjustHeading(sColor, motorL, motorR)
        if emergencyStop.is_pressed():
            raise BaseException

        sleep(0.1)
except BaseException:
    reset_brick()



