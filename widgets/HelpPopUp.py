import platform

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit
from PyQt5 import uic, QtGui, QtCore
import sys
import os
from pathlib import Path

from widgetHelperPackage import DefaultWidget


class HelpPopUp(QMainWindow):
    def __init__(self):
        super(HelpPopUp, self).__init__()
        uic.loadUi(str(Path(__file__).parents[1]) + "/UI/UIFiles/helpPopUp.ui", self)
        self.okBtn.clicked.connect(self.closeWindow)
    def showHelp(self,imgPath):
        self.label.setPixmap(QtGui.QPixmap(imgPath).scaled(self.label.size(), QtCore.Qt.KeepAspectRatio))
        if platform.machine() != 'x86_64':
            self.showFullScreen()
        else:
            self.show()
    def closeWindow(self):
        self.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelpPopUp()
    window.showHelp(str(Path(__file__).parents[1]) +'/images/help/helpMain.png')
    app.exec_()