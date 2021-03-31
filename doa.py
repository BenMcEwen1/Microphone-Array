from tuning import Tuning
import usb.core
import usb.util
import time
 
dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)

def direction():
    # Return the direction of arrival of the sound
    if dev:
        Mic_tuning = Tuning(dev)
    return Mic_tuning.direction