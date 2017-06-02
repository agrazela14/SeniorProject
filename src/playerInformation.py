#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
import math 

from PyQt5.QtWidgets import *

from PyQt5.QtCore import (QSize)

class PlayerInfo(QWidget):
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

    def move(self, xVal, yVal):
        self.title.move(xVal, yVal)
        self.le.move(xVal + 150, yVal)

#parent is the charactersheet
class PlayerInformation(QWidget):
    #variables here get shared with all instances, aka a bad idea

    def __init__(self, data, parent):
        #variables put here are supposed to be instance only
        super().__init__(parent)

        self.parent = parent
        self.player = PlayerInfo('Player Name', data.playerName, self)
        self.character = PlayerInfo('Character Name', data.characterName, self)
        self.characterClass = PlayerInfo('Class', data.characterClass, self)
        self.level = PlayerInfo('Level', data.level, self)
        self.exp = PlayerInfo('Experience', data.exp, self)
        self.align = PlayerInfo('Alignment', data.alignment, self)
        self.background = PlayerInfo('Background', data.background, self)
        self.ideal = PlayerInfo('Ideal', data.ideal, self)
        self.bond = PlayerInfo('Bond', data.bond, self)
        self.flaw = PlayerInfo('Flaw', data.flaw, self)

        self.setGeometry(400, 400, 290, 150)
        self.size = QSize(1000, 1000)
        self.resize(self.size)
        self.show()
        
    def move(self, xVal, yVal):
        self.player.move(xVal, yVal)
        self.character.move(xVal, yVal + 30)
        self.characterClass.move(xVal, yVal + 60)
        self.level.move(xVal, yVal + 90)
        self.exp.move(xVal, yVal + 120)
        self.align.move(xVal, yVal + 150)
        self.background.move(xVal, yVal + 180)
        self.ideal.move(xVal, yVal + 210)
        self.bond.move(xVal, yVal + 240)
        self.flaw.move(xVal, yVal + 270)

