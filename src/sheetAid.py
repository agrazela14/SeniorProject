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

class sheetAid(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        #Documentation says no parents for tab objects
        self.tabs = QTabWidget(self)
        self.baseTab = baseTab(self, self.tabs)
        self.ndx = 1
        self.tabs.insertTab(0, self.baseTab, "Add Sheets")
        self.tabs.resize(600, 700)
        self.size = QSize(600, 700)
        self.resize(self.size)
        self.setWindowTitle('DnD 5e character sheet aid')
        self.sheets = []
        self.show()

    def openSheet(self):
        #use pickle.load for this
        typeSet = {0} 
        flagSet = {0}
        fileName = QFileDialog.getOpenFileName(self, 'Open Sheet', '../characters')
        print(fileName)
        fo = open(fileName[0], "rb+") 
        sheet = CharacterSheet(fileName[0], fo, False, self.tabs)
        self.sheets.append(sheet)
        self.tabs.addTab(sheet, fileName[0])
         
    def addNewSheet(self, name):
        #make a new characterData and pickle.dump in the end to save it
        fo = open("../characters/" + name, "wb+")
        sheet = CharacterSheet(name, fo, True, self.tabs)
        self.sheets.append(sheet)
        self.tabs.addTab(sheet, name)

    def closeEvent(self, event):
        print('Close Event Triggered for: MainWindow')
        for char in self.sheets:
            char.writeData()

        event.accept()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    sheet = sheetAid()
    sys.exit(app.exec_())
