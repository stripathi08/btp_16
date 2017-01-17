# Declaring a class for all the functions

import RPi.GPIO as RPi
import math
from _future_ import division
import time 

#------------------------------------------------------------------------------------------------------------------------------------------

class jointfunctions():

	current_angle = array(i, [0, 0, 0, 0, 0, 0])		# To set these values while testing after the fabrication is complete 
	channel = array(i, [0, 1, 2, 3, 4, 5])
	'All the functions that drive the joints'
	
	# servo_channel = 0 for the eyes motion  
	# servo_channel = 1 for the jaw motion
	# servo_channel = 2 for the upper lips motion  
	# servo_channel = 3 for the lower lips  motion	
	# servo_channel = 4 for the neck motion - Sideways motion  
	# servo_channel = 5 for the neck motion - Up & Down motion 
# ------------------------------------------------------------------------

	def action_to_perform(self, servo_channel_joint):
		
		if self.servo_channel_joint == 0:
			print 'Eyes movement'
		elif self.servo_channel_joint == 1: 
			print 'Jaw movement'
		elif self.servo_channel_joint == 2:
			print 'Upper lips movement'
		elif self.servo_channel_joint == 3: 
			print 'Lower lips movement'
		elif self.servo_channel_joint == 4:
			print 'Neck sideways movement'
		elif self.servo_channel_joint == 5: 
			print 'Neck up & down movement'	
	
#-------------------------------------------------------------------------
	# Functions for individual control of all the motors/joints

	# Please include the current_angle[] array with initialised values at the start of the main program 

	# Movements include 

	# Eyes - Synchronised left and right motion via the rack and pinion setup

	def eyes(self, angle_eyes):
		
		pwm_start = current_angle[0] * 2.5 + 150 
		pwm_end = self.angle_eyes * 2.5 + 150
		rang = abs((pwm_end - pwm_start)/2) 
			
		if self.angle_eyes >= current_angle[0]:
			rate = 2 
				
		elif self.angle_eyes < current_angle[0]:
			rate = -2
			
		for i in range(int(rang)):
				pwm.set_pwm(channel[0], 0, pwm_start + rate)
				pwm_start += rate
				time.sleep(0.010)
		current_angle[0] = self.angle_eyes	

	# Jaw - Independent jaw up and down motion like that in humans using one jaw piece suspended via one servo motor 

	def jaw(self, angle_jaw):
		
		pwm_start = current_angle[1] * 2.5 + 150 
		pwm_end = self.angle_jaw * 2.5 + 150
		rang = abs((pwm_end - pwm_start)/2) 
			
		if self.angle_jaw >= current_angle[1]:
			rate = 2 
				
		elif self.angle_jaw < current_angle[1]:
			rate = -2
			
		for i in range(int(rang)):
				pwm.set_pwm(channel[1], 0, pwm_start + rate)
				pwm_start += rate
				time.sleep(0.010)
		current_angle[1] = self.angle_jaw	
		

	# Upper lips -  Synchronised sideways divergence and convergence of the two halves of the UPPER LIPS using two spur gears run by one servo motor  

	def upperlips(self, angle_upperlips):
		
		pwm_start = current_angle[2] * 2.5 + 150 
		pwm_end = self.angle_upperlips * 2.5 + 150
		rang = abs((pwm_end - pwm_start)/2) 
			
		if self.angle_upperlips >= current_angle[2]:
			rate = 2 
				
		elif self.angle_upperlips < current_angle[2]:
			rate = -2
			
		for i in range(int(rang)):
				pwm.set_pwm(channel[2], 0, pwm_start + rate)
				pwm_start += rate
				time.sleep(0.010)
		current_angle[2] = self.angle_upperlips	


	# Lower lips -  Synchronised sideways divergence and convergence of the two halves of the LOWER LIPS using two spur gears run by one servo motor  

		
	def lowerlips(self, angle_lowerlips):
		
		pwm_start = current_angle[3] * 2.5 + 150 
		pwm_end = self.angle_lowerlips * 2.5 + 150
		rang = abs((pwm_end - pwm_start)/2) 
			
		if self.angle_lowerlips >= current_angle[3]:
			rate = 2 
				
		elif self.angle_lowerlips < current_angle[3]:
			rate = -2
			
		for i in range (int(rang)):
				pwm.set_pwm(channel[3], 0, pwm_start + rate)
				pwm_start += rate
				time.sleep(0.010)
		current_angle[3] = self.angle_lowerlips

	# Neck sideways motion controlled by one dual-shaft high torque servo motor	

	def necksideways(self, angle_necksideways):
		
		pwm_start = current_angle[4] * 2.5 + 150 
		pwm_end = self.angle_necksideways * 2.5 + 150
		rang = abs((pwm_end - pwm_start)/2) 
			
		if self.angle_necksideways >= current_angle[4]:
			rate = 2 
				
		elif self.angle_necksideways < current_angle[4]:
			rate = -2
			
		for i in range(int(rang)):
				pwm.set_pwm(channel[4], 0, pwm_start + rate)
				pwm_start += rate
				time.sleep(0.010)
		current_angle[4] = self.angle_necksideways

	# Neck up & down motion controlled by one DC motor -  Power transmission is done via a belt drive mechanism		
		
	def neckupdown(self, angle_neckupdown):
		
					
		if self.angle_neckupdown >= current_angle[5]:
			rate = 2 
				
		elif self.angle_neckupdown < current_angle[5]:
			rate = -2
			
		for i in range(int(rang)):
				pwm.set_pwm(channel[10], 0, pwm_start + rate)       # INCOMPLETE or INCORRECT FUNCTION - SHALL BE SOLVED IN THE LAST
				pwm_start += rate
				time.sleep(0.010)
		current_angle[10] = self.angle_neckupdown



