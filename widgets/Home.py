import sys
from pathlib import Path

from PyQt5.QtWidgets import QApplication

from widgetHelperPackage import DefaultWidget
from widgets.HelpPopUp import HelpPopUp

class Home(DefaultWidget):
    def __init__(self,stack,widgetDict,laser,world):
        DefaultWidget.__init__(self,stack,widgetDict,laser,world)
        self.path = 'UI/UIFiles/home.ui'
        self.id = 'home'
        self.homeBtnExists=False
        self.loadUi()
        self.addBtn(self.startBtn, self.setStartWidget)
        self.addBtn(self.helpBtn,self.setHelpWidget)
        self.addBtn(self.settingsBtn, self.setSettingsWidget)
        self.addBtn(self.closeBtn, QApplication.quit)



    def setStartWidget(self):
        """Btn function to set Engrave Widget"""
        self.setWidget('start')

    def setSettingsWidget(self):
        """Btn function to set settings Widget"""
        self.setWidget('settings')

    def setHelpWidget(self):
        """Btn function to set help Widget"""
        self.help = HelpPopUp()
        self.help.showHelp(str(Path(__file__).parents[1]) + '/images/help/helpMain.png')




