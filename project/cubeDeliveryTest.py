""" Cube delivery test file """

from utils.brick import wait_ready_sensors, TouchSensor, Motor, EV3ColorSensor, reset_brick
from utils.sound import Sound
from time import sleep
from constants import *
from colorDetectionService import *
from pathTrackingService import *
from cubeDeliveryService import *

motorPusher = Motor("A")        # Motor port A
motorConvBelt = Motor("D")        # Motor port D
colorSensorPad = EV3ColorSensor(3) # Color sensor fpr the pad
emergencyStop = TouchSensor(2)

wait_ready_sensors()

#1. Identify the color mix
#2. Change left/right steering vector 
#3. Adjust motor speeds

initDeliverySystem(motorPusher, motorConvBelt)

try:
        #padRGB = getRGB(colorSensorPad)
        #sColor = getColorDetected(padRGB)
        #print(padRGB)
        #print(sColor)

        deliver("yellow", motorPusher, motorConvBelt)
        deliver("green", motorPusher, motorConvBelt)
        deliver("red", motorPusher, motorConvBelt)
        deliver("purple", motorPusher, motorConvBelt)
        deliver("blue", motorPusher, motorConvBelt)
        deliver("orange", motorPusher, motorConvBelt)

        sleep(1)
        
        raise BaseException

except (BaseException) as err:
    print(err)
    reset_brick()




