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
        self.lay = QHBoxLayout()
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
        
        self.lay.addWidget(self.nameBox)
        self.lay.addWidget(self.wtBox)
        self.lay.addWidget(self.qtBox)
        self.lay.addWidget(self.Inc)
        self.lay.addWidget(self.Dec)

        self.setLayout(self.lay)
        self.show()

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

class header(QWidget):
    def __init__(self, parent):
        super().__init__(parent.parent)
        self.header = QHBoxLayout()
        self.header.addWidget(QLabel("Item Name", self)) 
        self.header.addWidget(QLabel("Weight", self)) 
        self.header.addWidget(QLabel("Quantity", self)) 

        self.setLayout(self.header)
        self.show()
        

#parent is the charactersheet
class ItemsBlock(QWidget):
    #variables here get shared with all instances, aka a bad idea

    def __init__(self, data, parent):
        #variables put here are supposed to be instance only
        super().__init__(parent)

        self.parent = parent
        self.data = data
        self.lay = QVBoxLayout()
        self.itemList = []

        self.addBtn = QPushButton("+", self)
        self.addBtn.clicked.connect(self.addItem)

        self.lay.addWidget(self.addBtn)
        self.lay.addWidget(header(self))

        for info in self.data.items:
            self.fillItem(info)

        self.lay.setSpacing(1)
        self.setLayout(self.lay)
        self.show()


    #used to build the list of existing Items  
    def fillItem(self, itemData):
        #self.itemList.append(CharacterItem(itemData, self))
        self.lay.addWidget(CharacterItem(itemData, self))
    
    #used to add a new Item
    def addItem(self):
        newItem = ["Blank", 0, 1]
        self.lay.addWidget(CharacterItem(newItem, self))
        #self.data.items.append(newItem) 
        #self.itemList.append(CharacterItem(newItem, self))

    def move(self, xVal, yVal):
        self.lay.move(xVal, yVal)
        inc = 30
        self.addBtn.move(xVal, yVal)
        for item in self.lay:
            print('Item: ' + item.info[0]) 
            item.move(xVal, yVal + inc)
            inc += 30
