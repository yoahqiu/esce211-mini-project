from utils.brick import wait_ready_sensors, TouchSensor, Motor, EV3ColorSensor
from utils.sound import Sound
from time import sleep


from ast import literal_eval
from math import sqrt, e, pi
from statistics import mean, stdev


#1. Identify the color mix
#2. Change left/right steering vector 
#3. Adjust motor speeds

motorL = Motor("A")          # Motor port A (left)
motorR = Motor("B")          # Motor port B (right)
colorSensorPath = EV3ColorSensor(1)   # Color sensor 

wait_ready_sensors()

# variables to be calibrated
tresholdBlue = 0.3
tresholdRed = 0.8
tresholdGreen = 0.8
normalDps = 90
slowDownFactor = 0.8

motorL.set_dps(normalDps)
motorR.set_dps(normalDps)

while (True):

    aColors = colorSensorPath.get_rgb() #Hungarian notation, array of [R, G, B] colors
    r, g, b = aColors[0], aColors[1], aColors[2]

    #normalize values between 0 and 1
    denominator = sqrt(r ** 2 + g ** 2 + b ** 2)
    r = r/denominator #red will likely be the strongest color
    g = g/denominator
    b = b/denominator #blue will likely appear as black

    #if detect too much blue, turn left
    if (b > tresholdBlue):
        motorL.set_dps(motorL.get_dps * slowDownFactor)
        motorR.set_dps(normalDps)

    #if detect too red, turn right
    if (r > tresholdRed):
        motorL.set_dps(normalDps)
        motorR.set_dps(motorR.get_dps * slowDownFactor)

    #if detect green, launch cube delivery routine 

    sleep(0.3)


# TODO: explore more gradual control loops where a steering vector is changed
# TODO: in lab, record data in test document + take pictures
