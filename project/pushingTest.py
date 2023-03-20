from utils.brick import wait_ready_sensors, TouchSensor, Motor
from time import sleep


touch1 = TouchSensor(1)
motor = Motor("A")


wait_ready_sensors()

motor.set_power(100)

while True:
    if touch1.get_raw_value() == 0:
        continue

    motor.set_position(motor.get_position() + 90)
    sleep(1)
    motor.set_position(motor.get_position() - 90)
    