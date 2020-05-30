from pathlib import Path

from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from widgetHelperPackage import *
from widgets.HelpPopUp import HelpPopUp


class ManualMode(DefaultWidget):
    def __init__(self,stack,widgetDict,laser,world):
        DefaultWidget.__init__(self,stack,widgetDict,laser,world)
        self.path = 'UI/UIFiles/manMode.ui'
        self.id = 'manMode'
        self.homeBtnExists = True
        self.setX = False
        self.setY = False
        self.autOn=False
        self.xNum = 0
        self.yNum = 0
        self.laserPowerNum = 0
        self.loadUi()
        self.laser=laser
        self.addAllBtn()
        self.setUpKeyboardBtn()
        self.restObj=None
        self.addBtn(self.backBtn, self.backWidget)
        self.addBtn(self.helpBtn, self.setHelpWidget)

    def backWidget(self):
        """set's Widget one step back."""
        self.setWidget('settings')

    def setHelpWidget(self):
        """Btn function to set help Widget"""
        self.help = HelpPopUp()
        self.help.showHelp(str(Path(__file__).parents[1]) + '/images/help/helpManual.png')

    def go(self):
        self.working = self.widgetDict['working']
        coordDict={'x':[self.xNum],'y':[self.yNum],'laser':[self.autOn]}
        self.working.setUp(coordDict,'manual','1',inSteps=False)
        self.setWidget('working')
        self.working.start()

    def addAllBtn(self):
        self.addBtn(self.backBtn, self.backWidget)
        self.addBtn(self.helpBtn, self.setHelpPopUp)
        self.addBtn(self.setXBtn, self.xBtnSet)
        self.addBtn(self.setYBtn, self.yBtnSet)
        self.addBtn(self.autoOnBtn, self.laserAuto)
        self.addBtn(self.goBtn, self.go)

    def laserAuto(self):
        self.laser.turnOffLaser()
        if self.autoOnBtn.isChecked():
            self.autOn=True
        else:
            self.autOn=False

    def laserOn(self):
        self.autoOnBtn.setChecked(False)
        if self.laserManOnBtn.isChecked():
            self.laser.turnOnLaser()
        else:
            self.laser.turnOffLaser()

    def backWidget(self):
        """set's WIdget one step back."""
        self.setWidget('settings')

    def setHelpPopUp(self):
        """help function does not exist yet"""
        pass

    def yBtnSet(self):
        self.setBtnsFalse('y')
        if self.setYBtn.isChecked():
            self.setY = True
        else:
            self.setY = False

    def xBtnSet(self):
        self.setBtnsFalse('x')
        if self.setXBtn.isChecked():
            self.setX = True
        else:
            self.setX = False

    def setBtnsFalse(self, exception):
        if exception != 'y':
            self.setYBtn.setChecked(False)
            self.setY = False
        if exception != 'x':
            self.setX = False
            self.setXBtn.setChecked(False)

    def setUpLcd(self):
        """set LCD number"""
        self.xValue.display(self.xNum)
        self.yValue.display(self.yNum)


    def delEnd(self):
        if self.setX:
            self.xNum = self.delEndHelper(self.xNum)
        if self.setY:
            self.yNum = self.delEndHelper(self.yNum)
        self.setUpLcd()

    def delEndHelper(self, num):
        if num > 9 or num < -9:
            return int(str(num)[0:-1])
        else:
            return 0

    def clear(self):
        self.xNum = 0
        self.yNum = 0
        self.setUpLcd()

    def changeSign(self):
        if self.setX:
            self.xNum -= 2 * self.xNum
        if self.setY:
            self.yNum -= 2 * self.yNum
        self.setUpLcd()

    def number(self, num):
        if self.setX and self.xNum < 10000000:
            self.xNum = int(str(self.xNum) + str(num))
        if self.setY and self.yNum < 10000000:
            self.yNum = int(str(self.yNum) + str(num))
        self.setUpLcd()

    """Keyboard related functions"""

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

    def setUpKeyboardBtn(self):
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
        self.addBtn(self.clearBtn, self.clear)
