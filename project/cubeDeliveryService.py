from time import sleep

distances = {
    "relativeDistance" : 0,
    "red" : 0,
    "orange" : 1,
    "yellow" : 2,
    "green" : 3,
    "blue" : 4,
    "purple" : 5
}

in_delivery = False

def initDeliverySystem(motorPusher, motorConvBelt):
    offset = motorPusher.get_position()
    motorPusher.offset_encoder(offset)
    #motorConvBelt.reset_encoder()
    #motorConvBelt.set_power(50)
    

def deliver(color, motorPusher, motorConvBelt):
    #conveyor belt
    motorConvBelt.set_limits(50, 200)
    distanceMove = distances["relativeDistance"] - distances[color] * 100 # move to current - destination
    distances["relativeDistance"] -= distanceMove
    motorConvBelt.set_position_relative(distanceMove)
    sleep(abs(distanceMove)/200)
    
    #motor pusher
    motorPusher.set_limits(100, 130)
    sleep(1)
    motorPusher.set_position_relative(80)
    sleep(1)
    motorPusher.set_position_relative(-80)
    sleep(1)

def set_delivery(state):
    in__delivery = state

def is_in_delivery():
    return in_delivery


    