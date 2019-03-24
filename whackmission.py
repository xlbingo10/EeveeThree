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
moveForwardCm(rotations, speed, diam(5.35 on a standard wheel))
moveLargeMotor(speed,lorm(M=medium, L=large),dist(distance moved))
'''
myRobot.moveForwardCm(45,30,5.35)
myRobot.goToLine(0,10,10)
myRobot.moveMotor(100,"L",0.7)