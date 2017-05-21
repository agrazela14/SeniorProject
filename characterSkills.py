#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
import math 

from PyQt5.QtWidgets import (QWidget, QWidgetItem, QDialog, QPushButton, QLineEdit, 
    QInputDialog, QApplication, QMessageBox, QCheckBox)

from PyQt5.QtCore import (QSize)

class CharacterSkill(QWidgetItem):
    def __init__(self, name, relevantStat, parent):
        super().__init__(parent.parent)
        
        self.parent = parent     
        self.relevantStat = relevantStat
        self.initUI(name, parent)

    def rollDice(self):
        result = random.randint(1, 20)
        modifiedResult = result + math.ceil((int(self.relevantStat) - 11) / 2)

        if (self.trainedCheck.isChecked()):
            modifiedResult += 2

        output =  'Roll Result: ' + str(result) + '\n'
        output += 'Modified Result: ' + str(modifiedResult)
        QMessageBox.about(self.parent.parent, 'Roll Results', output)
    
    def initUI(self, name, parent):      

        self.btn = QPushButton(name, parent.parent.parent)
        self.trainedCheck = QCheckBox('trained', parent.parent.parent)
        self.btn.clicked.connect(self.rollDice)

        #self.trainedCheck.setMaximumSize(40, 40)
        
        
    def move(self, btnx, btny):
        self.btn.move(btnx, btny)
        self.trainedCheck.move(btnx + 150, btny)

#Parent here should be charactersheet
class SkillsBlock(QWidgetItem):
    #variables here get shared with all instances, aka a bad idea

    def __init__(self, parent):
        #variables put here are supposed to be instance only
        super().__init__(parent)

        self.parent = parent
        self.SkillList = [
            CharacterSkill("Acrobatics (Dex)", parent.Stats.Dex.le.text(), self),
            CharacterSkill("Handle Animal (Wis)", parent.Stats.Wis.le.text(), self),
            CharacterSkill("Arcana (Int)", parent.Stats.Int.le.text(), self),
            CharacterSkill("Athletics (Str)", parent.Stats.Str.le.text(), self),
            CharacterSkill("Deception (Cha)", parent.Stats.Cha.le.text(), self),
            CharacterSkill("History (Int)", parent.Stats.Int.le.text(), self),
        ]
        
    def move(self, xVal, yVal):
        inc = 0
        for skill in self.SkillList: 
            skill.move(xVal, yVal + inc)
            inc += 30
