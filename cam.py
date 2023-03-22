import camera
from machine import Pin
from time import sleep

class Cam:
    
    def flash_on():
        led.on()
        
    def flash_off():
        led.off()
    
    def snap():
        buf = camera.capture()
        return buf
    
    def start():
        global led
        led = Pin(4, Pin.OUT)
        state = camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)
        print("Camera State: ", state)
        camera.framesize(camera.FRAME_VGA)