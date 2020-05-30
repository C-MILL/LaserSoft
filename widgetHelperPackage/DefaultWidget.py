from PyQt5 import uic
from PyQt5.QtWidgets import QWidget



class DefaultWidget(QWidget):

    def __init__(self, stack,widgetDict,laser, world, parent=None):
        """This is a helper class that inherits the basic Widget functions and variables. stack: Stack of widgets that will get updated in this file. Also this file changes the stack index in the methid "setWidget". widgetDict: Stores all Widgets. Key is the page name and also th ID of the Widget"""
        super(DefaultWidget, self).__init__(parent)
        self.stack=stack
        self.widgetDict=widgetDict
        self.laser=laser
        self.config=None
        self.world=world


    def setLight(self, light, state):
        if state:
            light.setStyleSheet('color: black ; background-color : green')
        else:
            light.setStyleSheet('color: black ; background-color : red')

    def setConfig(self,config):
        self.config=config

    def loadUi(self):
        """uses FilePath and loads the UI file into python. If the file has a homeBtn, it gets bound to the Home Widget"""
        uic.loadUi(self.path, self)
        if self.homeBtnExists and self.id!='home':
            self.addBtn(self.homeBtn, self.setHomeWidget)


    def setHomeWidget(self):
        self.setWidget('home')

    def noButtonError(self):
        """just prints except error message from button inititialization"""
        print(self, "attribut error, Button missing  in the file you just wanted to load")

    def addBtn(self, btn, function, name=None):
        """helper function to import PyQt buttons from the UI file"""
        btn.clicked.connect(function)
        if name!=None:
            btn.setText(name)

    def setWidget(self, key):
        """inputs: key word of a Widget. loads the widget from the WIdget stack."""
        self.stack.setCurrentWidget(self.widgetDict[key])
