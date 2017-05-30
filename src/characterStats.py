import sys
import random
import math 

from PyQt5.QtWidgets import (QWidget, QWidgetItem, QDialog, QPushButton, QLineEdit, 
    QInputDialog, QApplication, QMessageBox)

from PyQt5.QtCore import (QSize)

class CharacterStat(QWidget):
    def __init__(self, name, parent):
        super().__init__(parent.parent)
        
        self.parent = parent     
        self.initUI(name, parent)
    
    def initUI(self, name, fo, parent):      

        self.btn = QPushButton(name, self)
        self.btn.clicked.connect(self.rollDice)

        self.Inc = QPushButton("+", self)
        self.Dec = QPushButton("-", self)

        self.Inc.setMaximumSize(40, 40)
        self.Dec.setMaximumSize(40, 40)
        self.Inc.clicked.connect(self.Increment)
        self.Dec.clicked.connect(self.Decrement)

        self.le = QLineEdit(self)
        #TODO input vallidator for a numeric value only
        #self.le.setInputMask('0')
        self.le.setText("10")
        
    def Increment(self):
        self.le.setText(str(int(self.le.text()) + 1))
        self.fo = utils.setFo('Stats', self.name) 
        self.fo.write(self.le.text())

    def Decrement(self):
        self.le.setText(str(int(self.le.text()) - 1))
        self.fo = utils.setFo('Stats', self.name) 
        self.fo.write(self.le.text())

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

    def __init__(self, fo, parent):
        #variables put here are supposed to be instance only
        super().__init__(parent)

        self.parent = parent
        self.Str = CharacterStat("Strength", fo, self)
        self.Con = CharacterStat("Constitution", fo, self)
        self.Dex = CharacterStat("Dexterity", fo, self)
        self.Wis = CharacterStat("Wisdom", fo, self)
        self.Int = CharacterStat("Intelligence", fo, self)
        self.Cha = CharacterStat("Charisma", fo, self)
        
    def move(self, xVal, yVal):
        self.Str.move(xVal, yVal)
        self.Con.move(xVal, yVal + 30)
        self.Dex.move(xVal, yVal + 60)
        self.Wis.move(xVal, yVal + 90)
        self.Int.move(xVal, yVal + 120)
        self.Cha.move(xVal, yVal + 150)
