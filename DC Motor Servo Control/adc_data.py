import RPi.GPIO as RPi
import Adafruit_ADS1x15
import time

adc_ob = Adafruit_ADS1x15.ADS1115()
ga = 1
adc = [0]*4
hgt
while(1):
	for i in range(4):
		adc[i] = adc_ob.read_adc(i, gain = ga)
		print adc[i] 
		time.sleep(0.2)	
	
