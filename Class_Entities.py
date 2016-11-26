import pygame
class xplayer:
    ##positional
    x = 0
    y = 0
    ##inventory
    inventory = []
    maxinventory = 10
    ##stats
    health = 100
    ##visualdata
    frames = [['up'],['down'],['left'],['right']]
    framedelay=[[],[],[],[]]
    PER_FRAME = False##per no of frames or delay in seconds
    ##collisiondata
    def __init__(self):
        pass
    def move(self,additx,addity):##add x and y values to current
        pass
    def updatepos(self,newx,newy):
        pass
    
    def dropitem(self,itemid):
        for items in range(len(inventory)):
            if items == inventory[x][0]:
                pass ##drop code here (return position to drop(normally charpos) and itemid alsop remove from inv

    def pickupitem(self,itemid):
        if (self.maxinventory+1) > self.maxinventory:
            return False##cannot add item
    
         

