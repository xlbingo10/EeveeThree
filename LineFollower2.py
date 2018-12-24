#!/usr/bin/env python3
#import sys sys.path.append()
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor

class Robot:
    def __init__ (self):
        self.tank = MoveTank(OUTPUT_B,OUTPUT_C) 
        self.cs = ColorSensor()
    def followLine(self,onLeft,followDistance):
        '''
        onLeft, the first perameter, is a True/False value that will
        make the robot run on the left or right side of the line.
        make it True for left and False for Right

        '''
    
        angleMult = 1 #this sets the variable angleMult to 1
        if not onLeft: #If the perameter onLeft is defined as True, then the variable angleMult is 3
            angleMult = 3 #setting angleMult to 3 makes the robot turn in a way so it follows the left side
        for loopcount in range (followDistance): #repeats 100:
            value = self.cs.reflected_light_intensity #value is defined as the color sensor's reflected light intensity
            print(value) #the value of value shows up on the screen
            if value < 50: #if value, the color sensor's light intensity, is less than fifty, the tank moves one way
                self.tank.on(SpeedPercent(10*angleMult),SpeedPercent(30/angleMult))
            else:
                self.tank.on(SpeedPercent(30/angleMult),SpeedPercent(10*angleMult))
        self.tank.off()

def followLine(onLeft, followDistance): #This is what the function followLine does
    '''
    onLeft, the first perameter, is a True/False value that will
    make the robot run on the left or right side of the line.
    make it True for left and False for Right

    '''
    
    angleMult = 1 #this sets the variable angleMult to 1
    if not onLeft: #If the perameter onLeft is defined as True, then the variable angleMult is 3
        angleMult = 3 #setting angleMult to 3 makes the robot turn in a way so it follows the left side
    for loopcount in range (followDistance): #repeats 100:
        value = cs.reflected_light_intensity #value is defined as the color sensor's reflected light intensity
        print(value) #the value of value shows up on the screen
        if value < 50: #if value, the color sensor's light intensity, is less than fifty, the tank moves one way
            tank.on(SpeedPercent(10*angleMult),SpeedPercent(30/angleMult))
        else:
            tank.on(SpeedPercent(30/angleMult),SpeedPercent(10*angleMult))
    tank.off()

def goToLine(color, range):
    global tank
    global cs
    print("here")
    print( cs.reflected_light_intensity )
    while cs.reflected_light_intensity < (color-range) or (cs.reflected_light_intensity > color+range):
        tank.on(SpeedPercent(10),SpeedPercent(10))
        print(cs.reflected_light_intensity)
    tank.off()

#left = True, Right = False
myRobot = Robot()
myRobot.followLine(True,100)

print("Check")
#goToLine(5,5)