"""
Find the Direction od Arrival of the audio and control servo motor
Author: Ben McEwen
Date: 18/03/2021
Last update: 19/03/2021
TODO: connect servo
"""

from tuning import Tuning
import usb.core
import usb.util
import time
from gpiozero import Servo
from scipy.interpolate import interp1d
 
dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)

servo = Servo(17)
servo_angle = 0
 
if dev:
    Mic_tuning = Tuning(dev)
    print(Mic_tuning.direction)
    while True:
        try:
            print(Mic_tuning.direction)
	    if Mic_tuning.direction >= 180:
	        servo_angle = 1
            else:
		m = interp1d([0,360],[-1,1])
                servo_angle = m(Mic_tuning.direction)
            servo.value = servo_angle
            time.sleep(1)
        except KeyboardInterrupt:
            break
