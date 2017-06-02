#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
import math 

from characterStats import *
from characterSkills import *

from PyQt5.QtWidgets import * #(QWidget, QWidgetItem, QDialog, QPushButton, QLineEdit, QInputDialog, QApplication, QMessageBox, QBoxLayout)

from PyQt5.QtCore import (QSize)

class baseTab(QWidget):
    def __init__(self, mainWindow, parent):
        super().__init__()
        
        self.parent = parent
        self.mainWindow = mainWindow
        self.initUI()
        
    def initUI(self):      
        self.newBtn = QPushButton("New", self)
        self.openBtn = QPushButton("Open", self)
        
        self.newBtn.clicked.connect(self.newSheet)
        self.openBtn.clicked.connect(self.openSheet)

        self.newBtn.move(30, 50)
        self.openBtn.move(30, 80)

        self.setGeometry(300, 300, 290, 150)
        self.size = QSize(1000, 1000)
        self.resize(self.size)
        self.setWindowTitle('Base Tab')
        self.show()
        
    def newSheet(self):
        charName = QInputDialog.getText(self.parent, "new sheet", 'new character name')
        self.mainWindow.addNewSheet(charName[0])

    def openSheet(self):
        self.mainWindow.openSheet()
        #openDialog = QFileDialog(self.parent, 'new file', '../characters', '') 


