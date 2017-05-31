import sys
import random
import math 

from PyQt5.QtWidgets import (QWidget, QWidgetItem, QDialog, QPushButton, QLineEdit, 
    QInputDialog, QApplication, QMessageBox)

from PyQt5.QtCore import (QSize)

class CharacterStat(QWidget):
    def __init__(self, info, parent):
        super().__init__(parent.parent)
        self.parent = parent     
        self.info = info
        self.initUI()
    
    def initUI(self):      

        self.btn = QPushButton(self.info[0], self)
        self.btn.clicked.connect(self.rollDice)

        self.Inc = QPushButton("+", self)
        self.Dec = QPushButton("-", self)

        self.Inc.setMaximumSize(40, 40)
        self.Dec.setMaximumSize(40, 40)
        self.Inc.clicked.connect(self.Increment)
        self.Dec.clicked.connect(self.Decrement)

        self.le = QLineEdit(self)
        self.le.setText(str(self.info[1]))

        self.saveCheck = QCheckBox(self.info[0] + "save", self)
        if (self.info[2]):
            self.saveCheck.setChecked()
        
    def Increment(self):
        self.le.setText(str(int(self.le.text()) + 1))

    def Decrement(self):
        self.le.setText(str(int(self.le.text()) - 1))

    def rollDice(self):
        result = random.randint(1, 20)
        modifiedResult = result + math.ceil((int(self.le.text()) - 11) / 2)
        output =  'Roll Result: ' + str(result) + '\n'
        output += 'Modified Result: ' + str(modifiedResult)
        QMessageBox.about(self.parent.parent, 'Roll Results', output)
        
    def move(self, btnx, btny):
        self.btn.move(btnx, btny)
        self.le.move(btnx + 110, btny)
        self.Inc.move(btnx + 250, btny)
        self.Dec.move(btnx + 290, btny)

#parent is the charactersheet
class StatsBlock(QWidget):
    #variables here get shared with all instances, aka a bad idea

    def __init__(self, data, parent):
        #variables put here are supposed to be instance only
        super().__init__(parent)

        self.parent = parent
        self.Str = CharacterStat(data.stats[0], self)
        self.Dex = CharacterStat(data.stats[1], self)
        self.Con = CharacterStat(data.stats[2], self)
        self.Int = CharacterStat(data.stats[3], self)
        self.Wis = CharacterStat(data.stats[4], self)
        self.Cha = CharacterStat(data.stats[5], self)
        
    def move(self, xVal, yVal):
        self.Str.move(xVal, yVal)
        self.Con.move(xVal, yVal + 30)
        self.Dex.move(xVal, yVal + 60)
        self.Wis.move(xVal, yVal + 90)
        self.Int.move(xVal, yVal + 120)
        self.Cha.move(xVal, yVal + 150)
