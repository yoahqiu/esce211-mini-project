from utils.brick import wait_ready_sensors, TouchSensor, Motor, EV3ColorSensor
from utils.sound import Sound
from time import sleep
from constants import *
from colorDetectionService import *


""" File meant for testing pad color detection and tuning hyperparameter.
"""

motorL = Motor("C")          # Motor port C (left)
motorR = Motor("B")          # Motor port B (right)
colorSensorPath = EV3ColorSensor(1)   # Color sensor main
colorSensorPad = EV3ColorSensor(3)

wait_ready_sensors()


while (True):
 
    pathRBG = getRGB(colorSensorPath)
    padRBG = getRGB(colorSensorPad)
    #print(pathRBG)
    
    print(padRBG)
    print(getColorDetected(padRBG))

    sleep(0.5)

