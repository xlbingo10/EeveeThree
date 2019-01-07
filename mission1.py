#!/usr/bin/env python3
#import sys sys.path.append()

from Robot import Robot

#left = True, Right = False
myRobot = Robot()
myRobot.goToLine(5,5,4) #def goToLine(color, range, speed):
myRobot.followLine(False,100) #def followLine(onLeft,followDistance):

