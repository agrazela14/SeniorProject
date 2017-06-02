#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
import math 

from PyQt5.QtWidgets import *

from PyQt5.QtCore import (QSize)

class Money(QWidget):
    def __init__(self, name, info, parent):
        super().__init__(parent.parent)
        self.parent = parent     
        self.name = name
        self.info = info
        self.initUI()
    
    def initUI(self):      
        self.title = QLabel(self.name, self.parent)
        self.le = QLineEdit(self.parent)
        self.le.setText(str(self.info))

        self.Inc = QPushButton("+", self.parent)
        self.Dec = QPushButton("-", self.parent)

        self.Inc.setMaximumSize(40, 40)
        self.Dec.setMaximumSize(40, 40)
        self.Inc.clicked.connect(self.Increment)
        self.Dec.clicked.connect(self.Decrement)

    def Increment(self):
        self.le.setText(str(int(self.le.text()) + 1))
        self.info += 1

    def Decrement(self):
        self.le.setText(str(int(self.le.text()) - 1))
        self.info -= 1

    def move(self, xVal, yVal):
        self.title.move(xVal, yVal)
        self.le.move(xVal + 150, yVal)
        self.Inc.move(xVal + 200, yVal)
        self.Dec.move(xVal + 240, yVal)

#parent is the charactersheet
class MoneyBlock(QWidget):
    #variables here get shared with all instances, aka a bad idea

    def __init__(self, data, parent):
        #variables put here are supposed to be instance only
        super().__init__(parent)

        self.parent = parent
        self.pp = Money('Platinum Pieces (PP)', data.platinum, self)
        self.gp = Money('Gold Pieces (GP)', data.gold, self)
        self.sp = Money('Silver Pieces (SP)', data.silver, self)
        self.cp = Money('Copper Pieces (CP)', data.copper, self)

        self.setGeometry(400, 400, 290, 150)
        self.size = QSize(1000, 1000)
        self.resize(self.size)
        self.show()
        
    def move(self, xVal, yVal):
        self.pp.move(xVal, yVal)
        self.gp.move(xVal, yVal + 30)
        self.sp.move(xVal, yVal + 60)
        self.cp.move(xVal, yVal + 90)

