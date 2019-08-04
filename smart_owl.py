from stepper_motor import Stepper
from screen import Screen
from camera import CameraSystem

from time import sleep
import sys
import os
import subprocess

import RPi.GPIO as GPIO

class Smart_Owl():
    def __init__(self, pin_def, step_seq):
        self.step_seq = step_seq
        self.stepper_L = Stepper(pin_def["steppers"]["L"], self.step_seq, rpm=30)
        self.stepper_R = Stepper(pin_def["steppers"]["R"], self.step_seq, rpm=30)
        self.screen = Screen(pin_def["SPI"]["RST"], pin_def["SPI"]["DC"])
        self.cam = CameraSystem()
        #os.system('pigs m 40 r')
        #os.system('pigs m 18 5')
        #subprocess.call("/home/pi/trust_and_connect.expect")
        print("Initialized")
    def displayFromCamera(self):
        self.screen.showFromCamera(self.cam.get_capture_pillow())
    def drive(self, mL, mR):
        if mL < 0:
            self.stepper_L.backward(mL)
        else:
            self.stepper_L.forward(mL)
        if mR < 0:
            self.stepper_R.backward(mR)
        else:
            self.stepper_R.forward(mR)
    def findFace(self):
        self.cam.detectFace()
    def end(self):
        GPIO.cleanup()
        sleep(10)
        sys.exit()
