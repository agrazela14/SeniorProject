#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we determine the event sender
object.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):

    val = 0;
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        btn1 = QPushButton("Increment", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Decrement", self)
        btn2.move(150, 50)
      
        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar().showMessage('Value is at ' + str(self.val)) 
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()
        
        
    def buttonClicked(self):
      
        sender = self.sender()
        if sender.text() == 'Increment':
            self.val += 1
        if sender.text() == 'Decrement':
            self.val -= 1

        self.statusBar().showMessage('Value is at ' + str(self.val)) 

    def keyPressEvent(self, e):
        
        if e.key() == 0x41 :
            self.val += 1
        if e.key() == 0x53 :
            self.val -= 1
        if e.key() == 0x43 :
            self.close()

        self.statusBar().showMessage('Value is at ' + str(self.val)) 
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
