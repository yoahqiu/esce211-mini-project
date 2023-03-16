from constants import *

from ast import literal_eval
from math import sqrt, e, pi
from statistics import mean, stdev

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
    if (r > yR1 and r < yR2 and g > yG1 and g < yG2 and b > yB1 and b < yB2):
        return "yellow"
    
    #purple
    if (r > pR1 and r < pR2 and g > pG1 and g < pG2 and b > pB1 and b < pB2):
        return "purple"
    
    #orange
    if (r > oR1 and r < oR2 and g > oG1 and g < oG2 and b > oB1 and b < oB2):
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
    elif (r > wR1 and r < wR2 and g > wG1 and g < wG2 and b > wB1 and b < wB2):
        return "white"

    return "none"