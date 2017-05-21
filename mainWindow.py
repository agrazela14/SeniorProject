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
from characterSheet import *

from PyQt5.QtWidgets import (QWidget, QWidgetItem, QDialog, QPushButton, QLineEdit, 
    QInputDialog, QApplication, QMessageBox, QTabBar, QTabWidget)

from PyQt5.QtCore import (QSize)

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        
        #self.tabBar = QTabBar(self)
        self.sheetList = [CharacterSheet(self)]
        self.sheetList.append(CharacterSheet(self))

        self.tabs = QTabWidget(self)
        self.tabs.insertTab(0, self.sheetList[0], "Sheet1")
        self.tabs.insertTab(1, self.sheetList[1], "Sheet2")
        self.size = QSize(1000, 1000)
        self.resize(self.size)
        self.setWindowTitle('DnD 5e character sheet aid')
        self.show()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    sheet = mainWindow()
    sys.exit(app.exec_())
