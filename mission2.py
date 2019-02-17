#!/usr/bin/env python3
#import sys sys.path.append()

from Robot import Robot
myRobot = Robot()
'''
"myRobot.":
moveUntilDistanceAway(distance, speed), 
followLine(onLeft(left = True, Right = False),followDistance), 
goToLine(color(B=0, W=100), range, speed),
moveForwardRot(rotations, speed)
moveForwardCm(rotations,speed,circ(16.5 on standard wheel))
moveLargeMotor(speed)
'''
#check
try:
    myRobot.moveForwardCm(46,40,16.5)
    myRobot.moveLargeMotor(20)
except:
    myRobot.stopAll()
