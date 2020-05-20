from controller import Robot, Motor, DistanceSensor
import math

TIME_STEP = 64
SPEED = 7.0
robot = Robot()

ds = []
dsNames = ['ds_front_right', 'ds_front_left', 'ds_right1', 'ds_right2']
ls = []
lsNames = ['ls_right', 'ls_left']

for i in range(4):
    ds.append(robot.getDistanceSensor(dsNames[i]))
    ds[i].enable(TIME_STEP)
    
wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']

for i in range(4):
    wheels.append(robot.getMotor(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)
    
def turn(count, direction):
    print(ds[2].getValue(), ds[3].getValue())
    while robot.step(TIME_STEP) != -1 and count > 0:
    
        if direction == "l":
            leftSpeed = SPEED * -1
            rightSpeed = SPEED
        elif direction == "r":
            leftSpeed = SPEED
            rightSpeed = SPEED * -1
        elif direction == "s":
            leftSpeed = SPEED
            rightSpeed = SPEED
        else:
            leftSpeed = SPEED * -1
            rightSpeed = SPEED
            
        wheels[0].setVelocity(leftSpeed)
        wheels[1].setVelocity(leftSpeed)
        wheels[2].setVelocity(rightSpeed)
        wheels[3].setVelocity(rightSpeed)
        count -= 1
        print("turning")

#getting the robot started
turn(10, "r")

        
while robot.step(TIME_STEP) != -1: 
      
    leftSpeed = SPEED
    rightSpeed = SPEED
    
    if ds[0].getValue() < 850 or ds[1].getValue() < 850:
        turn(10, "l")
    
    if ds[2].getValue() == 1000 and ds[3].getValue() != 1000:
        turn(4, "s")
        turn(10, "r")
    
    if ds[2].getValue() < ds[3].getValue():
        turn(1, "l")
    
    if ds[2].getValue() > ds[3].getValue():
        turn(1, "r")
                         
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(leftSpeed)
    wheels[2].setVelocity(rightSpeed)
    wheels[3].setVelocity(rightSpeed)
    