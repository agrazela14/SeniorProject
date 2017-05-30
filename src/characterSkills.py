#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
import math 

from PyQt5.QtWidgets import (QWidget, QWidgetItem, QDialog, QPushButton, QLineEdit, 
    QInputDialog, QApplication, QMessageBox, QCheckBox)

from PyQt5.QtCore import (QSize)

class CharacterSkill(QWidget):
    def __init__(self, name, relevantStat, parent):
        super().__init__(parent)
        
        self.parent = parent     
        self.relevantStat = relevantStat
        self.initUI(name, parent)

    def rollDice(self):
        result = random.randint(1, 20)
        modifiedResult = result + math.ceil((int(self.relevantStat.le.text()) - 11) / 2)

        if (self.trainedCheck.isChecked()):
            modifiedResult += 2

        output =  'Roll Result: ' + str(result) + '\n'
        output += 'Modified Result: ' + str(modifiedResult)
        QMessageBox.about(self, 'Roll Results', output)
    
    def initUI(self, name, parent):      

        self.btn = QPushButton(name, self)
        self.trainedCheck = QCheckBox('trained', self)
        self.btn.clicked.connect(self.rollDice)

        #self.trainedCheck.setMaximumSize(40, 40)
        
        
    def move(self, btnx, btny):
        self.btn.move(btnx, btny)
        self.trainedCheck.move(btnx + 150, btny)

#Parent here should be charactersheet
class SkillsBlock(QWidget):
    #variables here get shared with all instances, aka a bad idea

    def __init__(self, fo, data, parent):
        #variables put here are supposed to be instance only
        super().__init__(parent)

        self.parent = parent
        self.SkillList = [
            CharacterSkill("Acrobatics (Dex)", parent.Stats.Dex, self),
            CharacterSkill("Handle Animal (Wis)", parent.Stats.Wis, self),
            CharacterSkill("Arcana (Int)", parent.Stats.Int, self),
            CharacterSkill("Athletics (Str)", parent.Stats.Str, self),
            CharacterSkill("Deception (Cha)", parent.Stats.Cha, self),
            CharacterSkill("History (Int)", parent.Stats.Int, self),
        ]
        
    def move(self, xVal, yVal):
        inc = 0
        for skill in self.SkillList: 
            skill.move(xVal, yVal + inc)
            inc += 30
