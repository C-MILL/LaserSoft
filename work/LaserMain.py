
import platform
import time
if platform.machine()!='x86_64':
    import RPi.GPIO as GPIO


class LaserMain(object):

    def __init__(self):
        self.laserState = True
        if platform.machine() != 'x86_64':
            servoPIN = 13
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(servoPIN, GPIO.OUT)
            self.p = GPIO.PWM(servoPIN, 50)  # GPIO 17 als PWM mit 50Hz
            self.p.start(0)  # Initialisierung
        self.turnOffLaser()
    def turnOffLaser(self):
        if platform.machine()!='x86_64':
            self.p.ChangeDutyCycle(0)
        self.laserState=True

    def turnOnLaser(self,laserPower):
        if platform.machine()!='x86_64':
            self.p.ChangeDutyCycle(laserPower)
        self.laserState=False

    def getLaserState(self):
        return self.laserState







