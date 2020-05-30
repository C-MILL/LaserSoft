import platform
import sys

from PyQt5.QtWidgets import QApplication

from widgetHelperPackage import *
from work import *
from checkStates import *

class MainWidget(object):
    """"""
    def __init__(self):
        laser = LaserMain()
        world = World()
        self.widgetManager = WidgetManager(laser,world)
        widgetDic=self.widgetManager.getAllWidgets()
        widgetStack=self.widgetManager.addWidgetsToStack(widgetDic)
        configObject = widgetDic['config']
        config=configObject.getConfig()
        widgetDic['working'].setConfig(config)
        widgetDic['editing'].setConfig(config)
        widgetDic['settings'].setConfig(config)
        #world.setUpCoordinates(config)
        CheckStatesThread(laser, widgetDic,configObject)
        widgetStack.setCurrentWidget(widgetDic['home'])


    def startApplication(self):
        """starts App"""
        #self.widgetManager.showMaximized()
        if platform.machine() != 'x86_64':
            self.widgetManager.showFullScreen()
        else:
            self.widgetManager.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainApplication=MainWidget()
    mainApplication.startApplication()
    app.exec_()
    sys.exit()
