from constants import *
from time import sleep

dpsLeft = 0
dpsRight = 0
greenCounter = 0
aLineColors = ["blue", "red"]

def startMotors(motorL, motorR):
    motorL.set_dps(normalDps)
    motorR.set_dps(normalDps)
    
def reStartMotors(motorL, motorR):
    motorL.set_dps(dpsLeft)
    motorR.set_dps(dpsRight)

def stopMotors(motorL, motorR):
    dpsLeft = motorL.get_dps()
    dpsRight = motorR.get_dps()
    motorL.set_dps(0)
    motorR.set_dps(0)

def adjustHeading(sColor, motorL, motorR):

    #if detect too much blue, turn left
    if (sColor == aLineColors[0]):
        motorL.set_dps(motorL.get_dps() * slowDownFactor)
        motorR.set_dps(normalDps/2)

    #if detect too red, turn right
    if (sColor == aLineColors[1]):
        motorR.set_dps(motorR.get_dps() * slowDownFactor)
        motorL.set_dps(normalDps/2)
        
    #if white, go straight
    if (sColor == "white"):
        motorL.set_dps(normalDps)
        motorR.set_dps(normalDps)
        
def turnAround(motorL, motorR):
    motorL.set_dps(0)
    motorR.set_dps(normalDps)
    sleep(turnTime)
    flipHeadingPolarity()
    startMotors(motorL, motorR)
    
def flipHeadingPolarity():
    tmp = aLineColors[0]
    aLineColors[0] = aLineColors[1]
    aLineColors[1] = tmp