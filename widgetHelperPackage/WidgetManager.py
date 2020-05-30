from PyQt5.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

from functools import partial

from widgets import *


class WidgetManager(QWidget):
    def __init__(self, laser, world, parent=None):
        super(WidgetManager, self).__init__(parent)
        self.stack = QStackedWidget()
        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)
        self.laser = laser
        self.widgetDic={}
        self.world=world


    def addWidgetsToStack(self,widgetDic):
        """Current Object (A widget) gets stored in the Dictionary. Key is the ID of current Object"""
        for formkey in widgetDic:
            widget = widgetDic[formkey]
            self.stack.addWidget(widget)
        return self.stack

    def loadWidget(self, widgetStr):
        """Imput: Widget Object"""
        widget = widgetStr(self.stack, self.widgetDic, self.laser,self.world)
        self.widgetDic[widget.id] = widget

    def getAllWidgets(self):
        """place to initialize all Widgets"""
        self.loadWidget(Home)
        self.loadWidget(Settings)
        self.loadWidget(Working)
        self.loadWidget(ManualMode)
        self.loadWidget(Configuration)
        self.loadWidget(Working)
        self.loadWidget(Start)
        self.loadWidget(Editing)
        self.loadWidget(WhatToDo)
        self.loadWidget(Placing)
        self.loadWidget(ChooseMaterial)
        self.loadWidget(Wait)
        return self.widgetDic
