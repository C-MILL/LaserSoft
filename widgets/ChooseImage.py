import platform

from PyQt5.QtCore import pyqtSignal
import sys

from pathlib import Path


from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class ChooseImage(QMainWindow):
    returnImage = pyqtSignal(['QString'])

    def __init__(self):
        super(ChooseImage, self).__init__()
        uic.loadUi(str(Path(__file__).parents[1]) + "/UI/UIFiles/chooseImagePopUp.ui", self)
        self.populate()
        self.treeView.clicked.connect(self.showImage)
        self.okBtn.clicked.connect(self.ok)

    def showSelf(self):
        if platform.machine() != 'x86_64':
            self.showFullScreen()
        else:
            self.show()

    def populate(self):
        path = "C:"
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.treeView.setModel(self.model)
        if platform.machine() != 'x86_64':
            self.treeView.setRootIndex(self.model.index("/media"))
        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def showImage(self, index):
        try:
            self.indexItem = self.model.index(index.row(), 0, index.parent())
            self.filePath = self.model.filePath(self.indexItem)
            self.label.setPixmap(QtGui.QPixmap(self.filePath).scaled(self.label.size(), QtCore.Qt.KeepAspectRatio))
            self.label.setText('')
        except:
            self.label.setText('File format unknown!')

    def ok(self):
        try:
            self.returnImage.emit(self.filePath)
            self.close()
        except:
            print("Error, no image was selected")