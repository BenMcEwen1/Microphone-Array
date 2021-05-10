from pixel_ring import pixel_ring
 
def listen():
    pixel_ring.listen()

def spin():
    pixel_ring.spin()

def off():
    # Change brightness of LEDs (0x00: OFF)
    pixel_ring.set_brightness(0x00)
    spin()

def on():
    # Change brightness of LEDs (0x20: ON)
    pixel_ring.set_brightness(0x1F)
    listen()