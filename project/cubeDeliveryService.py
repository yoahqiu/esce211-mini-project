from time import sleep

distances = {
    "red" : 0,
    "orange" : 40,
    "yellow" : 80,
    "green" : 120,
    "blue" : 160,
    "purple" : 200
}

def initDeliverySystem(motorPusher, motorConvBelt):
    motorPusher.reset_encoder()
    motorConvBelt.reset_encoder()

def deliver(color, motorPusher, motorConvBelt):
    motorConvBelt.set_position(distances[color])
    motorPusher.set_position(90)
    sleep(1)
    motorPusher.set_position(0)


    