#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 02:45:08 2018

@author: riku
"""
from Utils import selectMyPlace,selectEnemyPlace

class card:
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost
    
    def fanfare(self,Field,PlayerID):
        print("fanfare pass")
        pass
    
    def lastWord(self,Field):
        print("fanfare pass")
        pass
    

class follower(card):
    def __init__(self,name,cost,AP,HP,EAP=2,EHP=2):
        card.__init__(self,name,cost)
        self.AP = AP
        self.HP = HP
        self.EAP = EAP
        self.EHP = EHP
        self.AttackFlag = 1
        self.EvolveFlag = 0
        self.cardType = "follower"
        
    def changeHP(self,plusHP):
        self.HP = self.HP + plusHP
        print(str(self.name) +"HP:" + str(self.HP))
        return self.HP
    
    def StandbyPhase(self,):
        self.AttackFlag = 0
    
    def evolution(self,Field,PlayerID):
        self.AP +=self.EAP
        self.HP +=self.EHP
        
class Amulet(card):
    def __init__(self,name,cost,count=None):
        card.__init__(self,name,cost)
        self.count = count
        self.cardType = "Amulet"
    
    def changeCount(self,plusCount):
        self.count = self.count + plusCount
        print(str(self.name) +"count:" + str(self.count))
        return self.count
    
    def StandbyPhase(self,):#オーバーライドして使う
        pass    

class Spell(card):
    def __init__(self,name,cost):
        card.__init__(self,name,cost)
        self.cardType = "Spell"
    
    def PlaySpell(self,Field,PlayerID):#オーバーライドして使う
        return True

class BubetuNoSinja(follower):
    def __init__(self,name="BubetuNoSinja",cost=1,AP=1,HP=1,):
        follower.__init__(self,name,cost,AP,HP)
        self.AP = AP
        self.HP = HP
        self.AttackFlag = 1
        self.cardType = "follower"
        
    def fanfare(self,Field,PlayerID):
        print("fanfare:"+str(self.name))
        if len(Field[PlayerID].place)>=2:
            SelectFieldID = selectMyPlace(Field,PlayerID,fanfareFlag=1)
            Field[PlayerID].place[SelectFieldID].changeHP(-1)
            Field[PlayerID].checkDestroy(SelectFieldID,Field)
            Field[PlayerID].draw(1)

class BubetuNoEnsou(Spell):
    def __init__(self,name="BubetuNoEnsou",cost=1):
        super().__init__(name,cost)
        self.cardType = "Spell"
        
    def PlaySpell(self,Field,PlayerID):
        if len(Field[PlayerID].place) == 0: return False
        if len(Field[1-PlayerID].place) == 0: return False
        
        SelectFieldID = selectMyPlace(Field,PlayerID,fanfareFlag=0)
        SelectEnemyFieldID = selectEnemyPlace(Field,PlayerID)
        Field[PlayerID].place[SelectFieldID].changeHP(-1)
        Field[PlayerID].checkDestroy(SelectFieldID,Field)
        Field[1-PlayerID].place[SelectEnemyFieldID].changeHP(-3)
        Field[1-PlayerID].checkDestroy(SelectEnemyFieldID,Field)
        return True
        
class Aira(follower):
    def __init__(self,name="Aira",cost=2,AP=2,HP=2,):
        follower.__init__(self,name,cost,AP,HP)
        self.AP = AP
        self.HP = HP
        self.AttackFlag = 1
        self.cardType = "follower"

    def evolution(self,Field,PlayerID):
        self.AP +=self.EAP
        self.HP +=self.EHP
        Field[PlayerID].MaxPP +=1
        
        
        #戦闘準備用
class BattleDeck:
    deck = []
    def __init__(self,deck):
        self.deck = deck
        
    def addCardToDeck(self,card):
        self.deck.append(card)
  
  
class makeCard:
    def makeFollower(self,name,cost,AP,HP):
        card = follower(name,cost,AP,HP)
        return card
        
class makeDeck:
    def makeDeck(self,cards):
        deck = []
        for i in range(40):
            deck.append(card)
        return deck      