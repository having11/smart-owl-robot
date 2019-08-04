import RPi.GPIO as GPIO
import time

class Stepper():
    def __init__(self, pins, seq, rpm=60):
        self.seq = seq
        self.pins = pins
        GPIO.setmode(GPIO.BCM)
        self.delay = 1 / rpm * 200 / 60
        self.setup_pins()
        self.stop()

    def setup_pins(self):
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
    
    def setStep(self, values):
        for index, pin in enumerate(self.pins):
            GPIO.output(pin, values[index])

    def forward(self, steps):
        for step in range(steps):
            for step_val in self.seq:
                self.setStep(step_val)
                time.sleep(self.delay)
    
    def backward(self, steps):
        for step in range(steps):
            for step_val in reversed(self.seq):
                self.setStep(step_val)
                time.sleep(self.delay)

    def stop(self):
        self.setStep([0,0,0,0])