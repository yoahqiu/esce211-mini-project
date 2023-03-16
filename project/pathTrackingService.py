from constants import *

def startMotors(motorL, motorR):
    motorL.set_dps(normalDps)
    motorR.set_dps(normalDps)

def stopMotors(motorL, motorR):
    motorL.set_dps(0)
    motorR.set_dps(0)

def adjustHeading(sColor, motorL, motorR):

    #if detect too much blue, turn left
    if (sColor == "blue"):
        motorL.set_dps(motorL.get_dps() * slowDownFactor)
        motorR.set_dps(normalDps)

    #if detect too red, turn right
    if (sColor == "red"):
        motorL.set_dps(motorR.get_dps() * slowDownFactor)
        motorR.set_dps(normalDps)
        
    #if white, go straight
    if (sColor == "white"):
        motorL.set_dps(normalDps)
        motorR.set_dps(normalDps)