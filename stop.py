#!/usr/bin/env python3
#import sys sys.path.append()

from Robot import Robot
import time
myRobot = Robot()


#"myRobot.":
myRobot.tank.on(10, 10)
time.sleep(5)
myRobot.stopAll()