import math
import time

from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1351



from PIL import Image, ImageFont, ImageDraw
import cv2

class Screen():
    def __init__(self, rst, dc):
        self.RST = rst
        self.DC = dc
        self.SPI_PORT = 0
        self.SPI_DEVICE = 0
        serial = spi(port=self.SPI_PORT, device=self.SPI_DEVICE)
        self.disp = ssd1351(serial, width=128, height=128, rotate=0)
        self.disp.show()
        self.width = 128
        self.height = 128
        self.disp.clear()

    def blank(self):
        self.disp.clear()
        self.disp.display()
    
    def show_img(self, img_path):
        im = Image.open(img_path)
        im.resize((128,128), Image.ANTIALIAS)
        self.disp.display(im)
        self.disp.show()

    def showFromCamera(self, photo):
        img = photo.convert('RGB')
        self.disp.display(img)
        print("Showing image")
        #self.disp.show()