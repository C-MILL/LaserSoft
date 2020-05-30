import ast
import pickle
from functools import partial

from widgetHelperPackage import *
from widgets.HelpPopUp import HelpPopUp
from widgets.Keyboard import Keyboard
from pathlib import Path


class Configuration(DefaultWidget):

    def __init__(self, stack, widgetDict, laser, world):
        DefaultWidget.__init__(self, stack, widgetDict, laser, world)
        self.path = 'UI/UIFiles/configuration.ui'
        self.id = 'config'
        self.homeBtnExists = True
        self.loadUi()
        self.read()
        self.configState = True
        self.doAllTests()
        self.engravingComboBox.activated.connect(self.setEngravingButtonNames)
        self.addBtn(self.backBtn, self.backWidget)
        self.addBtn(self.helpBtn, self.setHelpWidget)

    def backWidget(self):
        """set's Widget one step back."""
        self.setWidget('settings')

    def setHelpWidget(self):
        """Btn function to set help Widget"""
        self.help = HelpPopUp()
        self.help.showHelp(str(Path(__file__).parents[1]) + '/images/help/helpConfiguration.png')




    def setEngravingButtonNames(self):
        try:
            self.engravingWorkingSpeedBtn.setText(str(self.config['engraving'][str(self.engravingComboBox.currentText())]['workingSpeed']))
        except:
            self.config['engraving'][str(self.engravingComboBox.currentText())]['workingSpeed']=0
            self.engravingWorkingSpeedBtn.setText('0')
        try:
            self.engravingLaserPowerBtn.setText(str(self.config['engraving'][str(self.engravingComboBox.currentText())]['laserPower']))
        except:
            self.config['engraving'][str(self.engravingComboBox.currentText())]['laserPower']=0
            self.engravingLaserPowerBtn.setText('0')
        try:
            self.engravingNrOfPassesBtn.setText(str(self.config['engraving'][str(self.engravingComboBox.currentText())]['nrOfPasses']))
        except:
            self.config['engraving'][str(self.engravingComboBox.currentText())]['nrOfPasses']=0
            self.engravingNrOfPassesBtn.setText('0')









    def engravingWorkingSpeed(self):
        self.config['engraving'][str(self.engravingComboBox.currentText())]['workingSpeed'] = self.key.getTyped()
        self.engravingWorkingSpeedBtn.setText(str(self.key.getTyped()))
        self.key.close()

    def engravingLaserPower(self):
        self.config['engraving'][str(self.engravingComboBox.currentText())]['laserPower'] = int(self.key.getTyped())
        self.engravingLaserPowerBtn.setText(str(int(self.key.getTyped())))
        self.key.close()

    def engravingNrOfPasses(self):
        self.config['engraving'][str(self.engravingComboBox.currentText())]['nrOfPasses'] = int(self.key.getTyped())
        self.engravingNrOfPassesBtn.setText(str(int(self.key.getTyped())))
        self.key.close()








    def doAllTests(self):
        self.addBtn(self.saveBtn, self.save)
        self.addBtn(self.cancelBtn, self.read)







        try:
            self.addBtn(self.engravingWorkingSpeedBtn, partial(self.callKeyboard, self.engravingWorkingSpeed), str(self.config['engraving'][str(self.engravingComboBox.currentText())]['workingSpeed']))
        except:
            self.configState = False
            self.addBtn(self.engravingWorkingSpeedBtn, partial(self.callKeyboard, self.engravingWorkingSpeed))
        try:
            self.addBtn(self.engravingLaserPowerBtn, partial(self.callKeyboard, self.engravingLaserPower), str(self.config['engraving'][str(self.engravingComboBox.currentText())]['laserPower']))
        except:
            self.configState = False
            self.addBtn(self.engravingLaserPowerBtn, partial(self.callKeyboard, self.engravingLaserPower))


        try:
            self.addBtn(self.manualWorkingSpeedBtn, partial(self.callKeyboard, self.manualWorkingSpeed), str(self.config['manual']['1']['workingSpeed']))
        except:
            self.configState = False
            self.addBtn(self.manualWorkingSpeedBtn, partial(self.callKeyboard, self.manualWorkingSpeed))

        try:
            self.addBtn(self.manualLaserPowerBtn, partial(self.callKeyboard, self.manualLaserPower), str(self.config['manual']['1']['laserPower']))
        except:
            self.configState = False
            self.addBtn(self.manualLaserPowerBtn, partial(self.callKeyboard, self.manualLaserPower))




        try:
            self.addBtn(self.camHeightBtn, partial(self.callKeyboard, self.camHeight), str(self.config['cam']["camHeight"]))
        except:
            self.configState = False
            self.addBtn(self.camHeightBtn, partial(self.callKeyboard, self.camHeight))
        try:
            self.addBtn(self.camWidthBtn, partial(self.callKeyboard, self.camWidth), str(self.config['cam']["camWidth"]))
        except:
            self.configState = False
            self.addBtn(self.camWidthBtn, partial(self.callKeyboard, self.camWidth))
        try:
            self.addBtn(self.camOffsetXBtn, partial(self.callKeyboard, self.camOffsetX), str(self.config['cam']["camOffsetX"]))
        except:
            self.configState = False
            self.addBtn(self.camOffsetXBtn, partial(self.callKeyboard, self.camOffsetX))
        try:
            self.addBtn(self.camOffsetYBtn, partial(self.callKeyboard, self.camOffsetY), str(self.config['cam']["camOffsetY"]))
        except:
            self.configState = False
            self.addBtn(self.camOffsetYBtn, partial(self.callKeyboard, self.camOffsetY))


        try:
            self.addBtn(self.mmToStepsBtn, partial(self.callKeyboard, self.mmToSteps), str(self.config['general']["showMmToSteps"]))
        except:
            self.configState = False
            self.addBtn(self.mmToStepsBtn, partial(self.callKeyboard, self.mmToSteps))

        try:
            self.addBtn(self.laserFiringDiameterBtn, partial(self.callKeyboard, self.laserFiringDiameter), str(self.config['general']["showLaserFiringDiameter"]))
        except:
            self.configState = False
            self.addBtn(self.laserFiringDiameterBtn, partial(self.callKeyboard, self.laserFiringDiameter))

        try:
            self.addBtn(self.movingSpeedBtn, partial(self.callKeyboard, self.movingSpeed), str(self.config['general']['movingSpeed']))
        except:
            self.configState = False
            self.addBtn(self.movingSpeedBtn, partial(self.callKeyboard, self.movingSpeed))

        try:
            self.addBtn(self.startPosXBtn, partial(self.callKeyboard, self.startPosX), str(self.config['general']['startPosX']))
        except:
            self.configState = False
            self.addBtn(self.startPosXBtn, partial(self.callKeyboard, self.startPosX))

        try:
            self.addBtn(self.startPosYBtn, partial(self.callKeyboard, self.startPosY), str(self.config['general']['startPosY']))
        except:
            self.configState = False
            self.addBtn(self.startPosYBtn, partial(self.callKeyboard, self.startPosY))

        try:
            self.addBtn(self.lengthXBtn, partial(self.callKeyboard, self.lengthX), str(self.config['general']['lengthX']))
        except:
            self.configState = False
            self.addBtn(self.lengthXBtn, partial(self.callKeyboard, self.lengthX))

        try:
            self.addBtn(self.lengthYBtn, partial(self.callKeyboard, self.lengthY), str(self.config['general']['lengthY']))
        except:
            self.configState = False
            self.addBtn(self.lengthYBtn, partial(self.callKeyboard, self.lengthY))
        try:
            self.world.setUpCoordinates(self.config)
        except:
            self.configState = False


    def manualNrOfPasses(self):
        self.config['manual']['1']['nrOfPasses'] = int(self.key.getTyped())
        self.manualNrOfPassesBtn.setText(str(int(self.key.getTyped())))
        self.key.close()

    def manualLaserPower(self):
        num = self.key.getTyped()
        if num > 100:
            num = 100
        self.config['manual']['1']['laserPower'] = int(num)
        self.manualLaserPowerBtn.setText(str(int(num)))
        self.key.close()

    def manualWorkingSpeed(self):
        self.config['manual']['1']['workingSpeed'] = self.key.getTyped()
        self.manualWorkingSpeedBtn.setText(str(self.key.getTyped()))
        self.key.close()

    def laserFiringDiameter(self):
        try:
            self.config['general']['showLaserFiringDiameter'] = self.key.getTyped()
            self.config['general']['laserFiringDiameter'] = (self.config['general']['showLaserFiringDiameter'] * self.config['general']['showMmToSteps'])
            self.config['general']['mmToSteps'] = int(self.config['general']['showMmToSteps'] / (self.config['general']['showMmToSteps'] * self.config['general']['showLaserFiringDiameter']))
            self.laserFiringDiameterBtn.setText(str(self.key.getTyped()))
            self.key.close()
        except:
            pass

    def mmToSteps(self):
        try:
            self.config['general']['showMmToSteps'] = self.key.getTyped()
            self.config['general']['laserFiringDiameter'] = (self.config['general']['showLaserFiringDiameter'] * self.config['general']['showMmToSteps'])
            self.config['general']['mmToSteps'] = int(self.config['general']['showMmToSteps'] / (self.config['general']['showMmToSteps'] * self.config['general']['showLaserFiringDiameter']))
            self.mmToStepsBtn.setText(str(self.key.getTyped()))
            self.key.close()
        except:
            pass


    def lengthX(self):
        self.config['general']['lengthX'] = int(self.key.getTyped())
        self.lengthXBtn.setText(str(int(self.key.getTyped())))
        self.key.close()

    def lengthY(self):
        self.config['general']['lengthY'] = int(self.key.getTyped())
        self.lengthYBtn.setText(str(int(self.key.getTyped())))
        self.key.close()

    def startPosY(self):
        self.config['general']['startPosY'] = int(self.key.getTyped())
        self.startPosYBtn.setText(str(int(self.key.getTyped())))
        self.key.close()

    def startPosX(self):
        self.config['general']['startPosX'] = int(self.key.getTyped())
        self.startPosXBtn.setText(str(int(self.key.getTyped())))
        self.key.close()

    def movingSpeed(self):
        self.config['general']['movingSpeed'] = self.key.getTyped()
        self.movingSpeedBtn.setText(str(self.key.getTyped()))
        self.key.close()

    {'first': {'a': 1}, 'second': {'b': 2}}

    def camHeight(self):
        try:
            self.config['cam']['camHeight'] = int(self.key.getTyped())
            self.camHeightBtn.setText(str(int(self.key.getTyped())))
            self.key.close()
        except:
            self.config.update({'cam':  {'camHeight':int(self.key.getTyped())}})
            self.camHeightBtn.setText(str(int(self.key.getTyped())))
            self.key.close()
    def camWidth(self):
        try:
            self.config['cam']['camWidth'] = int(self.key.getTyped())
            self.camWidthBtn.setText(str(int(self.key.getTyped())))
            self.key.close()
        except:
            self.config.update({'cam':  {'camWidth':int(self.key.getTyped())}})
            self.camWidthBtn.setText(str(int(self.key.getTyped())))
            self.key.close()
    def camOffsetX(self):
        try:
            self.config['cam']['camOffsetX'] = int(self.key.getTyped())
            self.camOffsetXBtn.setText(str(int(self.key.getTyped())))
            self.key.close()
        except:
            self.config.update({'cam':  {'camOffsetX':int(self.key.getTyped())}})
            self.camOffsetXBtn.setText(str(int(self.key.getTyped())))
            self.key.close()
    def camOffsetY(self):
        try:
            self.config['cam']['camOffsetY'] = int(self.key.getTyped())
            self.camOffsetYBtn.setText(str(int(self.key.getTyped())))
            self.key.close()
        except:
            self.config.update({'cam':  {'camOffsetY':int(self.key.getTyped())}})
            self.camOffsetYBtn.setText(str(int(self.key.getTyped())))
            self.key.close()



    def callKeyboard(self, nextPhase):
        self.key = Keyboard()
        self.key.showKeyboard()
        self.key.returnNumber.connect(nextPhase)

    def save(self):
        pickle_out = open(str(Path(__file__).parents[1]) + "/data/config.pickle", "wb")
        pickle.dump(self.config, pickle_out)
        pickle_out.close()
        self.configState = True
        self.doAllTests()
        if self.configState == True:
            self.world.setUpCoordinates(self.config)
            self.world.printObjectName()

    def getConfigState(self):
        return self.configState

    def getConfig(self):
        return self.config

    def read(self):
        try:
            pickle_in = open(str(Path(__file__).parents[1]) + "/data/config.pickle", "rb")
            self.config = pickle.load(pickle_in)
            self.config = self.config
        except:
            pass
