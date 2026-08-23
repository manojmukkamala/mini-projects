import picamera
import time

camera = picamera.PiCamera()
#camera.capture('example.jpg')
camera.start_recording('example.h264')
time.sleep(10)
camera.stop_recording()

