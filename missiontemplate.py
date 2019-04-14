#!/usr/bin/env python3
#import sys sys.path.append()

from Robot import Robot
myRobot = Robot()
import time
'''
"myRobot.":
moveUntilDistanceAway(distance, speed), 
followLine(onLeft(left = True, Right = False),followDistance), 
goToLine(color(B=0, W=100), range, speed),
moveForwardRot(rotations, speed)
moveForwardCm(centimeters, speed, circ(16.5 on a standard wheel))
moveLargeMotor(speed,lorm(M=medium, L=large))
'''
#check
try:
    # my program here
    #del pass
    pass
    sound.speak('Success')
except:
    myRobot.stopAll()
    sound.speak('Exception')



