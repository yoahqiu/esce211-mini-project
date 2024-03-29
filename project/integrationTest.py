""" System test file """

from utils.brick import wait_ready_sensors, TouchSensor, Motor, EV3ColorSensor, reset_brick
from utils.sound import Sound
from time import sleep
from constants import *
from colorDetectionService import *
from pathTrackingService import *
from cubeDeliveryService import *

#1. Identify the color mix
#2. Change left/right steering vector 
#3. Adjust motor speeds

motorL = Motor("B")          # Motor port C (left)
motorR = Motor("C")          # Motor port B (right)
motorPusher = Motor("A")        # Motor port A
motorConvBelt = Motor("D")        # Motor port D
colorSensorPath = EV3ColorSensor(4) # Color sensor 
colorSensorPad = EV3ColorSensor(3)
emergencyStop = TouchSensor(2)   

wait_ready_sensors()


startMotors(motorL, motorR)
initDeliverySystem(motorPusher, motorConvBelt)

try:
    set_delivery(False)
    while (True):

        pathRGB = getRGB(colorSensorPath)
        sColor = getColorDetected(pathRGB)
        print(pathRGB)
        print(getColorDetected(pathRGB))

        padRGB = getRGB(colorSensorPad)
        sColorPad = getColorDetected(padRGB)

        if not is_in_delivery():
            if sColor == "red" or sColor == "blue" or sColor == "white":
                adjustHeading(sColor, motorL, motorR)

            if ((sColorPad != "none") and (sColorPad != "white")):
                stopMotors(motorL, motorR)
                deliver(sColorPad, motorPusher, motorConvBelt)
                startMotors(motorL, motorR)
                sleep(0.5) #get out of green zone


        if is_in_delivery():
            deliver(sColorPad, motorPusher, motorConvBelt)
            




        if emergencyStop.is_pressed():
            print("stop pressed")
            raise BaseException

        sleep(0.1)

except (BaseException) as err:
    print(err)
    reset_brick()

