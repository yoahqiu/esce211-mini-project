from utils.brick import wait_ready_sensors, TouchSensor, Motor, EV3ColorSensor
from utils.sound import Sound
from time import sleep
from constants import *
from colorDetectionService import *
from pathTrackingService import *
from cubeDeliveryService import *

""" Main code for the robot.
"""

motorL = Motor("C")          # Motor port C (left)
motorR = Motor("B")          # Motor port B (right)
motorPusher = Motor("A")        # Motor port A
motorConvBelt = Motor("D")        # Motor port D
colorSensorPath = EV3ColorSensor(1)   # Color sensor main
colorSensorPad = EV3ColorSensor(4)

wait_ready_sensors()


startMotors(motorL, motorR)

while (True):

    pathRBG = getRBG(colorSensorPath)
    sColorPath = getColorDetected(pathRBG)

    padRBG = getRBG(colorSensorPad)
    sColorPad = getColorDetected(padRBG)
    
    adjustHeading(sColorPath, motorL, motorR) #control loop that ensure the robot is within the path

    if (sColorPath == "green"): #delivery routine
        stopMotors(motorL, motorR)
        deliver(sColorPad, motorPusher, motorConvBelt)
        startMotors(motorL, motorR)
        sleep(0.5) #get out of green zone

    sleep(0.1)


