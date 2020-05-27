from controller import Robot, Motor, DistanceSensor, LightSensor, Camera
import math

TIME_STEP = 64
SPEED = 10.0
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
    
camera = wb_robot_get_device("camera");
camera.enable(TIME_STEP);
width = wb_camera_get_width(camera);
height = wb_camera_get_height(camera);
  
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

image = camera.getImage()

#get the pixel from the middle of the image    
for x in range(width/3, 2*width/3):
    for y in range(height/3, 2*height/3:
        red += camera.imageGetRed(image, width, x, y);
        blue += camera.imageGetBlue(image, width, x, y);
        green += camera.imageGetGreen(image, width, x, y);
    
target = [red,blue,green]

correct = 0
    
while robot.step(TIME_STEP) != -1: 
      
    leftSpeed = SPEED
    rightSpeed = SPEED
    
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
    
    image = camera.getImage()
    
    for x in range(0,camera.getWidth()):
        for y in range(0,camera.getHeight()):
            red1 += camera.imageGetRed(image, width, x, y);
            blue1 += camera.imageGetBlue(image, width, x, y);
            green1 += camera.imageGetGreen(image, width, x, y);
    
    colourdetect = [red,blue,green]
    
    for x in range(3):
        if (target[x].getValue() == colourdetect[x].getValue() && correct < 3):
            correct += 1
        elif (target[x].getValue() == colourdetect[x].getValue() && correct == 3):    
            leftSpeed = 0
            rightSpeed = 0
        else
            correct = 0