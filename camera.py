from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import io
from PIL import Image
import numpy as np

class CameraSystem():

    def __init__(self):
        self.camera = PiCamera()
        self.camera.rotation = 180
        self.camera.resolution = (128, 128)
        #self.rawCapture = PiRGBArray(self.camera, size=(128,128))
        self.cam = cv2.VideoCapture(0)
        time.sleep(0.1)
        self.face_cascade = cv2.CascadeClassifier('/home/pi/Documents/Code/haarcascade_frontalface_default.xml')
        self.stream = io.BytesIO()
    def get_capture(self):
        """self.camera.capture(self.rawCapture, format="bgr")
        image = self.rawCapture.array"""
        with PiRGBArray(self.camera) as stream:
            self.camera.capture(stream, format='bgr')
            img = stream.array

        #self.camera.close()
        
        print("Captured image")
        return img #return opencv-format image
    
    def get_capture_pillow(self):
        self.stream.close()
        self.stream = io.BytesIO()
        self.camera.capture(self.stream, format='jpeg', resize=(128,128))
        #self.camera.close()
        self.stream.seek(0)
        img = Image.open(self.stream)
        #self.stream = io.BytesIO()
        
        return img

    def detectFace(self):
        gray = cv2.cvtColor(self.get_capture(), cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        print(faces)

        return faces