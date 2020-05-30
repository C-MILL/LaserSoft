from pathlib import Path
import platform

from widgets.HelpPopUp import HelpPopUp

if platform.machine() != 'x86_64':
    from picamera import PiCamera
from PIL import Image
from PyQt5.uic.properties import QtGui
from PyQt5 import QtGui, QtCore

from ImageManipulation.Camera import  camera
from ImageManipulation.ConvertImageToPrintableDict import convertImageToPrintableDict
from ImageManipulation.ImageEditing import *
from widgetHelperPackage import *


class Placing(DefaultWidget):

    def __init__(self, stack, widgetDict, laser, world):
        DefaultWidget.__init__(self, stack, widgetDict, laser, world)
        self.path = 'UI/UIFiles/placing.ui'
        self.id = 'placing'
        self.homeBtnExists = True
        self.loadUi()
        self.imgToEngravePlacer.setStyleSheet("QLabel{ background-color: transparent;}")
        self.imgRoot = str(Path(__file__).parents[1]) + '/images'
        self.placerWidth = self.imgToEngravePlacer.width()
        self.placerHeight = self.imgToEngravePlacer.height()
        self.addBtn(self.rightBtn, self.moveRight)
        self.addBtn(self.leftBtn, self.moveLeft)
        self.addBtn(self.downBtn, self.moveDown)
        self.addBtn(self.upBtn, self.moveUp)
        self.addBtn(self.biggerBtn, self.scaleUp)
        self.addBtn(self.smallerBtn, self.scaleDown)
        self.addBtn(self.resizeBtn, self.setImage)
        self.addBtn(self.refreshCameraImageBtn, self.refreshCameraImage)
        self.camImgCoordX = 100
        self.camImgCoordY = 80
        self.camImgWidth = 460
        self.camImgHeight = 400
        self.addBtn(self.nextBtn, self.nextPage)
        self.addBtn(self.backBtn, self.backWidget)
        self.addBtn(self.helpBtn, self.setHelpWidget)
        if platform.machine() != 'x86_64':
            # PI
            self.camera = PiCamera()
            self.camera.rotation = 180
            self.camera.resolution = (2592, 1944)
    def backWidget(self):
        """set's Widget one step back."""
        self.setWidget('editing')

    def setHelpWidget(self):
        """Btn function to set help Widget"""
        self.help = HelpPopUp()
        self.help.showHelp(str(Path(__file__).parents[1]) + '/images/help/helpPlacing.png')

    def setUpCoords(self):
        self.factorStepToMm = self.world.getFactor()
        self.lengthInMmX = self.world.getLengthX()
        self.lengthInMmY = self.world.getLengthY()
        self.realMaxResolutionX = self.lengthInMmX * self.factorStepToMm
        self.realMaxResolutionY = self.lengthInMmY * self.factorStepToMm

    def moveRight(self):
        placerCoord = self.imgToEngravePlacer.pos()
        placerCoord.setX(placerCoord.x() + 1)
        self.imgToEngravePlacer.move(placerCoord)

    def moveLeft(self):
        placerCoord = self.imgToEngravePlacer.pos()
        placerCoord.setX(placerCoord.x() - 1)
        self.imgToEngravePlacer.move(placerCoord)

    def moveDown(self):
        placerCoord = self.imgToEngravePlacer.pos()
        placerCoord.setY(placerCoord.y() + 1)
        self.imgToEngravePlacer.move(placerCoord)

    def moveUp(self):
        placerCoord = self.imgToEngravePlacer.pos()
        placerCoord.setY(placerCoord.y() - 1)
        self.imgToEngravePlacer.move(placerCoord)

    def scaleUp(self):
        k = self.ratio(self.placerWidth, 5)
        self.imgToEngravePlacer.resize(self.placerWidth * k, self.placerHeight * k)
        self.imgToEngravePlacer.setPixmap(
            QtGui.QPixmap(self.imgRoot + '/06.png').scaled(self.imgToEngravePlacer.size()))
        self.placerWidth = self.imgToEngravePlacer.width()
        self.placerWidth = self.imgToEngravePlacer.width()
        self.placerHeight = self.imgToEngravePlacer.height()

    def scaleDown(self):
        if self.placerHeight > 5 or self.placerHeight > 5:
            k = self.ratio(self.placerWidth, -5)
            self.imgToEngravePlacer.resize(self.placerWidth * k, self.placerHeight * k)
            self.imgToEngravePlacer.setPixmap(
                QtGui.QPixmap(self.imgRoot + '/06.png').scaled(self.imgToEngravePlacer.size()))
            self.placerWidth = self.imgToEngravePlacer.width()
            self.placerWidth = self.imgToEngravePlacer.width()
            self.placerHeight = self.imgToEngravePlacer.height()

    def refreshCameraImage(self):
        if platform.machine() != 'x86_64':
            camera(self.config['cam'], self.camera)
        self.setCameraImage(self.imgRoot + '/finalCamImage.jpg')

    def setCameraImage(self, imagePath):
        image = cv2.imread(imagePath)
        self.cameraImg.setPixmap(QtGui.QPixmap(imagePath).scaled(460, 400, QtCore.Qt.KeepAspectRatio))
        self.camImgWidth = 460
        self.camImgHeight = 400

    def setImage(self):
        image = PIL.Image.open(self.imgRoot + '/06.png')
        self.showImageWidth, self.showImageHeight = image.size
        while self.showImageWidth > self.camImgWidth or self.showImageHeight > self.camImgHeight:
            self.showImageWidth /= 4
            self.showImageHeight /= 4

        placerCoord = self.imgToEngravePlacer.pos()
        placerCoord.setX(self.camImgCoordX + self.camImgWidth / 2 - self.showImageWidth / 2)
        placerCoord.setY(self.camImgCoordY + self.camImgHeight / 2 - self.showImageHeight / 2)
        self.imgToEngravePlacer.move(placerCoord)
        self.imgToEngravePlacer.resize(self.showImageWidth, self.showImageHeight)
        self.imgToEngravePlacer.setPixmap(
            QtGui.QPixmap(self.imgRoot + '/06.png').scaled(self.imgToEngravePlacer.size(), QtCore.Qt.KeepAspectRatio))
        self.placerWidth = self.imgToEngravePlacer.width()
        self.placerHeight = self.imgToEngravePlacer.height()

    def convertImageRealSize(self, img):
        self.setUpCoords()
        maxX = self.realMaxResolutionX
        maxY = self.realMaxResolutionY
        currentX = self.placerWidth
        currentY = self.placerHeight
        ratio = maxY / self.camImgHeight
        newX = currentX * ratio
        newY = currentY * ratio
        try:
            return resizeImg(img, newX, newY)
        except:
            return cv2Pil(resizeImg(pil2Cv(img), newX, newY), self.imgRoot + '/15.jpg')

    def nextPage(self):
        self.setWidget('wait')
        QtCore.QTimer.singleShot(100, self.processImg)

    def processImg(self):
        self.setWidget('chooseMaterial')
        showImagePos = self.imgToEngravePlacer.pos()
        showImagePosX = showImagePos.x()
        showImagePosY = showImagePos.y()
        edgeTL = showImagePosX, showImagePosY
        edgeTR = showImagePosX + self.placerWidth, showImagePosY
        edgeBL = showImagePosX, showImagePosY + self.placerHeight
        edgeBR = showImagePosX + self.placerWidth, showImagePosY + self.placerHeight
        self.originalSizedImage = PIL.Image.open(self.imgRoot + '/05.jpg')
        self.convertedImage = self.convertImageRealSize(self.originalSizedImage)
        self.convertedImageWidth, self.convertedImageHeight = self.convertedImage.size
        self.ratioBetweenImages = self.convertedImageWidth / self.placerWidth
        self.convertedImage = pil2Cv(self.convertedImage)
        self.convertedImage = cv2.threshold(self.convertedImage, 125, 255, cv2.THRESH_BINARY)[1]
        writeImgToFile(self.convertedImage, self.imgRoot + '/08.jpg')
        if self.out(edgeTL[0], self.camImgCoordX + self.camImgWidth) or self.out(self.camImgCoordX,
                                                                                 edgeBR[0]) or self.out(
                self.camImgCoordY, edgeBL[1]) or self.out(edgeTL[1], self.camImgCoordX + self.camImgWidth):
            clearImg(self.imgRoot + '/05.jpg')
            print('ERROR-Image is not in printing Area')

        else:
            if self.out(edgeBR[0], self.camImgCoordX + self.camImgWidth):  # Out right
                endX = int((self.camImgCoordX + self.camImgWidth - edgeBL[0]) * self.ratioBetweenImages)
            else:
                endX = self.convertedImageWidth

            if self.out(self.camImgCoordX, edgeTL[0]):  # Out left
                beginningX = int((self.camImgCoordX - edgeBR[0]) * self.ratioBetweenImages)
            else:
                beginningX = 0

            if self.out(self.camImgCoordY, edgeTL[1]):  # Out Top
                beginningY = int((self.camImgCoordY - edgeTR[1]) * self.ratioBetweenImages)
            else:
                beginningY = 0

            if self.out(edgeBR[1], self.camImgCoordY + self.camImgHeight):  # Out Bottom
                endY = int((self.camImgCoordY + self.camImgHeight - edgeBL[1]) * self.ratioBetweenImages)
            else:
                endY = self.convertedImageHeight
            self.convertedImage = self.convertedImage[beginningY:endY - 1, beginningX:endX - 1]
            if edgeTL[0] < 100:
                edgeTL = 100, edgeTL[1]
            if edgeTL[1] < 80:
                edgeTL = edgeTL[0], 80
            xToPlace = int((edgeTL[0] - self.camImgCoordX) * self.ratioBetweenImages)
            yToPlace = int((edgeTL[1] - self.camImgCoordY) * self.ratioBetweenImages)
            imageInWorld = self.placeImgInReal(xToPlace, yToPlace, self.convertedImage)
            writeImgToFile(imageInWorld, self.imgRoot + '/09.jpg')
            dict = convertImageToPrintableDict(imageInWorld)
            self.goToNextPage(dict)

    def placeImgInReal(self, x, y, img):
        blankImage = 255 * np.ones(shape=[self.realMaxResolutionY, self.realMaxResolutionX], dtype=np.uint8)
        blankImage[y:y + img.shape[0], x:x + img.shape[1]] = img
        return blankImage

    def ratio(self, x, z):
        k = (x + z) / x
        return k

    def out(self, pos1, pos2):
        if pos1 > pos2:
            return True
        else:
            return False

    def goToNextPage(self, dict):
        ChooseMaterial = self.widgetDict['chooseMaterial']
        ChooseMaterial.setDict(dict)

