import platform

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit
from PyQt5 import uic
import sys
import os
from pathlib import Path


class Keyboard(QMainWindow):
    returnNumber = pyqtSignal()
    def __init__(self):
        super(Keyboard, self).__init__()
        uic.loadUi(str(Path(__file__).parents[1]) + "/UI/UIFiles/keyBoardPopUp.ui", self)
        self.setUpKeyboardBtn()
        self.typed = ''
        self.decimals=False
        self.done = False
        self.final=''
        self.neg=False


    def getTyped(self):
        try:
            if self.neg and self.final[0]!='-':
                self.final = '-' + self.final
            return float(self.final)
        except:
            return(0)

    def showKeyboard(self):
        if platform.machine() != 'x86_64':
            self.showFullScreen()
        else:
            self.show()

    def one(self):
        self.number(1)

    def two(self):
        self.number(2)

    def three(self):
        self.number(3)

    def four(self):
        self.number(4)

    def five(self):
        self.number(5)

    def six(self):
        self.number(6)

    def seven(self):
        self.number(7)

    def eight(self):
        self.number(8)

    def nine(self):
        self.number(9)

    def zero(self):
        self.number(0)

    def number(self, add):
        if len(self.typed) < 10000000:
            self.typed = str(self.typed) + str(add)
            self.final=self.typed
        if self.decimals:
            full=str(self.typed)[0:self.dotPlace]
            dec=str(self.typed)[self.dotPlace:]
            self.final=full+'.'+dec
        self.updateLabel(self.final)

    def updateLabel(self, typed):
        if self.neg:
            typed='-'+typed
        self.label.setText(str(typed))

    def setUpKeyboardBtn(self):
        self.addBtn(self.dotBtn,self.dot)
        self.addBtn(self.oneBtn, self.one)
        self.addBtn(self.twoBtn, self.two)
        self.addBtn(self.threeBtn, self.three)
        self.addBtn(self.fourBtn, self.four)
        self.addBtn(self.fiveBtn, self.five)
        self.addBtn(self.sixBtn, self.six)
        self.addBtn(self.sevenBtn, self.seven)
        self.addBtn(self.eightBtn, self.eight)
        self.addBtn(self.nineBtn, self.nine)
        self.addBtn(self.zeroBtn, self.zero)
        self.addBtn(self.delBtn, self.delEnd)
        self.addBtn(self.signBtn, self.changeSign)
        self.okBtn.clicked.connect(self.returnNumber.emit)

    def dot(self):
        self.decimals=True
        if len(self.typed)==0:
            self.dotPlace=0
        else:
            self.dotPlace=int(len(self.typed))

    def addBtn(self, btn, function):
        """helper function to import PyQt buttons from the UI file"""
        btn.clicked.connect(function)

    def delEnd(self):
        self.typed = self.delEndHelper(self.typed)
        if self.decimals==False:
                self.decimals=False
                self.final=self.typed
        else:
            if self.dotPlace >= len(self.typed):
                self.decimals = False
                self.final = self.typed
            else:
                full = str(self.typed)[0:self.dotPlace]
                dec = str(self.typed)[self.dotPlace:]
                self.final = full + '.' + dec
        self.updateLabel(self.final)

    def delEndHelper(self, num):
        return str(num)[0:-1]


    def changeSign(self):
        if self.neg:
            self.neg=False
            self.updateLabel(self.final)
        else:
            self.neg=True
            self.updateLabel(self.final)

    def getDone(self):
        return self.done





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Keyboard()
    window.showKeyboard()
    app.exec_()
