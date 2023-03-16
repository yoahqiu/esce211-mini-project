


""" Cube delivery test file """

from utils.brick import wait_ready_sensors, TouchSensor, Motor, EV3ColorSensor
from utils.sound import Sound
from time import sleep
from constants import *
from colorDetectionService import *
from pathTrackingService import *

#1. Identify the color mix
#2. Change left/right steering vector 
#3. Adjust motor speeds

motorPusher = Motor("A")        # Motor port A
motorConvBelt = Motor("D")        # Motor port D


motorConvBelt.set_dps(-200)
sleep(0.5)
motorConvBelt.set_dps(0)


