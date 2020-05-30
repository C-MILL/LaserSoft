
import threading
from pathlib import Path
from PIL import Image
from PIL import ImageFile
from PyQt5 import QtGui, QtCore
import _thread

from ImageManipulation.ImageEditing import trueBlackWhite
from widgetHelperPackage import *
from widgets.HelpPopUp import HelpPopUp
from work.Cal import cal


class Editing(DefaultWidget):

    def __init__(self,stack,widgetDict,laser,world):
        DefaultWidget.__init__(self,stack,widgetDict,laser,world)
        self.path = 'UI/UIFiles/editing.ui'
        self.id = 'editing'
        self.homeBtnExists=True
        self.lock = threading.Lock()
        self.loadUi()
        self.horizontalSlider.valueChanged[int].connect(self.recalc)
        self.addBtn(self.nextBtn, self.nextPage)
        self.imgRoot=str(Path(__file__).parents[1])+'/images'
        self.imgPath = self.imgRoot+ '/05.jpg'
        self.addBtn(self.backBtn, self.backWidget)
        self.addBtn(self.helpBtn, self.setHelpWidget)
    def backWidget(self):
        """set's Widget one step back."""
        self.setWidget('start')

    def setHelpWidget(self):
        """Btn function to set help Widget"""
        self.help = HelpPopUp()
        self.help.showHelp(str(Path(__file__).parents[1]) + '/images/help/helpEditing.png')

    def recalc(self):
        _thread.start_new_thread(self.update, ())

    def setPaths(self,imagePath,finalPath):
        self.imagePath=imagePath
        self.finalPath=finalPath
        imageToEngrave = trueBlackWhite(self.imagePath, self.horizontalSlider.value(), self.finalPath)
        self.setImageToEngrave(imageToEngrave)
        self.label.setPixmap(QtGui.QPixmap(self.imgPath).scaled(self.label.size(), QtCore.Qt.KeepAspectRatio))

    def update(self):
        self.lock.acquire()
        try:
            imageToEngrave=trueBlackWhite(self.imagePath, self.horizontalSlider.value(),self.finalPath)
            self.setImageToEngrave(imageToEngrave)
            self.label.setPixmap(QtGui.QPixmap(QtGui.QPixmap(self.imgPath)).scaled(self.label.size(), QtCore.Qt.KeepAspectRatio))
        finally:
            self.lock.release()


    def setImageToEngrave(self, imageToEngrave):
        self.imageToEngrave=imageToEngrave


    def nextPage(self):
        self.setWidget('wait')
        QtCore.QTimer.singleShot(100,self.processImg)


    def processImg(self):
        cal(self, self.world, self.config, True)
        self.widgetDict['placing'].setConfig(self.config)
        self.widgetDict['placing'].refreshCameraImage()
        img = Image.open(self.imgPath)
        desiredWidth = 1500
        percent = (desiredWidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(percent)))
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        img = img.resize((desiredWidth, hsize), Image.NEAREST)
        img = img.convert("RGBA")
        datas = img.getdata()
        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:  # Pixel will be stored as Black Pixel
                newData.append((255, 255, 255, 0))
            else:
                if item[0] > 100:  # Pixel will be stored as Black Pixel
                    newData.append((255, 255, 255, 0))
                else:  # Pixel will be stored as Invisible
                    newData.append(item)
        img.putdata(newData)
        file = open(self.imgRoot + '/06.png', 'wb')
        img.save(file, 'PNG')
        file.flush()
        file.close()
        self.widgetDict['placing'].setImage();
        self.setWidget('placing')