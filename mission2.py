#!/usr/bin/env python3
#import sys sys.path.append()

from Robot import Robot
myRobot = Robot()
from ev3dev2.sound import Sound
sound = Sound()

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
    myRobot.moveForwardCm(-46,40,16.5)
    sound.speak('Success')
except:
    myRobot.stopAll()
    sound.speak('Exception')