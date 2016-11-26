import pygame
import GAME_SETUP

class Player:
    ##
    tpath = 'Data\\tiles\\'
    dpath = 'player\\'
    ##positional
    x = 0
    y = 0
    ##inventory
    inventory = []
    maxinventory = 10
    ##stats
    health = 100
    health_MAX = 100
    speed = 250
    ##visualdata
    #frames = [['up'],['down'],['left'],['right'],['still'],]
    frames = [['UP.png'],['DN.png'],['LF.png'],['RT.png'],['BLANK.png']]
    framedelay=[[''],[''],[''],['']]
    PER_FRAME = False##per no of frames or delay in seconds
    visible = True##draw me/not
    animated = False##animation in any movement state
    ##collisiondata
    def __init__(self):
        for x in range(len(self.frames)):
            for y in range(len(self.frames[x])):
                self.frames[x][y] = pygame.image.load(self.tpath+self.dpath+self.frames[x][y])
    ##movement
    def move(self,additx,addity):##add x and y values to current
        self.x = self.x + additx
        self.y = self.y + addity

    def updatepos(self,newx,newy):
        self.x = newx
        self.y = newy

    def getpos(self):
        return(self.x,self.y)

    #inventory stuff
    def dropitem(self,itemid):
        for items in range(len(inventory)):
            if items == inventory[x][0]:
                pass ##drop code here (return position to drop(normally charpos) and itemid alsop remove from inv

    def pickupitem(self,itemid):
        if (self.maxinventory+1) > self.maxinventory:
            return False##cannot add item
    ## state and retrieval
    def isdead(self):
        if self.health <= 0 :
            return True
        else:
            return False
    #set variables
        #vis
    def set_visible(self,state):
        ##true/false
        self.visible = bool(state)
    ##interaction
    def damage(self,dam):
        self.health = self.health - dam
        if self.isdead():
            print('dead!')

    def heal(self,hp):
        self.health = self.health + hp
        if self.health > self.health_MAX:
            self.health = self.health_MAX
            
    def healthmodify(self,hp):##both combined
        self.health = self.health + hp
        if self.health > self.health_MAX:
            self.health = self.health_MAX
        if self.isdead():
            print('dead!')
        
    
         


