#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we receive data from
a QInputDialog dialog. 

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
import random
import math 

from characterStats import *
from characterSkills import *

from PyQt5.QtWidgets import (QWidget, QWidgetItem, QDialog, QPushButton, QLineEdit, 
    QInputDialog, QApplication, QMessageBox)

from PyQt5.QtCore import (QSize)

class CharacterSheet(QWidget):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        self.initUI()
        
    def initUI(self):      
        self.Stats = StatsBlock(self)
        self.Stats.move(30, 50) 

        self.Skills = SkillsBlock(self)
        self.Skills.move(30, 275)
         
        #self.setGeometry(300, 300, 290, 150)
        self.size = QSize(1000, 1000)
        self.resize(self.size)
        self.setWindowTitle('Input dialog')
        self.show()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    sheet = CharacterSheet()
    sys.exit(app.exec_())
