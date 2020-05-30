from functools import partial
from pathlib import Path
from PyQt5 import uic, QtGui, QtCore
from ImageManipulation import trueBlackWhite
from widgetHelperPackage import DefaultWidget
from widgets.ChooseImage import ChooseImage
from widgets.HelpPopUp import HelpPopUp


class Start(DefaultWidget):#Erbt von der DefaultWidget Klasse
    def __init__(self,stack,widgetDict,laser,world):
        # Initialiesiere die Standardvariablen der seite
        DefaultWidget.__init__(self,stack,widgetDict,laser,world)
        # Pfad für das UI-File
        self.path = 'UI/UIFiles/start.ui'
        # gibt dem Widget einen Namen
        self.id = 'start'
        # Initialisiere den Bildpfad für das Editing
        self.imgPath=''
        # fügt einen Home-Knopf hinzu
        self.homeBtnExists=True
        # Lädt das Widget
        self.loadUi()
        #Füge alle Knöpfe hinzu
        self.addBtn(self.chooseImgBtn, partial(self.callImgPopUp))
        self.addBtn(self.nextBtn, self.setNextPage)
        self.addBtn(self.backBtn, self.backWidget)
        self.addBtn(self.helpBtn, self.setHelpWidget)

    def backWidget(self):
        """set's Widget one step back."""
        self.setWidget('home')

    def setHelpWidget(self):
        """Btn function to set help Widget"""
        self.help = HelpPopUp()
        self.help.showHelp(str(Path(__file__).parents[1]) + '/images/help/helpStart.png')

    def callImgPopUp(self):
        """Lädt das Fenster für die Bildwahl. Nimmt keine Variablen, gibt einen Bildpfad über die "showPicOnBtn" Methode zurück. """
        self.imgPU = ChooseImage()
        self.imgPU.showSelf()
        self.imgPU.returnImage.connect(self.showPicOnBtn)

    def showPicOnBtn(self,imgPath):
        """Speichert das Bild und lade es als Icon auf dem Knopf"""
        self.imgPath=imgPath
        self.chooseImgBtn.setIcon(QtGui.QIcon(imgPath))

    def setNextPage(self):
        self.setWidget('wait')
        QtCore.QTimer.singleShot(100, self.processImg)

    def processImg(self):
        """Lädt die Editing Seite. Nutzt den imgPath."""
        #Setze Editing als Seite
        self.setWidget('editing')
        #Wenn ein Bild geladen wurde, nutze den gegebenen Pfad
        if self.imgPath!='':
            #Konvertiere das Bild in ein Schwarzweissbild und speichere es als Datei ab.
            trueBlackWhite(self.imgPath, 125, str(Path(__file__).parents[1]) + '/images/04.jpg')
            #Lade das Bild in dem Label auf der Editing Seite.
            self.widgetDict['editing'].setPaths(self.imgPath, str(Path(__file__).parents[1]) + '/images/05.jpg')
        else:
            trueBlackWhite(str(Path(__file__).parents[1])+ '/images/01.jpg', 125, str(Path(__file__).parents[1]) + '/images/04.jpg')
            self.widgetDict['editing'].setPaths(str(Path(__file__).parents[1])+ '/images/01.jpg', str(Path(__file__).parents[1]) + '/images/05.jpg')



