import sys
import random
import math 

from PyQt5.QtWidgets import *
#(QWidget, QWidgetItem, QDialog, QPushButton, QLineEdit, QInputDialog, QApplication, QMessageBox)

from PyQt5.QtCore import (QSize)

class CharacterItem(QWidget):
    def __init__(self, info, parent):
        super().__init__(parent.parent)
        self.parent = parent     
        self.info = info
        self.initUI()
    
    def initUI(self):      
        self.nameBox = QLineEdit(self.parent)
        self.nameBox.setText(self.info[0])

        self.wtBox = QLineEdit(self.parent)
        self.wtBox.setText(str(self.info[1]))

        self.qtBox = QLineEdit(self.parent)
        self.qtBox.setText(str(self.info[2]))

        self.Inc = QPushButton("+", self.parent)
        self.Dec = QPushButton("-", self.parent)

        self.Inc.setMaximumSize(40, 40)
        self.Dec.setMaximumSize(40, 40)
        self.Inc.clicked.connect(self.Increment)
        self.Dec.clicked.connect(self.Decrement)

    def Increment(self):
        self.qtBox.setText(str(int(self.qtBox.text()) + 1))
        self.info[2] += 1

    def Decrement(self):
        self.qtBox.setText(str(int(self.qtBox.text()) - 1))
        self.info[2] -= 1

    def move(self, btnx, btny):
        self.nameBox.move(btnx, btny)
        self.wtBox.move(btnx + 150, btny)
        self.qtBox.move(btnx + 300, btny)
        self.Inc.move(btnx + 450, btny)
        self.Dec.move(btnx + 490, btny)

#parent is the charactersheet
class ItemsBlock(QWidget):
    #variables here get shared with all instances, aka a bad idea

    def __init__(self, data, parent):
        #variables put here are supposed to be instance only
        super().__init__(parent)

        self.parent = parent
        self.data = data
        self.itemList = []
        for info in self.data.items:
            self.fillItem(info)

        self.addBtn = QPushButton("+", self)
        self.addBtn.clicked.connect(self.addItem)

    #used to build the list of existing Items  
    def fillItem(self, itemData):
        self.itemList.append(CharacterItem(itemData, self))
    
    #used to add a new Item
    def addItem(self):
        newItem = ["Blank", 0, 1]
        self.data.items.append(newItem) 
        self.itemList.append(CharacterItem(newItem, self))
        self.move(30, 50)

    def move(self, xVal, yVal):
        inc = 30
        self.addBtn.move(xVal, yVal)
        for item in self.itemList:
            item.move(xVal, yVal + inc)
            inc += 30
