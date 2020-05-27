from controller import Robot, Motor, DistanceSensor, Camera, CameraRecognitionObject
import math

TIME_STEP = 64
SPEED = 9.0
robot = Robot()

ds = []
dsNames = ['ds_front_right', 'ds_front_left', 'ds_right1', 'ds_right2', 'ds_right3']

cam = robot.getCamera('cam1')
cam.enable(TIME_STEP)
cam.recognitionEnable(TIME_STEP)

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

def almostStraight():

    val1 = math.floor(ds[2].getValue()/10)
    val2 = math.floor(ds[3].getValue()/10)
    
    if val1 == val2 and ds[2].getValue() != 1000 and ds[3].getValue() != 1000:
        return True
    else:
        return False

def getColour():
    cameraData = cam.getImage()

    r = Camera.imageGetRed(cameraData, cam.getWidth(), 32, 32)
    g = Camera.imageGetGreen(cameraData, cam.getWidth(), 32, 32)
    b = Camera.imageGetBlue(cameraData, cam.getWidth(), 32, 32)
    
    colours = [r,g,b]
    
    return colours

#getting the robot started


# turn(7, "r")
# print(cam.getCameraRecognitionObject(0).get_colors)
# turn(10, "stop")

# turn(7, "r")
# print(cam.getCameraRecognitionObject(0).get_colors)
# turn(10, "stop")


#wall following algorithm        
while robot.step(TIME_STEP) != -1: 
      
    leftSpeed = SPEED
    rightSpeed = SPEED
    
    # #if colour is same as start zone colour, stop.
    # if ls[0].getValue() >= 333 and blueCount < 230:
        # blueCount += 1
    # else:
        # turn(1, "stop")
        # break
    
    if ds[0].getValue() < 850 or ds[1].getValue() < 850:
        colours = getColour()
        print(colours)
        turn(7, "l")
        
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
    
 