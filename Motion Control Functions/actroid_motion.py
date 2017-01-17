# Test code to actuate multiple motors from RPi using the PCA9685 PWM generator module

import RPi.GPIO as GPIO
import time
import math

from servofunctions_class import *

import Adafruit_PCA9685

from  _future_ import division

pwm = Adafruit_PCA9685.PCA9685()
motion = jointfunctions()

servo_min = 150
servo_max = 600

frequency = 100

# Functions that this library uses

# pwm.set_pwm(channel, on, off) - 
# pwm.set_pwm_freq(frequency value) - Between 40 and 1000 for ideal operation of a servo 

pwm.set_pwm_freq(frequency)

channel[16] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
init_stand_pwm_values[16] = {385, 385, 150, 385, 385, 375, 385, 385, 600, 345, 375, 355, 0, 0, 0, 0}

def init_stand():
	for index in range(0,16):
		pwm.set_pwm(channel[index], 0, init_stand_pwm_values[index])
		time.sleep(0.020)
		
# Link lengths for the biped
# Lan = Ankle Length
# Lsh = Shin Length
# Lth = Thigh Length 
# Lab = Foot length division 1
# Laf = Foot length division 2
# Following the convention in the research paper by Huang

Lth = 106
Lsh = 86
Lan = 73
Lab = Laf = 50 




#----------------------------------------------------------------------

# Squats for the robot - Depending upon link lengths

def knee_motion(k):
	knee_angle_rad = (math.pi * k)/180
	
	# Angle(in radians) p for the thigh motor - PITCH
	# Angle(in radians) q or the ankle motor - PITCH 
	# central_angle(in radians) for the knee bend
	
	p = math.pi/2 - math.atan((Lth - Lsh*math.cos(knee_angle_rad))/Lsh*math.sin(knee_angle_rad))
	q = math.pi/2 - (knee_angle_rad - math.atan((Lth - Lsh*math.cos(knee_angle_rad))/Lsh*math.sin(knee_angle_rad)))
 	
 	# Knee Pitch movement notification and then action 
 	motion.knee_bending(2)
 	motion.knee_bending(8)
 	
 	motion.right_knee_pitch(k)
 	motion.left_knee_pitch(180-k)
 	
 	# Hip Pitch movement notification and and then action
 	motion.hip_bending(3)
 	motion.hip_bending(9)
 	
 	motion.right_hip_pitch(90-p)
 	motion.left_hip_pitch(90+p)
 	
 	# Ankle Pitch movement notification and then action
 	motion.ankle_bending(1)
 	motion.ankle_bending(7)
 	
 	motion.right_ankle_pitch(90-q)
 	motion.left_ankle_pitch(90-q)

#----------------------------------------------------------------------


for index in range(10):
	knee_motion(90)
	init_stand() 	
 	
 	
 	
	




