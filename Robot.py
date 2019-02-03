#!/usr/bin/env python3
#import sys sys.path.append()
import sys
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor, GyroSensor
from ev3dev2.led import Leds

class Robot:
    def __init__ (self, sensorList= []):
        
        self.tank = MoveTank(OUTPUT_B,OUTPUT_C) 
        try:
            self.cs = ColorSensor()
        except:
            self.cs = None
        try:
            self.gyro = GyroSensor()
        except:
            self.gyro = None
        try:
            self.ultrasonicSensor = UltrasonicSensor()
        except:
            self.ultrasonicSensor = None

    # note:  this function doesn quite work yet
    def turn(self,degree,leftmotor,rightmotor):
        if self.gyro is None:
            print ("Gyro Needed For All Uses Of Turn")
            sys.exit(1)
        self.tank.on(leftmotor,rightmotor)
        self.gyro.reset()
        self.gyro.wait_until_angle_changed_by(degree)
        self.tank.off()
    def moveUntilDistanceAway(self, distance, speed):
        '''
        the function makes the robot move until it is a certain distance away from an object
        distance is how far away the ultrasonic sensor is from an object
        
        '''
        if self.ultrasonicSensor != None:
            while self.ultrasonicSensor.distance_centimeters_continuous > distance:
                self.tank.on(SpeedPercent(speed),SpeedPercent(speed))
            self.tank.off()

        self.nSensors = 0
            self.ultrasonicSensor = UltrasonicSensor()
        except:
            self.ultrasonicSensor = None
            self.nSensors = 0
        for sensor in sensorList:
            if sensor == "color":
                try:
                    self.cs = ColorSensor()
                    self.nSensors += 1
                except:
                    self.cs = None
        self.allSensorsFound = False
        if self.nSensors == len(sensorList):
            self.allSensorsFound = True
    def flashLEDs (self, color):
        my_leds = Leds()
        my_leds.all_off()
        my_leds.set_color("LEFT", color)
        my_leds.set_color("RIGHT", color)
        my_leds.all_off()
        my_leds.set_color("LEFT", "GREEN")
        my_leds.set_color("RIGHT", "GREEN")
    def moveUntilDistanceAway(self, distance, speed):
        '''
        the function makes the robot move until it is a certain distance away from an object
        distance is how far away the ultrasonic sensor is from an object
        
        '''
        if self.ultrasonicSensor != None:
            print ("Distance:", distance) 
            while self.ultrasonicSensor.distance_centimeters_continuous > distance:
                print ("Distance:", self.ultrasonicSensor.distance_centimeters_continuous)
                self.tank.on(SpeedPercent(10),SpeedPercent(10))
                self.tank.on(SpeedPercent(speed),SpeedPercent(speed))
                self.tank.off()
        else: 
            print ("Error with ultrasonic sensor!")
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

    def goToLine(self, color, range, speed):
        self.cs = ColorSensor()
        while self.cs.reflected_light_intensity < (color-range) or (self.cs.reflected_light_intensity > color+range):
            self.tank.on(SpeedPercent(speed),SpeedPercent(speed))
        self.tank.off()
    def moveForwardRot(self, rotations, speed):
        self.tank.on_for_rotations(speed, speed, rotations)
        self.tank.off()
    def moveForwardCm(self, centimeters, speed, circ):
        self.tank.on_for_rotations(speed, speed, float(centimeters)/circ)
        self.tank.off()
    

