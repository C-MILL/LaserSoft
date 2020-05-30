import shutil
from functools import partial
from pathlib import Path
from platform import system

import cv2
from PyQt5 import uic, QtGui
from PyQt5.QtCore import pyqtSignal

from ImageManipulation.ImageEditing import trueBlackWhite
from widgetHelperPackage import DefaultWidget
from widgets.ChooseImage import ChooseImage


class WhatToDo(DefaultWidget):
    def __init__(self,stack,widgetDict,laser,world):
        DefaultWidget.__init__(self,stack,widgetDict,laser,world)
        self.path = 'UI/UIFiles/whatToDo.ui'
        self.id = 'whatToDo'
        self.homeBtnExists=True
        self.path
        self.loadUi()
        self.addBtn(self.engraveImageBtn,self.setEngraving)
        self.addBtn(self.cutImageBtn,self.setCutting)

    def showPicOnBtn(self,imgPath):
        self.imgPath=imgPath
        self.chooseImgBtn.setIcon(QtGui.QIcon(imgPath))

    def setImagePath(self,imagePath):
        self.imagePath=imagePath
        self.cutting()
        self.engraving()



    def cutting(self):
        image = cv2.imread (self.imagePath)
        cv2.waitKey (0)
        median = cv2.medianBlur (image, 5) #"Verunschärfe" bild für die einfachere weiterverarbeitung
        gray = cv2.cvtColor (median, cv2.COLOR_BGR2GRAY) #Bild wird Schwarzweiss
        clahe = cv2.createCLAHE (clipLimit=2.0, tileGridSize=(8, 8)) #erhöhe Kontrast
        cl1 = clahe.apply (gray)
        edges_filtered = cv2.Canny(cl1, 60, 120)#Filtere kleine veränderungen im Bild. (Zum Beispiel Barthaare werden zu masse vereint, man will ja nicht 200 Barthaare einzeln Drucken)
        edged = cv2.Canny (edges_filtered, 20, 10) #Einstellungen um Konturen im Bild zu finden (morph wird hier genutzt um den THreashold wert für zu erkennende Konturen zu verändern)
        cv2.waitKey (0)
        if system() != 'Windows':
            _, contours, _ = cv2.findContours (edged,cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE) #Finde Konturen
        else:
            contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # Finde Konturen
        cv2.waitKey (0)
        cv2.drawContours (image, contours, -1, (0, 255, 0), 3) #Zeichne Konturen auf einen Schwazen Hintergrund
        cv2.imwrite (str(Path(__file__).parents[1]) + '/images/03.jpg', edged, [int (cv2.IMWRITE_JPEG_QUALITY), 90]) #Schreibe Bild als File
        self.cutImageBtn.setIcon(QtGui.QIcon(str(Path(__file__).parents[1]) + '/images/03.jpg'))
    def engraving(self):
        trueBlackWhite(self.imagePath, 125,str(Path(__file__).parents[1]) + '/images/04.jpg')
        self.engraveImageBtn.setIcon(QtGui.QIcon(str(Path(__file__).parents[1]) + '/images/04.jpg'))

    def setEngraving(self):
        self.widgetDict['editing'].setPaths(self.imagePath,str(Path(__file__).parents[1])+ '/images/05.jpg')
        self.setWidget('editing')
    def setCutting(self):
        pass