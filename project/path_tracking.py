""" This code is deprecated and its feature is now included in padDetection """

from utils.brick import wait_ready_sensors, TouchSensor, Motor, EV3ColorSensor
from utils.sound import Sound
from time import sleep


from ast import literal_eval
from math import sqrt, e, pi
from statistics import mean, stdev


#1. Identify the color mix
#2. Change left/right steering vector 
#3. Adjust motor speeds

motorL = Motor("C")          # Motor port C (left)
motorR = Motor("B")          # Motor port B (right)
motorPusher = Motor("A")        # Motor port A
motorConvBelt = Motor("D")        # Motor port D
colorSensorPath = EV3ColorSensor(1)   # Color sensor 

wait_ready_sensors()

# variables to be calibrated
tresholdBlue = 0.5
tresholdRed = 0.85
tresholdGreen = 0.8
normalDps = 300
slowDownFactor = 0.55

motorL.set_dps(normalDps)
motorR.set_dps(normalDps)

while (True):

    aColors = colorSensorPath.get_rgb() #Hungarian notation, array of [R, G, B] colors
    r, g, b = aColors[0], aColors[1], aColors[2]

    #normalize values between 0 and 1
    denominator = sqrt(r ** 2 + g ** 2 + b ** 2)
    if (denominator <= 0):
        denominator = 1
    r = r/denominator #red will likely be the strongest color
    g = g/denominator
    b = b/denominator #blue will likely appear as black

    print([r, g, b])
    #if detect too much blue, turn left
    if (b > tresholdBlue):
        motorR.set_dps(motorL.get_dps() * slowDownFactor)
        motorL.set_dps(normalDps)

    #if detect too red, turn right
    if (r > tresholdRed):
        motorR.set_dps(normalDps)
        motorL.set_dps(motorR.get_dps() * slowDownFactor)

    #if detect green, launch cube delivery routine
    if (g > tresholdGreen):
        print("detect green")
        
    #if white, go straight
    if (r > 0.55 and r < 0.80 and g > 0.55 and g < 0.80 and b > 0.20 and b < 0.60):
        motorL.set_dps(normalDps)
        motorR.set_dps(normalDps)

    sleep(0.1)


# TODO: explore more gradual control loops where a steering vector is changed
# TODO: in lab, record data in test document + take pictures
# TODO: button on/off
