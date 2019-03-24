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
moveForwardCm(rotations, speed, circ(16.5 on a standard wheel))
moveLargeMotor(speed,lorm(M=medium, L=large))
'''
myRobot.moveForwardCm(45,30,16.5)
myRobot.goToLine(0,10,10)
myRobot.moveMotor(100,"L",0.7)