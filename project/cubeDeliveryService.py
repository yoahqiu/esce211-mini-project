from time import sleep

distances = {
    "red" : 0,
    "orange" : 100,
    "yellow" : 200,
    "green" : 300,
    "blue" : 400,
    "purple" : 500
}

relativeDistance = 0

def initDeliverySystem(motorPusher, motorConvBelt):
    offset = motorPusher.get_position()
    motorPusher.offset_encoder(offset)
    #motorConvBelt.reset_encoder()
    #motorConvBelt.set_power(50)
    

def deliver(color, motorPusher, motorConvBelt):
    #conveyor belt
    distanceMove = relativeDistance - distances[color]
    relativeDistance += distanceMove
    motorConvBelt.set_position_relative(distanceMove)
    
    #motor pusher
    motorPusher.set_limits(100, 130)
    sleep(1)
    motorPusher.set_position_relative(70)
    sleep(1)
    motorPusher.set_position_relative(-70)
    sleep(1)


    