import copy
from functools import partial
from pathlib import Path

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QTimer, QByteArray
from PyQt5.QtGui import QPixmap, QMovie
from widgetHelperPackage import *
from platform import system
from work import *



class Wait(DefaultWidget):

    def __init__(self, stack, widgetDict, laser, world):
        DefaultWidget.__init__(self, stack, widgetDict, laser, world)
        self.path = 'UI/UIFiles/wait.ui'
        self.id = 'wait'
        self.homeBtnExists = False
        self.loadUi()

        self.gif = QMovie('UI/Icons/loading.gif', QByteArray(), self)
        self.gif.setCacheMode(QMovie.CacheAll)
        self.gif.setSpeed(100)
        self.loadingLabel.setMovie(self.gif)
        self.gif.start()