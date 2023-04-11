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
colorSensorPath = EV3ColorSensor(4)   # Color sensor main
colorSensorPad = EV3ColorSensor(3)
emergencyStop = TouchSensor(2)
tone1 = Sound(duration = 1.0, volume = 100, pitch="A3")

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


delivered = []
pads_passed = 0
in_delivery = False
delivery_count = 0
turning_timer = 0
prevColorsPad = ["white"] * 5
prevColorsPath = ["white"] * 5
prevColorPath = "none"
currColorPath = "none"
prevColorPad = "none"
currColorPad = "none"
is_turning = False
is_fetching = False
run = False
isStarting = True
initDeliverySystem(motorPusher, motorConvBelt)


while(True):
    
    if emergencyStop.is_pressed():
        tone1.play()
        tone1.wait_done()
        delivered = []
        pads_passed = 0
        in_delivery = False
        delivery_count = 0
        turning_timer = 0
        prevColorsPad = ["white"] * 5
        prevColorsPath = ["white"] * 5
        prevColorPath = "none"
        currColorPath = "none"
        prevColorPad = "none"
        currColorPad = "none"
        is_turning = False
        is_fetching = False
        isStarting = True
        run = True

    while(run):
        
        
        if run and isStarting:
            print("sensors ready")
            

            
            
            print("all forward!")
            
            isStarting = False
            print(run)
        

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
        if sColorPad != "white":
            prevColorsPad.append(sColorPad)
        prevColorPad = getMostPopularColor(prevColorsPad)
        if (prevColorPad != "white" or currColorPad != "white"):
            print(prevColorPad, sColorPad)
        if sColorPad != "white":
            prevColorsPad.pop(0)
        currColorPad = sColorPad
        
        #print("padRGB: " + str(padRGB))
        
            
        if (prevColorPath == "yellow" and currColorPath == "yellow" and is_fetching == True):
            print("turning around - yellow")
            print(prevColorPad)
            sleep(1)
            turnAround(motorR, motorL)
            is_fetching = False
            stopMotors(motorL, motorR)
            tone1.play()
            tone1.wait_done()
            run = False
            

                
        if (prevColorPath == "green" and currColorPath != "green" and not is_fetching): #detects falling edge
         #keeps track of the number of pads passed no matter if cube is delivered or not
            in_delivery = True
            print("in delivery")
            if delivery_count == 0:
                pads_passed += 1
                delivery_count = 1
                print(pads_passed)
            print(pads_passed)
            
        if (prevColorPad != "white" and prevColorPad != "none" and (currColorPad == "white" or currColorPad == "none")and (not is_fetching) and in_delivery): #detect falling edge
            print(delivered)
            print(prevColorPad)
            if (delivered.count(prevColorPad) < 1): #confirm color not yet delivered
                delivery_count = 0
                print(prevColorPad)
                delivery_routine(prevColorPad)
                in_delivery = False
            print(delivered)
                
                #180deg turn routine
        if (pads_passed >= 6) and (in_delivery == False) and not is_fetching:
            print("turning around")
            sleep(1)
            motorL.set_dps(normalDps)
            motorR.set_dps(normalDps)
            sleep(3)
            turnAround(motorR, motorL)
            pads_passed = 0
            delivered = []
            is_fetching = True

            #delivery routine                
        if in_delivery and not is_fetching: #if robot has been in delivery mode for 5 secs but didn't drop a cube, leave mode
            delivery_count += 1
            if delivery_count == 60:
                delivery_count = 0
                pads_passed += 1
                print(pads_passed)
                print("in delivery for too long")
                in_delivery = False
                    
        #print(is_fetching)
                
        sleep(0.1)

    

    



