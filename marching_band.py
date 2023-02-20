from utils.brick import wait_ready_sensors, TouchSensor
from utils import sound
from time import sleep

touch1 = TouchSensor(1)
touch2 = TouchSensor(2)
touch3 = TouchSensor(3)
enter = TouchSensor(4)
SOUND1 = sound.Sound(duration=0.3, pitch="A1", volume=60)
SOUND2 = sound.Sound(duration=0.3, pitch="A2", volume=60)
SOUND3 = sound.Sound(duration=0.3, pitch="A3", volume=60)
SOUND4 = sound.Sound(duration=0.3, pitch="A4", volume=60)

wait_ready_sensors()



while True:
    if enter.get_raw_value() == 0:
        continue
    command = str(touch3.get_raw_value()) + str(touch2.get_raw_value()) + str(touch1.get_raw_value())
    #Change the content of the if statements during subsystem 2/3 development (Ralph and Eimy this is for you)
    if command == "000":
        print("1")
    elif command == "001":
        print("2")
    elif command == "010":
        print("3")
    elif command == "011":
        print("4")
    elif command == "100":
        print("Start Drum")    
    elif command == "101":
        print("Stop Drum")
    elif command == "110":
        pass
    elif command == "111":
        print("STOP!")
    sleep(0.3)
    



