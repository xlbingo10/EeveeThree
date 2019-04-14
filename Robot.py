#!/usr/bin/env python3
#import sys sys.path.append()
import sys, time, math
from ev3dev2.motor import Motor, MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor, GyroSensor
from ev3dev2.led import Leds

class Robot:
    def __init__ (self, sensorList= []):
        try:
            self.tank = MoveTank(OUTPUT_B,OUTPUT_C) 
            self.outputList = [ OUTPUT_B, OUTPUT_C]
        except:
            self.tank = None
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
        try:
            self.large = LargeMotor(OUTPUT_D)
            self.outputList.append(OUTPUT_D)
        except:
            self.large = None
        try:
            self.medium = MediumMotor(OUTPUT_D)
            self.outputList.append(OUTPUT_D)
        except:
            self.medium = None


    # note:  this function doesn quite work yet
    def turn(self,degree,leftmotor,rightmotor):
        if self.gyro is None:
            print ("Gyro Needed For All Uses Of Turn")
            sys.exit(1)
        if self.tank is None:
            print ("Tank Needed For All Uses Of Turn")
            sys.exit(1)
        self.tank.on(leftmotor,rightmotor)
        #self.gyro.reset()
        self.gyro.wait_until_angle_changed_by(degree)
        self.tank.off()
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
        if self.tank is None:
            print ("Tank Needed For All Uses Of moveUntilDistanceAway")
            sys.exit(1)
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
    
        if self.tank is None:
            print ("Tank Needed For All Uses Of followLine")
            sys.exit(1)
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
        if self.tank is None:
            print ("Tank Needed For All Uses Of goToLine")
            sys.exit(1)
        self.cs = ColorSensor()
        while self.cs.reflected_light_intensity < (color-range) or (self.cs.reflected_light_intensity > color+range):
            self.tank.on(SpeedPercent(speed),SpeedPercent(speed))
        self.tank.off()

    def moveMotor(self, speed, lorm, dist):
        if lorm == "M":
            self.medium.on_for_rotations(SpeedPercent(speed), -dist)
            time.sleep(0.5)
            self.medium.on_for_rotations(SpeedPercent(speed), dist)
        if lorm == "L":
            self.large.on_for_rotations(SpeedPercent(speed), -dist)
            time.sleep(0.5)
            self.large.on_for_rotations(SpeedPercent(speed), dist)
        
    
    def moveForwardRot(self, rotations, speed):
        if self.tank is None:
            print ("Tank Needed For All Uses Of moveForwardRot")
            sys.exit(1)
        self.tank.on_for_rotations(speed, speed, rotations)
        self.tank.off()
    def moveForwardCm(self, centimeters, speed, diam):
        
        circ = math.pi*diam
        if self.tank is None:
            print ("Tank Needed For All Uses Of moveForwardCm")
            sys.exit(2)
        self.tank.on_for_rotations(speed, speed, float(centimeters)/circ)
        self.tank.off()
    def stopAll(self):
        self.tank.off()
        try:
            for out in self.outputList:
                m = Motor(out)
                m.stop()
        except:
            pass
