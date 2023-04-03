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
tone1 = Sound(duration = 1.0, volume = 80, pitch="A3")

def delivery_routine(color):
    global pads_passed
    global delivered
    print("delivery routine")
    print("deliver " + color)
    stopMotors(motorL, motorR)
    sleep(0.05)
    deliver(color, motorPusher, motorConvBelt)
    delivered.append(color)
    startMotors(motorL, motorR)
    sleep(0.05)

wait_ready_sensors()

print("sensors ready")
startMotors(motorL, motorR)
initDeliverySystem(motorPusher, motorConvBelt)
print("all forward!")


delivered = []
pads_passed = 0
in_delivery = False
delivery_count = 0
prevColorsPad = ["none"] * 10
prevColorsPath = ["none"] * 10
prevColorPath = "none"
currColorPath = "none"
prevColorPad = "none"
currColorPad = "none"
is_turning = False
is_fetching = False

while (True):

    pathRGB = getRGB(colorSensorPath)
    sColorPath = getColorDetected(pathRGB)
    prevColorsPath.append(sColorPath)
    prevColorPath = getMostPopularColor(prevColorsPath)
    prevColorsPath.pop(0)
    currColorPath = sColorPath
    
    adjustHeading(sColorPath, motorL, motorR) #control loop that ensure the robot is within the path

    #print("pathRGB: " + str(pathRGB))
    padRGB = getRGB(colorSensorPad)
    sColorPad = getColorDetected(padRGB)
    prevColorsPad.append(sColorPad)
    prevColorPad = getMostPopularColor(prevColorsPad)
    prevColorsPad.pop(0)
    currColorPad = sColorPad
    
    #print("padRGB: " + str(padRGB))
    
        
    if (prevColorPath != "yellow" and currColorPath == "yellow" and is_fetching == True and is_fetching):
        print("turning around")
        sleep(1)
        turnAround(motorR, motorL)
        is_fetching = False
        stopMotors(motorL, motorR)
        tone1.play()
        tone1.wait_done()
            
    if (prevColorPath == "green" and currColorPath != "green" and not is_fetching): #detects falling edge
     #keeps track of the number of pads passed no matter if cube is delivered or not
        in_delivery = True
        if delivery_count == 0:
            pads_passed += 1
        print(pads_passed)
            
            #180deg turn routine
    if (pads_passed >= 6) and (in_delivery == False) and not is_fetching:
        print("turning around")
        sleep(1)
        turnAround(motorR, motorL)
        pads_passed = 0
        delivered = []
        is_fetching = True

        #delivery routine
    if (prevColorPad != "white" and prevColorPad != "none" and currColorPad == "white" and not is_fetching and in_delivery): #detect falling edge
        in_delivery = False
        delivery_count = 0
        if (delivered.count(prevColorPad) < 1): #confirm color not yet delivered
            delivery_routine(prevColorPad)
                
    if in_delivery and not is_fetching: #if robot has been in delivery mode for 5 secs but didn't drop a cube, leave mode
        delivery_count += 1
        if delivery_count == 50:
            delivery_count = 0
            print("in delivery for too long")
            in_delivery = False
                
    print(is_fetching)

    if emergencyStop.is_pressed():
        raise BaseException

    sleep(0.1)



