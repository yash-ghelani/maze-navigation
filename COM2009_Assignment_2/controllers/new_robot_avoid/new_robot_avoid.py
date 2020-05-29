from controller import Robot, Motor, DistanceSensor, Camera, CameraRecognitionObject
import sys

TIME_STEP = 35
SPEED = 9.1
robot = Robot()

#device setup
ds = []
dsNames = ['ds_front_right', 'ds_front_left', 'ds_right1', 'ds_right2', 'ds_right3']
  
wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']

cams = []
camNames = ['cam1', 'cam2']

for i in range(5):
    ds.append(robot.getDistanceSensor(dsNames[i]))
    ds[i].enable(TIME_STEP)

for i in range(4):
    wheels.append(robot.getMotor(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)
    
for i in range(2):
    cams.append(robot.getCamera(camNames[i]))
    cams[i].enable(TIME_STEP)
    cams[i].recognitionEnable(TIME_STEP)

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

#getting colour of obstacle from camera
def getColour(index):
    try:
        obstacleColour = cams[index].getRecognitionObjects()[0].get_colors()
    except:
        print("camera issue")
        obstacleColour = [0,0,0]
        
    return obstacleColour

#getting target colour of beacon
turn(10, "r")
turn(5, "s")
target = getColour(0)
print(target)
turn(8, "l")

t = 0

#maze algorithm        
while robot.step(TIME_STEP) != -1:       
    leftSpeed = SPEED
    rightSpeed = SPEED
    
    if ds[0].getValue() < 1000 or ds[1].getValue() < 1000:
        print("checking if wall or beacon")             
        if getColour(0) == target and t > 50:
            print("found")
            wheels[0].setVelocity(0.0)
            wheels[1].setVelocity(0.0)
            wheels[2].setVelocity(0.0)
            wheels[3].setVelocity(0.0)
            sys.exit()
        else:
            turn(9, "l")
       
    elif ds[2].getValue() == 1000 and ds[4].getValue() == 1000 and ds[3].getValue() < 1000:       
        print("turning corner")        
        turn(4, "s")
        turn(9, "r")
    
    #microadjustments to stick to wall
    elif ds[2].getValue() < ds[3].getValue():
        turn(1, "l")
    elif ds[2].getValue() > ds[3].getValue():
        turn(1, "r")
    else:
        turn(1, "s")
    
    if (t > 50 and t % 5 == 0) and getColour(1) == target:
        turn(10,"l")
    
                         
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(leftSpeed)
    wheels[2].setVelocity(rightSpeed)
    wheels[3].setVelocity(rightSpeed)
    
    t += 1

