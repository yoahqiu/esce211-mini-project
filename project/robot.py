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

try:
    while (True):

        pathRGB = getRGB(colorSensorPath)
        sColorPath = getColorDetected(pathRGB)
        print("pathRGB: " + str(pathRGB))

        padRGB = getRGB(colorSensorPad)
        sColorPad = getColorDetected(padRGB)
        print("padRGB: " + str(padRGB))
        
        adjustHeading(sColorPath, motorL, motorR) #control loop that ensure the robot is within the path

        if ((sColorPad != "none") and (sColorPad != "white") and delivered.count(sColorPad) < 1): #delivery routine
            print("delivery routine")
            stopMotors(motorL, motorR)
            deliver(sColorPad, motorPusher, motorConvBelt)
            delivered.append(sColorPad)
            startMotors(motorL, motorR)
            sleep(0.5) #get out of green zone

        if emergencyStop.is_pressed():
            raise BaseException

        sleep(0.05)

except (BaseException) as err:
    print(err)
    reset_brick()


