from utils.brick import wait_ready_sensors, TouchSensor, Motor
from utils import Sound
from time import sleep


###############################
### Global I/O declarations ###
###############################

touch1 = TouchSensor(1)     # Sensor port 1
touch2 = TouchSensor(2)     # Sensor port 2
touch3 = TouchSensor(3)     # Sensor port 3
enter = TouchSensor(4)      # Sensor port 4
motor = Motor("A")          # Motor port A

wait_ready_sensors()


######################
### Robot commands ###
######################

def play_sound1():
    sound1 = Sound(duration=1, pitch="A1", volume=60)
    sound1.play()


def play_sound2():
    sound2 = Sound(duration=1, pitch="A2", volume=60)
    sound2.play()


def play_sound3():
    sound3 = Sound(duration=1, pitch="A3", volume=60)
    sound3.play()


def play_sound4():
    sound4 = Sound(duration=1, pitch="A4", volume=60)
    sound4.play()


def start_drum():
    pass


def stop_drum():
    pass


def stop_all():
    no_tone = Sound(duration=1, pitch="A1", volume=0)
    no_tone.play()
    stop_drum()


#################
### Main loop ###
#################

while True:
    # While Enter TS is not pressed, do nothing
    if enter.get_raw_value() == 0:
        continue

    # Read command value from TS and concatenate in a 3 bit string
    command = str(touch3.get_raw_value()) + \
        str(touch2.get_raw_value()) + str(touch1.get_raw_value())

    # Switch statement to determine which command to execute
    if command == "000":
        play_sound1()
    elif command == "001":
        play_sound2()
    elif command == "010":
        play_sound3()
    elif command == "011":
        play_sound4()
    elif command == "100":
        start_drum()
    elif command == "101":
        stop_drum()
    elif command == "110":
        pass
    elif command == "111":
        stop_all()

    # Add a delay to slow down processor speed
    sleep(0.3)
