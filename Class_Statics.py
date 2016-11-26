import pygame


    ##
    ##positional
    ##frames
    ##stats
    ##flags

class static:
     ##
    tpath = 'Data\\tiles\\'
    dpath = 'statics\\'

    #positional
    x = 0
    y = 0

    ##frames
    frames = [['BLANKC.png'],['BLANKC.png']]
    framedelay = [[''],['']]

    ##stats
    health = 100
    ##flags
    destructible = False
    PER_FRAME = False
    visible = True##draw me/not
    animated = False##animation in any movement state
    blocking = True
    def __init__(self):
        for x in range(len(self.frames)):
            self.frames[x][y] = pygame.image.load(self.tpath+self.dpath+self.frames[x][y])

        self.static_Cinit()

    def static_Cinit(): #custom initialisation for each static if anything else nneds to be done
        pass

class plantpot(static):
    ##
    ##positional
    ##frames
    frames = []
    ##stats
    ##flags
    self.destructible = True
        
    
