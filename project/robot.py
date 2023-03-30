from utils.brick import wait_ready_sensors, TouchSensor, Motor, EV3ColorSensor, reset_brick
from utils.sound import Sound
from time import sleep
from constants import *
from colorDetectionService import *
from pathTrackingService import *
from cubeDeliveryService import *

""" Main code for the robot.
"""

motorL = Motor("B")          # Motor port C (left)
motorR = Motor("C")          # Motor port B (right)
motorPusher = Motor("A")        # Motor port A
motorConvBelt = Motor("D")        # Motor port D
colorSensorPath = EV3ColorSensor(1)   # Color sensor main
colorSensorPad = EV3ColorSensor(3)
emergencyStop = TouchSensor(2)

wait_ready_sensors()

print("sensors ready")
startMotors(motorL, motorR)
initDeliverySystem(motorPusher, motorConvBelt)
print("all forward!")


delivered = []
prevColors = ["none"] * 10
prevColor = "none"
currColor = "none"

while (True):

    pathRGB = getRGB(colorSensorPath)
    sColorPath = getColorDetected(pathRGB)
    #print("pathRGB: " + str(pathRGB))

    padRGB = getRGB(colorSensorPad)
    sColorPad = getColorDetected(padRGB)
    prevColors.append(sColorPad)
    prevColor = getMostPopularColor(prevColors)
    prevColors.pop(0)
    currColor = sColorPad
    #print("padRGB: " + str(padRGB))
    
    adjustHeading(sColorPath, motorL, motorR) #control loop that ensure the robot is within the path

    #180deg turn routine
    if (len(delivered) >= 6):
        print("turning around")
        sleep(1)
        turnAround(motorL, motorR)

    #delivery routine
    if (prevColor != "white" and prevColor != "none" and currColor == "white"): #defect falling edge
        if (delivered.count(prevColor) < 1): #confirm color not yet delivered
            print("delivery routine")
            print("deliver" + prevColor)
            stopMotors(motorL, motorR)
            sleep(0.05)
            deliver(prevColor, motorPusher, motorConvBelt)
            delivered.append(prevColor)
            startMotors(motorL, motorR)
            sleep(0.05)

    if emergencyStop.is_pressed():
        raise BaseException

    sleep(0.1)



