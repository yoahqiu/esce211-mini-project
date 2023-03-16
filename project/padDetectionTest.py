from utils.brick import wait_ready_sensors, TouchSensor, Motor, EV3ColorSensor
from utils.sound import Sound
from time import sleep


from ast import literal_eval
from math import sqrt, e, pi
from statistics import mean, stdev


""" File meant for testing pad color detection and tuning hyperparameter.
"""

motorL = Motor("C")          # Motor port C (left)
motorR = Motor("B")          # Motor port B (right)
colorSensorPath = EV3ColorSensor(1)   # Color sensor main
colorSensorPad = EV3ColorSensor(3)

wait_ready_sensors()

# variables to be calibrated
tresholdBlue = 0.5
tresholdRed = 0.85
tresholdGreen = 0.8
normalDps = 300
slowDownFactor = 0.55
in_delivery_routine = False


def getRBG(colorsensor):
    aColors = colorsensor.get_rgb() #Hungarian notation, array of [R, G, B] colors
    r, g, b = aColors[0], aColors[1], aColors[2]

    #normalize values between 0 and 1
    denominator = sqrt(r ** 2 + g ** 2 + b ** 2)
    if (denominator <= 0):
        denominator = 1
    r = r/denominator 
    g = g/denominator
    b = b/denominator

    return [r, g, b]

def getColorDetected(aRGB):
    r, g, b = aRGB[0], aRGB[1], aRGB[2]
    #yellow
    if (r > 0.70 and r < 0.80 and g > 0.60 and g < 0.70 and b > 0.00 and b < 0.10):
        return "yellow"
    
    #purple
    if (r > 0.90 and r < 0.99 and g > 0.10 and g < 0.20 and b > 0.10 and b < 0.20):
        return "purple"
    
    #orange
    if (r > 0.90 and r < 0.99 and g > 0.20 and g < 0.30 and b > 0.00 and b < 0.10):
        return "orange"
    
    #if detect too much blue, turn left
    elif (b > tresholdBlue):
        return "blue"

    #if detect too red, turn right
    elif (r > tresholdRed):
        return "red"

    #if detect green, launch cube delivery routine
    elif (g > tresholdGreen):
        return "detect green"
        
    #if white, go straight
    elif (r > 0.55 and r < 0.80 and g > 0.55 and g < 0.80 and b > 0.20 and b < 0.60):
        return "white"

    return "none"


while (True):
 
    pathRBG = getRBG(colorSensorPath)
    padRBG = getRBG(colorSensorPad)
    #print(pathRBG)
    
    print(padRBG)
    print(getColorDetected(padRBG))

    sleep(0.5)

