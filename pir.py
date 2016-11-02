from gpiozero import MotionSensor
from subprocess import call
from time import sleep

# Time to wait until display should turn off after last motion detected
timeUntilDisplayOff = 1800
# The GPIO data pin to which the PIR sensor is connected
pin = 14

pir = MotionSensor(pin)
timer = timeUntilDisplayOff

while True:

	if pir.motion_detected:
		timer = timeUntilDisplayOff
		print ("Motion detected! Setting timer to " + str(timer) + " seconds.")
		
	if timer > 0:
		if timer % 10 == 0:
			print ("Timer: " + str(timer) + " seconds")
		timer -= 1

	elif timer == 0:
		call(['vcgencmd', 'display_power', '0'])

		print ("Timer is 0. Display turned off. Waiting for motion...")
		# display is now off. we wait for motion and turn it on
		pir.wait_for_motion()
		call(['vcgencmd', 'display_power', '1'])
		timer = timeUntilDisplayOff
	
	sleep(1)