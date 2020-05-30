import platform
from threading import Thread

import time
from work import *

class CheckStatesThread(Thread):
    def __init__(self,laser,widgetDic,config):
        Thread.__init__(self)
        self.laser=laser
        self.config=config
        self.closedSensor=True
        self.referenceDone=True
        self.xyzSensor=True
        self.widgetDic=widgetDic
        self.stateOfLaserBefore=None
        self.stateOfConfigBefore=None
        self.daemon = True
        self.masterState=False
        self.masterStateBefore=None
        self.start()

    def run(self):
        threadRuntime=0
        while True:
            laserState=self.stateOfLaser()
            configState=self.stateOfConfig()
            if configState:
                self.masterState=True
            else:
                self.masterState=False
            self.stateOfAll()
            if platform.machine() != 'x86_64':
                time.sleep(5)
            else:
                time.sleep(0.2)
            threadRuntime+=1

    def stateOfAll(self):
        state=self.masterState
        if state != self.masterStateBefore:
            for formkey in self.widgetDic:
                widget = self.widgetDic[formkey]
                if formkey != 'wait':
                    widget.setLight(widget.pageTitle, state)
            self.masterStateBefore = state

    def stateOfLaser(self):
        state=self.laser.getLaserState()
        if state!=self.stateOfLaserBefore:
            for formkey in self.widgetDic:
                widget = self.widgetDic[formkey]
                if formkey != 'wait':
                    widget.setLight(widget.laserLight,state)
            self.stateOfLaserBefore=state
        return state

    def stateOfConfig(self):
        state=self.config.getConfigState()
        if state != self.stateOfConfigBefore:
            for formkey in self.widgetDic:
                widget = self.widgetDic[formkey]
                if formkey!='wait':
                    widget.setLight(widget.configLight, state)
            self.stateOfConfigBefore = state
        return state