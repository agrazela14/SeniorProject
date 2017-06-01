#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
import math 

from characterStats import *
from characterSkills import *
from characterItems import *
from playerInformation import *

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
        self.playerName = "Player"
        self.characterName = "Character"
        self.characterClass = "Commoner"
        self.level = 1 
        self.exp = 0
        self.alignment = "N"
        
        #Actually just do a list of "statInfo"s that can be indexed into in each charStat
        self.stats = [
            #characterStats.statInfo("Strength", 10, False),
            #characterStats.statInfo("Dexterity", 10, False),
            #characterStats.statInfo("Constitution", 10, False),
            #characterStats.statInfo("Intelligence", 10, False),
            #characterStats.statInfo("Wisdom", 10, False),
            #characterStats.statInfo("Charisma", 10, False)
            ["Strength", 10, False],
            ["Dexterity", 10, False],
            ["Constitution", 10, False],
            ["Intelligence", 10, False],
            ["Wisdom", 10, False],
            ["Charisma", 10, False]
        ]
        #do the same with skills
        #self.skills = characterSkills.skillBlock()
        self.skills = [
            #characterSkills.skillInfo("Acrobatics", 1, False),
            #characterSkills.skillInfo("Animal Handling", 4, False),
            #characterSkills.skillInfo("Arcana", 3, False),
            #characterSkills.skillInfo("Athletics", 0, False),
            #characterSkills.skillInfo("Deception", 5, False),
            #characterSkills.skillInfo("History", 3, False),
            #characterSkills.skillInfo("Insight", 4, False),
            #characterSkills.skillInfo("Intimidation", 5, False),
            #characterSkills.skillInfo("Investigation", 3, False),
            #characterSkills.skillInfo("Medicine", 4, False),
            #characterSkills.skillInfo("Nature", 3, False),
            #characterSkills.skillInfo("Perception", 4, False),
            #characterSkills.skillInfo("Performance", 5, False),
            #characterSkills.skillInfo("Persuasion", 5, False),
            #characterSkills.skillInfo("Religion", 3, False),
            #characterSkills.skillInfo("Sleight of Hand", 1, False),
            #characterSkills.skillInfo("Stealth", 1, False),
            #characterSkills.skillInfo("Survival", 4, False)
            ["Acrobatics", 1, False],
            ["Animal Handling", 4, False],
            ["Arcana", 3, False],
            ["Athletics", 0, False],
            ["Deception", 5, False],
            ["History", 3, False],
            ["Insight", 4, False],
            ["Intimidation", 5, False],
            ["Investigation", 3, False],
            ["Medicine", 4, False],
            ["Nature", 3, False],
            ["Perception", 4, False],
            ["Performance", 5, False],
            ["Persuasion", 5, False],
            ["Religion", 3, False],
            ["Sleight of Hand", 1, False],
            ["Stealth", 1, False],
            ["Survival", 4, False]
        ]
        
        #Just make feats a list of strings
        self.feats = ['']
        #self.str = 10
        #self.dexSave = False
        #self.dex = 10
        #self.conSave = False
        #self.con = 10
        #self.intSave = False
        #self.int = 10
        #self.wisSave = False
        #self.wis = 10
        #self.wisSave = False
        #self.cha = 10
        #self.chaSave = False

        self.curHp = 0
        self.maxHp = 0
        self.tempHp = 0
        self.prof = 1
        self.ac = 10
        self.initiative = 0
        self.moveSpeed = 30

        self.Attacks = [Attack("unarmed", True, 1, 4, 0, True)]
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

        self.platinum = 0
        self.gold = 0
        self.silver = 0
        self.copper = 0
        self.items = [["Commoner's Clothes", 3, 1]] 


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
        self.size = QSize(1000, 1000)
        self.resize(self.size)
        self.setWindowTitle(self.name)

        self.tabs = QTabWidget(self)
        self.tabs.resize(1000, 1000)
        self.tabs.setMovable(True)
        self.tabs.setMinimumSize(150, 20)

        self.PlayerInfo = PlayerInformation(self.data, self.tabs)
        self.PlayerInfo.move(30, 50)
        self.tabs.addTab(self.PlayerInfo, 'Info')

        self.Stats = StatsBlock(self.data, self.tabs)
        self.Stats.move(30, 50) 
        self.tabs.addTab(self.Stats, "Stats")

        self.Skills = SkillsBlock(self.data, self.tabs)
        self.Skills.move(30, 50)
        self.tabs.addTab(self.Skills, "Skills")


        self.Items = ItemsBlock(self.data, self)
        self.Items.move(30, 50)
        self.tabs.addTab(self.Items, "Items")
        #self.setGeometry(300, 250, 250, 150)
        #self.show()
        #self.tabs.show()
         

    #Needs an on close function for pickling the data file
