from controller import Robot, Motor, DistanceSensor, LightSensor
import math

TIME_STEP = 64
SPEED = 7.0
robot = Robot()

ds = []
dsNames = ['ds_front_right', 'ds_front_left', 'ds_right1', 'ds_right2']
ls = []
lsNames = ['ls_front_right', 'ls_front_left','ls_right']

for i in range(4):
    ds.append(robot.getDistanceSensor(dsNames[i]))
    ds[i].enable(TIME_STEP)
    
for i in range(3):
    ls.append(robot.getLightSensor(lsNames[i]))
    ls[i].enable(TIME_STEP)
    
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
        
#detect colour
target_colour = ls[2].getValues()
        
while robot.step(TIME_STEP) != -1: 
    
    lsr_colour = ls[0].getValues()
    lsl_colour = ls[1].getValues()
    
    while ((ls[0].getValues() or ls[1].getValues()) != target_colour) and 
      (ds[0].getValue() < 850 or ds[1].getValue() < 850):
        leftSpeed = SPEED
        rightSpeed = SPEED
        
        lsr_colour = ls[0].getValues()
        lsl_colour = ls[1].getValues()
        
        if ds[0].getValue() < 850 or ds[1].getValue() < 850:
            turn(10, "l")
        
        #if math.floor(ds[2].getValue() / 10) < ds[3].getValue():
        
        if ds[2].getValue() < ds[3].getValue():
            turn(1, "l")
        
        if ds[2].getValue() > ds[3].getValue():
            turn(1, "r")
                             
        wheels[0].setVelocity(leftSpeed)
        wheels[1].setVelocity(leftSpeed)
        wheels[2].setVelocity(rightSpeed)
        wheels[3].setVelocity(rightSpeed)

    leftSpeed = 0
    rightSpeed = 0