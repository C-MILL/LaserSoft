import time
from pathlib import Path
from threading import Thread
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal
from work import World

import platform

if platform.machine()!='x86_64':
    import RPi.GPIO as GPIO


def cal(self,world, config, forPic):
    self.world=world
    if platform.machine() != 'x86_64':
            GPIO.setmode(GPIO.BOARD)
            dirPinX = 12
            pulPinX = 11
            dirPinY = 16
            pulPinY = 15
            endX = 18
            endY = 22
            GPIO.setup(pulPinX, GPIO.OUT)
            GPIO.setup(dirPinX, GPIO.OUT)
            GPIO.setup(pulPinY, GPIO.OUT)
            GPIO.setup(dirPinY, GPIO.OUT)
            GPIO.setup(endX, GPIO.IN)
            GPIO.setup(endY, GPIO.IN)
            speed = config['general']['movingSpeed']
            while GPIO.input(endY) == 0 or GPIO.input(endX)==0:
                if GPIO.input(endY)==0:
                    GPIO.output(dirPinY, 1)
                    GPIO.output(pulPinY, 1)
                if GPIO.input(endX)==0:
                    GPIO.output(dirPinX, 1)
                    GPIO.output(pulPinX, 1)
                time.sleep(speed)
                GPIO.output(dirPinX, 0)
                GPIO.output(pulPinX, 0)
                GPIO.output(dirPinY, 0)
                GPIO.output(pulPinY, 0)
                time.sleep(speed)
    world.updateCurrent(config['general']['startPosX'],config['general']['startPosY'])
    '..................................................'
    if forPic==True:
        self.working = self.widgetDict['working']
        coordDict={'x':[0],'y':[100],'laser':[False]}
        self.working.setUp(coordDict,'manual','1',inSteps=False)
        self.working.start()