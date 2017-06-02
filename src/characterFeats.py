import sys
import random
import math 

from PyQt5.QtWidgets import *
#(QWidget, QWidgetItem, QDialog, QPushButton, QLineEdit, QInputDialog, QApplication, QMessageBox)

from PyQt5.QtCore import (QSize)

class CharacterFeat(QWidget):
    def __init__(self, info, parent):
        super().__init__(parent.parent)
        self.parent = parent     
        self.info = info
        self.lay = QHBoxLayout()
        self.initUI()
    
    def initUI(self):      
        self.nameBox = QLineEdit(self.parent)
        self.nameBox.setText(self.info[0])

        self.description = QLineEdit(self.parent)
        self.description.setText(str(self.info[1]))

        self.lay.addWidget(self.nameBox)
        self.lay.addWidget(self.description)

        self.setLayout(self.lay)
        self.show()

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
        self.header.addWidget(QLabel("Name", self)) 
        self.header.addWidget(QLabel("Description", self)) 

        self.setLayout(self.header)
        self.show()
        

#parent is the charactersheet
class FeatsBlock(QWidget):
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

        for info in self.data.feats:
            self.fillItem(info)

        self.lay.setStretchFactor(self.lay, 0)
        self.setLayout(self.lay)
        self.show()


    #used to build the list of existing Items  
    def fillItem(self, itemData):
        #self.itemList.append(CharacterItem(itemData, self))
        self.lay.addWidget(CharacterFeat(itemData, self))
    
    #used to add a new Item
    def addItem(self):
        newFeat = ["Feat Name", "Feat Descrption"]
        self.lay.addWidget(CharacterFeat(newFeat, self))
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
