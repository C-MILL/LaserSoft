from pathlib import Path

from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from widgetHelperPackage import *
from widgets.HelpPopUp import HelpPopUp
from widgets.Keyboard import Keyboard
from work.Cal import cal


class Settings(DefaultWidget):

    def __init__(self,stack,widgetDict,laser,world):
        DefaultWidget.__init__(self,stack,widgetDict,laser,world)
        self.path = 'UI/UIFiles/settings.ui'
        self.id = 'settings'
        self.homeBtnExists=True
        self.loadUi()
        self.addBtn(self.manBtn, self.setManWidget)
        self.addBtn(self.aboutBtn, self.setAboutWidget)
        self.addBtn(self.calBtn, self.setCalWidget)
        self.addBtn(self.parBtn, self.setConfigWidget)
        self.addBtn(self.helpBtn, self.setHelpWidget)
    def setManWidget(self):
        self.setWidget('manMode')

    def setHelpWidget(self):
        """Btn function to set help Widget"""
        self.help = HelpPopUp()
        self.help.showHelp(str(Path(__file__).parents[1]) + '/images/help/helpSettings.png')

    def setAboutWidget(self):
        self.help = HelpPopUp()
        self.help.showHelp(str(Path(__file__).parents[1]) + '/images/help/about.png')


    def setCalWidget(self):
            cal(self, self.world, self.config, False)

    def setConfigWidget(self):
        self.setWidget('config')



    def showValue(self):
        self.key.close()
