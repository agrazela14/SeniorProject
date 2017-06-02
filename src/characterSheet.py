#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
import math 
import pickle

from characterStats import *
from characterSkills import *
from characterItems import *
from characterMoney import *
from characterFeats import *
from playerInformation import *
from characterInformation import *

from PyQt5.QtWidgets import (QWidget, QWidgetItem, QDialog, QPushButton, QLineEdit, 
    QInputDialog, QApplication, QMessageBox)

from PyQt5.QtCore import *

class Attack():
    def __init__(self, name, light, diceNum, diceSides, reach, prof):
        self.name = name 
        self.light = light 
        self.diceNum = diceNum 
        self.diceSides = diceSides 
        self.reach = reach 
        self.prof = prof 

class Item():
    def __init__(self, name, quantity, wt):
        self.name = name
        self.quantity = quantity 
        self.wt = wt

class CharacterData():
    def __init__(self):
        #Player Info
        self.playerName = "Player"
        self.characterName = "Character"
        self.characterClass = "Commoner"
        self.level = 1 
        self.exp = 0
        self.alignment = "N"
        self.background = "background"
        self.ideal = "ideal"
        self.bond = "bond"
        self.flaw = "flaw"
        
        #Character Stats
        self.stats = [
            ["Strength", 10, False],
            ["Dexterity", 10, False],
            ["Constitution", 10, False],
            ["Intelligence", 10, False],
            ["Wisdom", 10, False],
            ["Charisma", 10, False]
        ]
        
        #Character Skills
        self.skills = [
            ["Acrobatics (Dex)", 1, False],
            ["Animal Handling (Wis)", 4, False],
            ["Arcana (Int)", 3, False],
            ["Athletics (Str)", 0, False],
            ["Deception (Cha)", 5, False],
            ["History (Int)", 3, False],
            ["Insight (Wis)", 4, False],
            ["Intimidation (Cha)", 5, False],
            ["Investigation (Int)", 3, False],
            ["Medicine (Wis)", 4, False],
            ["Nature (Int)", 3, False],
            ["Perception (Wis)", 4, False],
            ["Performance (Cha)", 5, False],
            ["Persuasion (Cha)", 5, False],
            ["Religion (Int)", 3, False],
            ["Sleight of Hand (Dex)", 1, False],
            ["Stealth (Dex)", 1, False],
            ["Survival (Wis)", 4, False]
        ]
        
        #Character Feats/Features
        self.feats = [['Feat Name', 'Feat Description']]

        #Character Information
        self.curHp = 0
        self.maxHp = 0
        self.tempHp = 0
        self.prof = 2
        self.ac = 10
        self.initiative = 0
        self.moveSpeed = 30
        
        #Character Attacks
        self.Attacks = [Attack("unarmed", True, 1, 4, 0, True)]

        #Character Spells
        self.firstLevelSlots = 0
        self.secondLevelSlots = 0
        self.thirdLevelSlots = 0
        self.fourthLevelSlots = 0
        self.fifthLevelSlots = 0
        self.sixthLevelSlots = 0
        self.seventhLevelSlots = 0
        self.eighthLevelSlots = 0
        self.ninthLevelSlots = 0
        
        self.spells = ["blank"]

        #If at all possible, make spells and items work where 2 things, money/items and slots/spells are on same page
        
        #Character Money
        self.platinum = 0
        self.gold = 0
        self.silver = 0
        self.copper = 0
        #Character Items 
        self.items = [["Commoner's Clothes", 3, 1]] 

        #Try to combine the Money and Items, put money on the left or top 


class CharacterSheet(QWidget):
    def __init__(self, name, fo, new, parent):
        super().__init__()
        
        self.parent = parent
        self.fo = fo
        self.name = name

        if new:
            self.data = CharacterData()

        else:
            self.data = pickle.load(fo)
        self.initUI()
        
    def initUI(self):      
        #Make Tabs so that stuff works
        #Player Info, Stats, Skills, items, feats, spells
        self.size = QSize(600, 700)
        self.resize(self.size)
        self.setWindowTitle(self.name)

        self.tabs = QTabWidget(self)
        self.tabs.resize(600, 700)
        self.tabs.setMovable(True)
        self.tabs.setMinimumSize(150, 20)

        self.PlayerInfo = PlayerInformation(self.data, self.tabs)
        self.PlayerInfo.move(30, 50)
        self.tabs.addTab(self.PlayerInfo, 'Info')

        #self.charInfo = CharacterInformation(self.data, self.tabs)
        #self.charInfo.move(30, 50)
        #self.tabs.addTab(self.charInfo, 'Vitals')

        self.Stats = StatsBlock(self.data, self.tabs)
        self.Stats.move(30, 50) 
        self.tabs.addTab(self.Stats, "Stats")

        self.Skills = SkillsBlock(self.data, self.tabs)
        self.Skills.move(30, 50)
        self.tabs.addTab(self.Skills, "Skills")

        self.Feats = FeatsBlock(self.data, self)
        self.tabs.addTab(self.Feats, "Feat/ures")

        self.Items = ItemsBlock(self.data, self)
        #self.Items.move(30, 50)
        self.tabs.addTab(self.Items, "Items")

        self.Money = MoneyBlock(self.data, self)
        self.Money.move(30, 50)
        self.tabs.addTab(self.Money, "Money")
        #self.setGeometry(300, 250, 250, 150)
        #self.show()
        #self.tabs.show()
         

    #Needs an on close function for pickling the data file

    def writeData(self):
        print('Close Event Triggered for: ' + self.name)
        print('Highest Protocol: ' + str(pickle.HIGHEST_PROTOCOL))
        pickle.dump(self.data, self.fo, 3)

