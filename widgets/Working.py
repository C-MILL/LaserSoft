import copy
from functools import partial
from pathlib import Path

from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from widgetHelperPackage import *
from platform import system
from work import *



class Working(DefaultWidget):

    def __init__(self, stack, widgetDict, laser, world):
        DefaultWidget.__init__(self, stack, widgetDict, laser, world)
        self.path = 'UI/UIFiles/working.ui'
        self.id = 'working'
        self.homeBtnExists = False
        self.loadUi()
        self.addBtn(self.finishedBtn,self.finished)
        self.addBtn(self.cancelBtn,self.cancel)
        self.finishedBtn.setEnabled(False)


    def start(self):
        self.finishedBtn.setEnabled(False)
        self.work = Work()
        self.work.setStop(False)
        self.work.updatePage.connect(self.updatePage)
        self.work.setUp(laser=self.laser, laserPower=self.laserPower, workingSpeed=self.workingSpeed, coordDict=self.coordDict, config=self.config, world=self.world,mmToSteps=self.mmToSteps,movingSpeed=self.movingSpeed,inSteps=self.inSteps,firingDiameter=self.laserFiringDiameter)
        self.setWidget('working')
        self.work.startOperation()


    def setUp(self, coordDict, mode,material,inSteps):

        self.inSteps=inSteps
        self.workingConfig = self.config[mode][material]
        self.coordDict = coordDict
        self.laserPower = self.workingConfig['laserPower']
        self.workingSpeed = self.workingConfig['workingSpeed']
        self.nrOfPasses=self.workingConfig['nrOfPasses']
        self.mmToSteps=self.config['general']['mmToSteps']
        self.movingSpeed=self.config['general']['movingSpeed']
        self.laserFiringDiameter = self.config['general']['laserFiringDiameter']

    def updatePage(self):
        self.progressBar.setValue(self.work.getPercent())
        picturePath = str(Path(__file__).parents[1]) + "/images/plot.jpg"
        self.label.setPixmap(QtGui.QPixmap(picturePath))
        if self.work.getPercent()==100:
            self.finishedBtn.setEnabled(True)

    def cancel(self):
        self.setWidget('wait')
        self.work.setStop(True)
        QtCore.QTimer.singleShot(100, self.process)

    def process(self):
        self.laser.turnOffLaser()
        self.setWidget('home')

    def finished(self):
        self.work.terminate()
        self.laser.turnOffLaser()
        self.setWidget('home')