#!/usr/bin/env python3
#import sys sys.path.append()

from Robot import Robot

sensorList = ["color"]#, "gyro", "ultra"]
myRobot = Robot(sensorList = sensorList)
if myRobot.allSensorsFound:
    myRobot.flashLEDs("AMBER")
else: 
    myRobot.flashLEDs("RED")