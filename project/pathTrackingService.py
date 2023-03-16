from constants import *

def adjustHeading(sColor, motorL, motorR):

    #if detect too much blue, turn left
    if (sColor == "blue"):
        motorR.set_dps(motorL.get_dps() * slowDownFactor)
        motorL.set_dps(normalDps)

    #if detect too red, turn right
    if (sColor == "red"):
        motorR.set_dps(normalDps)
        motorL.set_dps(motorR.get_dps() * slowDownFactor)
        
    #if white, go straight
    if (sColor == "white"):
        motorL.set_dps(normalDps)
        motorR.set_dps(normalDps)