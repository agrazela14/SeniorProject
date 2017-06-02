#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
import math 

from PyQt5.QtWidgets import *

from PyQt5.QtCore import (QSize)

class CharacterStat(QWidget):
    def __init__(self, info, prof, parent):
        super().__init__(parent.parent)
        self.parent = parent     
        self.info = info
        self.prof = prof
        self.initUI()
    
    def initUI(self):      

        self.btn = QPushButton(self.info[0], self.parent)
        self.btn.clicked.connect(self.rollDice)

        self.Inc = QPushButton("+", self.parent)
        self.Dec = QPushButton("-", self.parent)

        self.Inc.setMaximumSize(40, 40)
        self.Dec.setMaximumSize(40, 40)
        self.Inc.clicked.connect(self.Increment)
        self.Dec.clicked.connect(self.Decrement)

        self.save = QPushButton("Save", self.parent)
        self.save.clicked.connect(self.saveRoll)

        self.le = QLineEdit(self.parent)
        self.le.setText(str(self.info[1]))

        self.saveCheck = QCheckBox(self.info[0] + " save", self.parent)
        if (self.info[2]):
            self.saveCheck.setChecked()
        
    def Increment(self):
        self.le.setText(str(int(self.le.text()) + 1))
        self.info[1] += 1

    def Decrement(self):
        self.le.setText(str(int(self.le.text()) - 1))
        self.info[1] -= 1

    def saveRoll(self):
        result = random.randint(1, 20)
        modifiedResult = result + math.ceil((int(self.le.text()) - 11) / 2)
        if self.saveCheck.isChecked():
            modifiedResult += self.prof
        output =  'Roll Result: ' + str(result) + '\n'
        output += 'Modified Result: ' + str(modifiedResult)
        QMessageBox.about(self, 'Roll Results', output)

    def rollDice(self):
        result = random.randint(1, 20)
        modifiedResult = result + math.ceil((int(self.le.text()) - 11) / 2)
        output =  'Roll Result: ' + str(result) + '\n'
        output += 'Modified Result: ' + str(modifiedResult)
        QMessageBox.about(self, 'Roll Results', output)
        
    def move(self, btnx, btny):
        self.btn.move(btnx, btny)
        self.le.move(btnx + 110, btny)
        self.Inc.move(btnx + 250, btny)
        self.Dec.move(btnx + 290, btny)
        self.saveCheck.move(btnx + 340, btny)
        self.save.move(btnx + 480, btny)

#parent is the charactersheet
class StatsBlock(QWidget):
    #variables here get shared with all instances, aka a bad idea

    def __init__(self, data, parent):
        #variables put here are supposed to be instance only
        super().__init__(parent)

        self.parent = parent
        self.Str = CharacterStat(data.stats[0], data.prof, self)
        self.Dex = CharacterStat(data.stats[1], data.prof, self)
        self.Con = CharacterStat(data.stats[2], data.prof, self)
        self.Int = CharacterStat(data.stats[3], data.prof, self)
        self.Wis = CharacterStat(data.stats[4], data.prof, self)
        self.Cha = CharacterStat(data.stats[5], data.prof, self)

        self.setGeometry(400, 400, 290, 150)
        self.size = QSize(1000, 1000)
        self.resize(self.size)
        self.show()
        
    def move(self, xVal, yVal):
        self.Str.move(xVal, yVal)
        self.Con.move(xVal, yVal + 30)
        self.Dex.move(xVal, yVal + 60)
        self.Wis.move(xVal, yVal + 90)
        self.Int.move(xVal, yVal + 120)
        self.Cha.move(xVal, yVal + 150)
