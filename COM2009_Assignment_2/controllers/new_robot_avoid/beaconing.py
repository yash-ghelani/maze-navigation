from controller import Robot, Motor, DistanceSensor, LightSensor

TIME_STEP = 64
robot = Robot()

ds = []
dsNames = ['ds_right', 'ds_left']
ls = []
lsNames = ['ls_right', 'ls_left']

for i in range(2):
    ds.append(robot.getDistanceSensor(dsNames[i]))
    ds[i].enable(TIME_STEP)
    
for i in range(2):
    ls.append(robot.getLightSensor(lsNames[i]))
    ls[i].enable(TIME_STEP)
    
wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
for i in range(4):
    wheels.append(robot.getMotor(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)
avoidObstacleCounter = 0
while robot.step(TIME_STEP) != -1:
    leftSpeed = 1.0
    rightSpeed = 1.0
    if avoidObstacleCounter > 0:
        avoidObstacleCounter -= 1
        leftSpeed = 1.0
        rightSpeed = -1.0
    else:  # read sensors
        for i in range(2):
            if ds[i].getValue() < 950.0:
                avoidObstacleCounter = 100
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)

#turn right first to detect colour
lsr_colour = ls[0].getValues()
lsl_colour = ls[1].getValues()
for i in range(3):
    ls_colour[i] = 1/2(lsr_colour[i]+lsl_colour[i])