# Mention the action sequence to generate various kinds of motions 

#-----------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------------
class movements(jointunctions):

	

	'All the individual movements that produce expressions '
# ----------------- MOVEMENTS FOR EYES -----------------------------

	def eyes_to_fro(self, extent):



		# Deduce angular displacement from the physical model = Let that variable be angle_disp initialised with 0 for now.

		angle_disp = 0

		# Let's consider the maximum displacement to be 5 cms on either sides that gives the maximum anglular displacement of 30 degrees on 
		# either side. So, with the neutral being at 90 degrees -  The sway should be 90 +- 30 = 60/120. We only take a note of the final 
		# angle value. This is with respect to the servo motor acting as a pinion that drives the rack to which the eyballs are connected

		# This to & fro motion can be done with any current angle location as the center.

		max_angle = current_angle[0] + angle_disp
		min_angle = current_angle[0] - angle_disp

		eyes(max_angle)
		eyes(min_angle)


	def eyes_oneway(self, extent):

		# Deduce the relation between the extent of motion and the angular displacement in the same scenario => Deduce relation between extent and final_angle
		# For now we keep the final_angle as an initialised value of 0

		final_angle = 0

		eyes(final_angle)
		
	def jaws_to_fro(self, extent_angle):
		
		# Mention the extent of to and fro motion - How much of laughter -  Mild or WIld :P 
		# extent_angle shall be maximum that the jaw should shift
				
		jaw(5)
		time.sleep(1)
		jaw(self.extent_angle)
		time.sleep(1)

#---------------------------------------------------------------------------------------

#---------------------------- EXPRESSIONS FOR THE COMPLETE ROBOT -----------------------

	# -------------HAPPINESS -----------------
	# Facial characters showing happiness
	# Wide lips
	# Slightly parted lips with a gap
	# Eyes in the center

	# For the upper and lower lips -  since their motion will be either ways, i.e. bidirectional, the neutral position angle is kept 90
	# So to diverge the lips -  Angle is increased and to converge - angle is decreased
	
	# Extent of happiness - 1 to 3 - 3 discrete settings with corresponding angles being 10, 20 and 30 -  Subject to Change
	# Jaw is kept at 0 degrees when the lips are sticking together - This prevents the jaw from undesired opposite movement that pushes it 
	# inside the face beyond the joint  lips
	# For 1 to 3 discrete settings - The setting of the jaw shall be the same - 1:2:3::10:20:30


	def happy(self, extent_happy):

		if self.extent_happy == 1:
			ang = 10
		elif self.extent_happy == 2:
			ang = 20
		if self.extent_happy == 3:
			ang = 30			

		upperlips(90 + ang)
		lowerlips(90 + ang)
		jaw(ang)
		eyes(90) 
	# -----------------------------------------------

	#------------------- SAD ------------------------
	# Facial characters while being sad
	# Lips together
	# Eyes at the center
	# Face facing front and head drooped down 
	# Jaws keeping the lips together

	# No extent of being sad -  Only one extreme condition

	def sad(self):

		upperlips(90)
		lowerlips(90)
		jaw(0)
		eyes(90)
		neckupdown(90 - 20 ) # The head is vertical in the centre at 90 degrees. Going up increases the angle and going down decreases

	# --------------------------------------------------

	# --------------------- LAUGHTER --------------- 
	# Facial characters while laughing 
	# Lips apart at extremes
	# Eyes in the center
	# Face slightly facing upwards
	# Jaw moving to and fro 

	# Let's keep the extreme angle of the lips to be at servo angle of 120 - STC(Subject to Change)

	def laugh(self, extent_laugh):

		if self.extent_laugh == 1:
			ang = 10
		elif self.extent_laugh == 2:
			ang = 20
		elif self.extent_laugh == 3:
			ang = 30

		upperlips(90 + ang)
		lowerlips(90 + ang)
		eyes(90)
		jaws_to_fro(ang)

	#--------------------------------------------------

	#---------------------------- WOW/AMAZEMENT ---------------
	# Facial Characters while laughing 
	# Lips slightly apart ~ 10 degrees or so
	# Eyes in the center and trying to pop out
	# Jaw open and at the extremes

	def wow(self):
		
		upperlips(90 + 10)
		lowerlips(90 + 10)
		eyes(90) # Trying to bring it out as well - Another mechanism needed
		jaw(0 + 30) # Maximum 30 degrees

	#----------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------







