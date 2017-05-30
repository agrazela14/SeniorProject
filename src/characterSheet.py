#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we receive data from
a QInputDialog dialog. 

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
import random
import math 

from characterStats import *
from characterSkills import *

from PyQt5.QtWidgets import (QWidget, QWidgetItem, QDialog, QPushButton, QLineEdit, 
    QInputDialog, QApplication, QMessageBox)

from PyQt5.QtCore import (QSize)

class Attack():
    def __init__(self, name, light, diceNum, diceSides, reach, prof):
        this.name = name 
        this.light = light 
        this.diceNum = diceNum 
        this.diceSides = diceSides 
        this.reach = reach 
        this.prof = prof 

class Item():
    def __init__(self, name, quantity, wt):
        this.name = name
        this.quantity = quantity 
        this.wt = wt

class CharacterData():
    def __init__(self):
        self.playerName = "Player"
        self.characterName = "Character"
        self.characterClass = "Commoner"
        self.level = 1 
        self.exp = 0
        self.Alignment = "N"
        
        #Actually just do a list of "statInfo"s that can be indexed into in each charStat
        self.stats = [
            characterStats.statInfo("Strength", 10, False),
            characterStats.statInfo("Dexterity", 10, False),
            characterStats.statInfo("Constitution", 10, False),
            characterStats.statInfo("Intelligence", 10, False),
            characterStats.statInfo("Wisdom", 10, False),
            characterStats.statInfo("Charisma", 10, False)
        ]
        #do the same with skills
        #self.skills = characterSkills.skillBlock()
        self.skills = [
            characterSkills.skillInfo("Acrobatics", "Dexterity", False),
            characterSkills.skillInfo("Animal Handling", "Wisdom", False),
            characterSkills.skillInfo("Arcana", "Intelligence", False),
            characterSkills.skillInfo("Athletics", "Strength", False),
            characterSkills.skillInfo("Deception", "Charisma", False),
            characterSkills.skillInfo("History", "Intelligence", False),
            characterSkills.skillInfo("Insight", "Wisdom", False),
            characterSkills.skillInfo("Intimidation", "Charisma", False),
            characterSkills.skillInfo("Investigation", "Intelligence", False),
            characterSkills.skillInfo("Medicine", "Wisdom", False),
            characterSkills.skillInfo("Nature", "Intelligence", False),
            characterSkills.skillInfo("Perception", "Wisdom", False),
            characterSkills.skillInfo("Performance", "Charisma", False),
            characterSkills.skillInfo("Persuasion", "Charisma", False),
            characterSkills.skillInfo("Religion", "Intelligence", False),
            characterSkills.skillInfo("Sleight of Hand", "Dexterity", False),
            characterSkills.skillInfo("Stealth", "Dexterity", False),
            characterSkills.skillInfo("Survival", "Wisdom", False)
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
        self.proficiency = 0
        self.ac = 10
        self.initiative = 0
        self.moveSpeed = 30

        self.Attacks = [Attack("unarmed", True, 1, 4, 0, True]
        self.1stLevelSlots = 0
        self.2ndLevelSlots = 0
        self.3rdLevelSlots = 0
        self.4thLevelSlots = 0
        self.5thLevelSlots = 0
        self.6thLevelSlots = 0
        self.7thLevelSlots = 0
        self.8thLevelSlots = 0
        self.9thLevelSlots = 0
        
        self.spells = ["blank"]

        self.platinum = 0
        self.gold = 0
        self.silver = 0
        self.copper = 0
        self.items = ["Commoner's Clothes", 1, 3] 


class CharacterSheet(QWidget):
    def __init__(self, name, fo, new, parent):
        super().__init__()
        
        self.parent = parent
        self.fo = fo
        self.name = name
        self.initUI()

        if new:
            self.data = characterData(fo)

        else:
            self.data = pickle.load(fo)
        
    def initUI(self):      
        self.Stats = StatsBlock(fo, self.data, self)
        self.Stats.move(30, 50) 

        self.Skills = SkillsBlock(fo, self.data, self)
        self.Skills.move(30, 275)
         
        self.size = QSize(1000, 1000)
        self.resize(self.size)
        self.setWindowTitle('Input dialog')
        self.show()
