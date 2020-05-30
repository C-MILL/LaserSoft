import sys
from pathlib import Path

import numpy as np
from PyQt5 import uic, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication
from functools import partial
from widgetHelperPackage import DefaultWidget
from widgets.HelpPopUp import HelpPopUp
from widgets.Keyboard import Keyboard

class ChooseMaterial(DefaultWidget):
    def __init__(self,stack,widgetDict,laser,world):
        DefaultWidget.__init__(self,stack,widgetDict,laser,world)
        self.path = 'UI/UIFiles/chooseMaterial.ui'
        self.id = 'chooseMaterial'
        self.homeBtnExists=True
        self.loadUi()
        self.addBtn(self.goBtn, self.go)
        self.addBtn(self.paperBtn,self.paper)
        self.addBtn(self.cardboardBtn, self.cardboard)
        self.addBtn(self.plywoodBtn, self.plywood)
        self.addBtn(self.woodBtn, self.wood)
        self.addBtn(self.aluBtn, self.alu)
        self.addBtn(self.metalBtn, self.metal)
        self.material='1'
        self.addBtn(self.backBtn, self.backWidget)
        self.addBtn(self.helpBtn, self.setHelpWidget)
    def backWidget(self):
        """set's Widget one step back."""
        self.setWidget('placing')

    def setHelpWidget(self):
        """Btn function to set help Widget"""
        self.help = HelpPopUp()
        self.help.showHelp(str(Path(__file__).parents[1]) + '/images/help/helpChooseMaterial.png')

    def setDict(self,dict):
        self.dict=dict

    def go(self):
        self.setWidget('wait')
        QtCore.QTimer.singleShot(100, self.process)

    def process(self):
        self.working = self.widgetDict['working']
        self.working.setUp(self.dict, 'engraving', self.material, inSteps=True)
        self.working.start()

    def paper(self):
        self.deactivateBtns('paper')
        self.material='Paper'
    def cardboard(self):
        self.deactivateBtns('cardboard')
        self.material = 'Cardboard'
    def plywood(self):
        self.deactivateBtns('plywood')
        self.material = 'Plywood/Leather'
    def wood(self):
        self.deactivateBtns('wood')
        self.material = 'Wood'
    def alu(self):
        self.deactivateBtns('alu')
        self.material = 'Aluminium'
    def metal(self):
        self.deactivateBtns('metal')
        self.material = 'Metal'

    def deactivateBtns(self,m):
        if m!='paper':
            self.paperBtn.setChecked(False)
        if m != 'cardboard':
            self.cardboardBtn.setChecked(False)
        if m != 'plywood':
            self.plywoodBtn.setChecked(False)
        if m != 'wood':
            self.woodBtn.setChecked(False)
        if m != 'alu':
            self.aluBtn.setChecked(False)
        if m != 'metal':
            self.metalBtn.setChecked(False)

