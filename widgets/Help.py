from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from widgetHelperPackage import *


class Help(DefaultWidget):

    def __init__(self,stack,widgetDict,laser,world):
        DefaultWidget.__init__(self,stack,widgetDict,laser,world)
        self.path = 'UI/UIFiles/helpWidget.ui'
        self.id = 'help'
        self.homeBtnExists=True
        self.loadUi()

