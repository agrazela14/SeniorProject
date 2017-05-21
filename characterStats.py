#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
import math 

from PyQt5.QtWidgets import (QWidget, QWidgetItem, QDialog, QPushButton, QLineEdit, 
    QInputDialog, QApplication, QMessageBox)

from PyQt5.QtCore import (QSize)

class CharacterStat(QWidgetItem):
    def __init__(self, name, parent):
        super().__init__(parent.parent)
        
        self.parent = parent     
        self.initUI(name, parent)
    
    def initUI(self, name, parent):      

        self.btn = QPushButton(name, parent.parent.parent)
        self.btn.clicked.connect(self.rollDice)

        self.Inc = QPushButton("+", parent.parent.parent)
        self.Dec = QPushButton("-", parent.parent.parent)

        self.Inc.setMaximumSize(40, 40)
        self.Dec.setMaximumSize(40, 40)
        self.Inc.clicked.connect(self.Increment)
        self.Dec.clicked.connect(self.Decrement)

        self.le = QLineEdit(parent.parent.parent)
        #TODO input vallidator for a numeric value only
        #self.le.setInputMask('0')
        self.le.setText("10")
        
    def Increment(self):
        self.le.setText(str(int(self.le.text()) + 1))

    def Decrement(self):
        self.le.setText(str(int(self.le.text()) - 1))

    def rollDice(self):
         
        result = random.randint(1, 20)
        modifiedResult = result + math.ceil((int(self.le.text()) - 11) / 2)
        output =  'Roll Result: ' + str(result) + '\n'
        output += 'Modified Result: ' + str(modifiedResult)
        QMessageBox.about(self.parent.parent, 'Roll Results', output)
        
    def move(self, btnx, btny):
        self.btn.move(btnx, btny)
        self.le.move(btnx + 110, btny)
        self.Inc.move(btnx + 250, btny)
        self.Dec.move(btnx + 290, btny)

#parent is the charactersheet
class StatsBlock(QWidgetItem):
    #variables here get shared with all instances, aka a bad idea

    def __init__(self, parent):
        #variables put here are supposed to be instance only
        super().__init__(parent)

        self.parent = parent
        self.Str = CharacterStat("Strength", self)
        self.Con = CharacterStat("Constitution", self)
        self.Dex = CharacterStat("Dexterity", self)
        self.Wis = CharacterStat("Wisdom", self)
        self.Int = CharacterStat("Intelligence", self)
        self.Cha = CharacterStat("Charisma", self)
        
    def move(self, xVal, yVal):
        self.Str.move(xVal, yVal)
        self.Con.move(xVal, yVal + 30)
        self.Dex.move(xVal, yVal + 60)
        self.Wis.move(xVal, yVal + 90)
        self.Int.move(xVal, yVal + 120)
        self.Cha.move(xVal, yVal + 150)
