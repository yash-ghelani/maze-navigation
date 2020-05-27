from controller import Robot, Motor, DistanceSensor, Camera, CameraRecognitionObject
import math

TIME_STEP = 64
SPEED = 9.0
robot = Robot()

ds = []
dsNames = ['ds_front_right', 'ds_front_left', 'ds_right1', 'ds_right2', 'ds_right3']

cams = []
camNames = ['cam1', 'cam2']


cam = robot.getCamera('cam1')

for i in range(2):
    cams.append(robot.getCamera(camNames[i]))
    cams[i].enable(TIME_STEP)
    cams[i].recognitionEnable(TIME_STEP)

for i in range(5):
    ds.append(robot.getDistanceSensor(dsNames[i]))
    ds[i].enable(TIME_STEP)
    
wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']

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
        elif direction == "stop":
            leftSpeed = 0.0
            rightSpeed = 0.0
        else:
            leftSpeed = SPEED * -1
            rightSpeed = SPEED
            
        wheels[0].setVelocity(leftSpeed)
        wheels[1].setVelocity(leftSpeed)
        wheels[2].setVelocity(rightSpeed)
        wheels[3].setVelocity(rightSpeed)
        count -= 1

def getColour():
    try:
        colours = cam.getRecognitionObject(0).get_colors()
    except:
        print("colour detection error")
        colours = [0,0,0]

    return colours

#getting the robot started
turn(7, "r")
target = getColour()
print(target)
beaconFound = False

#wall following algorithm        
while robot.step(TIME_STEP) != -1 and beaconFound == False: 
      
    leftSpeed = SPEED
    rightSpeed = SPEED
    
    if ds[0].getValue() < 1000 or ds[1].getValue() < 1000:
        
        print("checking if wall or beacon")        
        try:
            if getColour() == target:
                beaconFound == True
            else:
                turn(7, "l")
        except:
            print("colour detection error")
            turn(8, "l")
        
    elif ds[2].getValue() == 1000 and ds[4].getValue() == 1000 and ds[3].getValue() != 1000:
        turn(3, "s")
        turn(7, "r")
    
    if ds[2].getValue() < ds[3].getValue():
        turn(1, "l")
    
    if ds[2].getValue() > ds[3].getValue():
        turn(1, "r")
                         
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(leftSpeed)
    wheels[2].setVelocity(rightSpeed)
    wheels[3].setVelocity(rightSpeed)
    
print("beacon found, ending sequence")