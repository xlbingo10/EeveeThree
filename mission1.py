#!/usr/bin/env python3
#import sys sys.path.append()

from Robot import Robot

#left = True, Right = False
myRobot = Robot()
#myRobot.goToLine(5,5,10)
#myRobot.followLine(True,100) 
myRobot.moveUntilDistanceAway(30, 10)