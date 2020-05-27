from controller import Robot, Motor, DistanceSensor, Camera, CameraRecognitionObject
import math

TIME_STEP = 64
SPEED = 10.0
robot = Robot()

#device setup
ds = []
dsNames = ['ds_front_right', 'ds_front_left', 'ds_right1', 'ds_right2', 'ds_right3']

cams = []
camNames = ['cam1', 'cam2']
  
wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']

for i in range(1):
    cams.append(robot.getCamera(camNames[i]))
    cams[i].enable(TIME_STEP)
    cams[i].recognitionEnable(TIME_STEP)

for i in range(5):
    ds.append(robot.getDistanceSensor(dsNames[i]))
    ds[i].enable(TIME_STEP)

for i in range(4):
    wheels.append(robot.getMotor(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)

#how much the robot will turn    
def turn(count, direction):

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
            
        wheels[0].setVelocity(leftSpeed)
        wheels[1].setVelocity(leftSpeed)
        wheels[2].setVelocity(rightSpeed)
        wheels[3].setVelocity(rightSpeed)
        count -= 1

#get object colour - try-excepot used for exception handling
def getColour():
    try:
        colours = cams[0].getRecognitionObject(0).get_colors()
    except:
        print("colour detection error")
        colours = [0,0,0]
    return colours

#getting target colour of beacon
turn(7, "r")
target = getColour()
print(target)
beaconFound = False

t = 0

#maze algorithm        
while robot.step(TIME_STEP) != -1 and beaconFound == False: 
      
    leftSpeed = SPEED
    rightSpeed = SPEED
    
    if ds[0].getValue() < 1000 or ds[1].getValue() < 1000:
        
        print(t)
        if t >= 20:
            print("checking if wall or beacon")               
            if getColour() == target:
                beaconFound == True
            else:
                turn(7, "l")
                t = 0
        else:
            turn(7, "l")  
        
    elif ds[2].getValue() == 1000 and ds[4].getValue() == 1000 and ds[3].getValue() != 1000:
        turn(2, "s")
        turn(7, "r")
    
    if ds[2].getValue() < ds[3].getValue():
        turn(1, "l")
    
    if ds[2].getValue() > ds[3].getValue():
        turn(1, "r")
                         
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(leftSpeed)
    wheels[2].setVelocity(rightSpeed)
    wheels[3].setVelocity(rightSpeed)
    
    t += 1
    
print("beacon found, ending sequence")