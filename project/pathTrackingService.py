from constants import *
from time import sleep

dpsLeft = normalDps
dpsRight = normalDps
greenCounter = 0
aLineColors = ["blue", "red"]

def startMotors(motorL, motorR):
    dpsLeft = normalDps
    dpsRight = normalDps
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
    if sColor == "orange": #red and orange are too similar in navigation
        sColor = "red"
        
    #if detect too much blue, turn left
    if (sColor == aLineColors[0]):
        dpsLeft = motorL.get_dps() * slowDownFactor
        dpsRight = normalDps*1.2
        motorL.set_dps(dpsLeft)
        motorR.set_dps(dpsRight)
        #print("adjusting left")
        sleep(0.2)
        
    #if detect too red, turn right
    if (sColor == aLineColors[1]):
        dpsRight = motorL.get_dps() * slowDownFactor
        dpsLeft = normalDps*1.2
        motorR.set_dps(dpsRight)
        motorL.set_dps(dpsLeft)
        #print("adjusting right")
        sleep(0.2)
        
    #if white, go straight
    if (sColor == "white" and aLineColors[0] == "blue"):
        dpsRight = motorL.get_dps() * slowDownFactor
        dpsLeft = normalDps*1.2
        motorR.set_dps(dpsLeft)
        motorL.set_dps(dpsRight)
        #print("adjusting right")
        sleep(0.2)
    
    if (sColor == "white" and aLineColors[0] != "blue"): #in reverse path, travserse normally
        motorR.set_dps(normalDps)
        motorL.set_dps(normalDps)
        sleep(0.2)
        
    if (sColor == "green"):
        motorL.set_dps(normalDps)
        motorR.set_dps(normalDps)
        sleep(0.2)
        

        
def turnAround(motorL, motorR):
    motorL.set_dps(normalDps)
    motorR.set_dps(-normalDps)
    sleep(turnTime)
    flipHeadingPolarity()
    startMotors(motorL, motorR)
    
def flipHeadingPolarity():
    tmp = aLineColors[0]
    aLineColors[0] = aLineColors[1]
    aLineColors[1] = tmp