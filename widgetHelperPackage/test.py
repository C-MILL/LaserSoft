import os

from PyQt5 import QtGui

files=[]
for file in os.listdir("C:/"):
    if file.endswith(".jpeg"):
        files.append(os.path.join(os.getcwd(), file))

for x in files:
    item = QtGui.QListWidgetItem()
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(_fromUtf8(x)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    item.setIcon(icon)
    self.listWidget.addItem(item)