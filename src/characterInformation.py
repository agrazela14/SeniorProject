#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
import math 

from PyQt5.QtWidgets import *

from PyQt5.QtCore import (QSize)

class CharacterInfo(QWidget):
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

#parent is the charactersheet
class CharacterInformation(QWidget):
    #variables here get shared with all instances, aka a bad idea

    def __init__(self, data, parent):
        #variables put here are supposed to be instance only
        super().__init__(parent)

        self.parent = parent
        self.tempHp = CharacterInfo('Temp Hp', data.tempHp, self)
        self.curHp = CharacterInfo('Current Hp', data.curHp, self)
        self.maxHp = CharacterInfo('Max Hp', data.maxHp, self)
        self.ac = CharacterInfo('AC', data.ac, self)
        self.prof = CharacterInfo('Proficency', data.prof, self)
        self.move = CharacterInfo('Move', data.exp, self)
        self.init = CharacterInfo('Initiative', data.alignment, self)

        self.setGeometry(400, 400, 290, 150)
        self.size = QSize(1000, 1000)
        self.resize(self.size)
        self.show()
        
    def move(self, xVal, yVal):
        self.tempHp.move(xVal, yVal)
        self.curHp.move(xVal, yVal + 30)
        self.maxHp.move(xVal, yVal + 60)
        self.ac.move(xVal, yVal + 90)
        self.prof.move(xVal, yVal + 120)
        self.move.move(xVal, yVal + 150)
        self.init.move(xVal, yVal + 180)

