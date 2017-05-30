import sys
import random
import math 
import pickle

from characterStats import *
from characterSkills import *
from characterSheet import *
from baseTab import *

from PyQt5.QtWidgets import (QWidget, QWidgetItem, QDialog, QPushButton, QLineEdit, 
    QInputDialog, QApplication, QMessageBox, QTabBar, QTabWidget)

from PyQt5.QtCore import (QSize)

class sheetAid(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        #Documentation says no parents for tab objects
        self.baseTab = baseTab(self)
        self.ndx = 1
        self.tabs = QTabWidget(self)
        self.tabs.insertTab(0, self.baseTab, "Add Sheets")
        self.size = QSize(1000, 1000)
        self.resize(self.size)
        self.setWindowTitle('DnD 5e character sheet aid')
        self.show()

    def openSheet(self):
        #use pickle.load for this
        typeSet = {0} 
        flagSet = {0}
        fileName = QFileDialog.getOpenFileName(self, 'Open Sheet', '../characters')
        print(fileName)
        fo = open(fileName[0], "w+") 
        sheet = characterSheet(name, fo, False, self)
        self.tabs.addTab(sheet, 0, name)
         
    def addNewSheet(self, name):
        #make a new characterData and pickle.dump in the end to save it
        fo = open("../characters/" + name[0], "w+")
        sheet = characterSheet(name, fo, True, self)
        self.tabs.addTab(sheet, 0, name)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    sheet = sheetAid()
    sys.exit(app.exec_())
