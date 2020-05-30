import time
from pathlib import Path
from threading import Thread
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal
import platform

if platform.machine()!='x86_64':
    import RPi.GPIO as GPIO



def stepper(step, speed, firingDiameter):
    init = False
    if platform.machine()!='x86_64':
        if init == False:
            GPIO.cleanup
            GPIO.setmode(GPIO.BOARD)
            dirPinX = 16
            pulPinX = 15
            dirPinY = 12
            pulPinY = 11
            GPIO.setup(pulPinX, GPIO.OUT)
            GPIO.setup(dirPinX, GPIO.OUT)
            GPIO.setup(pulPinY, GPIO.OUT)
            GPIO.setup(dirPinY, GPIO.OUT)
        if step[0] > 0 and step[1] > 0:
            for i in range(round(firingDiameter)):
                GPIO.output(pulPinX, 1)
                GPIO.output(pulPinY, 1)
                time.sleep(speed)
                GPIO.output(pulPinX, 0)
                GPIO.output(pulPinY, 0)
                time.sleep(speed)
        if step[0] > 0 and step[1] < 0:
            for i in range(round(firingDiameter)):
                GPIO.output(pulPinX, 1)
                GPIO.output(dirPinY, 1)
                GPIO.output(pulPinY, 1)
                time.sleep(speed)
                GPIO.output(pulPinX, 0)
                GPIO.output(dirPinY, 0)
                GPIO.output(pulPinY, 0)
                time.sleep(speed)
        if step[0] < 0 and step[1] > 0:
            for i in range(round(firingDiameter)):
                GPIO.output(dirPinX, 1)
                GPIO.output(pulPinX, 1)
                GPIO.output(pulPinY, 1)
                time.sleep(speed)
                GPIO.output(dirPinX, 0)
                GPIO.output(pulPinX, 0)
                GPIO.output(pulPinY, 0)
                time.sleep(speed)
        if step[0] < 0 and step[1] < 0:
            for i in range(round(firingDiameter)):
                GPIO.output(dirPinY, 1)
                GPIO.output(pulPinY, 1)
                GPIO.output(dirPinX, 1)
                GPIO.output(pulPinX, 1)
                time.sleep(speed)
                GPIO.output(dirPinY, 0)
                GPIO.output(pulPinY, 0)
                GPIO.output(dirPinX, 0)
                GPIO.output(pulPinX, 0)
                time.sleep(speed)
        if step[0] > 0 and step[1] == 0:
            for i in range(round(firingDiameter)):
                GPIO.output(pulPinX, 1)
                time.sleep(speed)
                GPIO.output(pulPinX, 0)
                time.sleep(speed)
        if step[0] < 0 and step[1] == 0:
            for i in range(round(firingDiameter)):
                GPIO.output(dirPinX, 1)
                GPIO.output(pulPinX, 1)
                time.sleep(speed)
                GPIO.output(dirPinX, 0)
                GPIO.output(pulPinX, 0)
                time.sleep(speed)
        if step[0] == 0 and step[1] > 0:
            for i in range(round(firingDiameter)):
                GPIO.output(pulPinY, 1)
                time.sleep(speed)
                GPIO.output(pulPinY, 0)
                time.sleep(speed)
        if step[0] == 0 and step[1] < 0:
            for i in range(round(firingDiameter)):
                GPIO.output(dirPinY, 1)
                GPIO.output(pulPinY, 1)
                time.sleep(speed)
                GPIO.output(dirPinY, 0)
                GPIO.output(pulPinY, 0)
                time.sleep(speed)