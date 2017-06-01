#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
import math 

from PyQt5.QtWidgets import * 
#(QWidget, QWidgetItem, QDialog, QPushButton, QLineEdit, QInputDialog, QApplication, QMessageBox, QCheckBox)

from PyQt5.QtCore import (QSize)

class CharacterSkill(QWidget):
    def __init__(self, info, relevantStat, prof, parent):
        super().__init__(parent)
        
        self.info = info
        self.parent = parent     
        self.relevantStat = relevantStat
        self.prof = prof
        self.initUI()

    def initUI(self):      
        print('Skill name: ' + self.info[0])
        self.btn = QPushButton(self.info[0], self.parent)
        self.trainedCheck = QCheckBox('trained', self.parent)

        if (self.info[2]):
            self.trainedCheck.setChecked()
        self.btn.clicked.connect(self.rollDice)

    def rollDice(self):
        result = random.randint(1, 20)
        modifiedResult = result + math.ceil((self.relevantStat[1] - 11) / 2)

        if (self.trainedCheck.isChecked()):
            modifiedResult += self.prof

        output =  'Roll Result: ' + str(result) + '\n'
        output += 'Modified Result: ' + str(modifiedResult)
        QMessageBox.about(self, 'Roll Results', output)
        
    def move(self, btnx, btny):
        self.btn.move(btnx, btny)
        self.trainedCheck.move(btnx + 150, btny)

#Parent here should be charactersheet
class SkillsBlock(QWidget):
    #variables here get shared with all instances, aka a bad idea

    def __init__(self, data, parent):
        #variables put here are supposed to be instance only
        super().__init__(parent)

        self.parent = parent
        self.SkillList = [
            CharacterSkill(data.skills[0], data.stats[data.skills[0][1]], data.prof, self),
            CharacterSkill(data.skills[1], data.stats[data.skills[1][1]], data.prof, self),
            CharacterSkill(data.skills[2], data.stats[data.skills[2][1]], data.prof, self),
            CharacterSkill(data.skills[3], data.stats[data.skills[3][1]], data.prof, self),
            CharacterSkill(data.skills[4], data.stats[data.skills[4][1]], data.prof, self),
            CharacterSkill(data.skills[5], data.stats[data.skills[5][1]], data.prof, self),
            CharacterSkill(data.skills[6], data.stats[data.skills[6][1]], data.prof, self),
            CharacterSkill(data.skills[7], data.stats[data.skills[7][1]], data.prof, self),
            CharacterSkill(data.skills[8], data.stats[data.skills[8][1]], data.prof, self),
            CharacterSkill(data.skills[9], data.stats[data.skills[9][1]], data.prof, self),
            CharacterSkill(data.skills[10], data.stats[data.skills[10][1]], data.prof, self),
            CharacterSkill(data.skills[11], data.stats[data.skills[11][1]], data.prof, self),
            CharacterSkill(data.skills[12], data.stats[data.skills[12][1]], data.prof, self),
            CharacterSkill(data.skills[13], data.stats[data.skills[13][1]], data.prof, self),
            CharacterSkill(data.skills[14], data.stats[data.skills[14][1]], data.prof, self),
            CharacterSkill(data.skills[15], data.stats[data.skills[15][1]], data.prof, self),
            CharacterSkill(data.skills[16], data.stats[data.skills[16][1]], data.prof, self),
            CharacterSkill(data.skills[17], data.stats[data.skills[17][1]], data.prof, self),
        ]
        
    def move(self, xVal, yVal):
        inc = 0
        for skill in self.SkillList: 
            skill.move(xVal, yVal + inc)
            inc += 30
