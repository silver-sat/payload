from picamera import PiCamera
from time import sleep
import os, sys, os.path

camera = PiCamera()

# Remove the old image so we don't get confused
os.unlink('/home/pi/Desktop/image.jpg')

camera.resolution = 'VGA'
camera.start_preview()
sleep(2)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
