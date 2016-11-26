import pygame
import GAME_SETUP
class Tile:
    ##
    tpath = 'Data\\tiles\\'##tile path
    dpath = 'static\\'##data path(specific tile data) if animated put folder of animated here as well
    ##positional
    ##frames
    #frames = [['BLANK.png'],['BLANK.png']]
    #framedelay = [[''],['']] ##in sec
    frames = ['UNUSEDC.png']
    framedelay = [''] # in seconds
    framedelay_watcher=0##seperate varaiable for tracking time to actually change(ticker)
    currframe = 0
    ##stats
    TILE_ID = 0
    TILE_UID = 0##flag for fancy things later

    ##flags
    PER_FRAME = False
    visible = True##draw me/not
    animated = False##animation in any movement state
    blocking = True
    loaded = False ##workaorund test for imporper loading

    def __init__(self):
        #for x in range(len(self.frames)):
            #for y in range(len(self.frames[x])):
                #break
                #print('x='+str(x)+'|'+str(y),self.tpath+self.dpath+str(self.frames[x][y]))
                #input('###')
                #self.frames[x][y] = pygame.image.load(self.tpath+self.dpath+self.frames[x][y])##replaced as currently no need for other ##EDIT: reenabled for mo to get working

        #print('preload images for this item:',len(self.frames),'\ncontent array:\n',self.frames,'\n[][]{}{}[][]')
        #for x in range(0,len(self.frames)):
            #print('item loading:'+str(self.frames[x]),'x='+str(x))
            #self.frames[x] = pygame.image.load(self.tpath+self.dpath+self.frames[x])
            #print('loaded:',self.frames[x],'as pygame surface')
        self.loadme()
        if self.animated and (not self.PER_FRAME):##converts to frames left if not displayed
             print('animconvert')
             #input()
            #for x in range(len(self.framedelay)):
            #    for y in range(len(self.framedelay[x])):
            #        self.framedelay[x][y] = (self.framedelay[x][y]*GAME_SETUP.framerate)##target frames = 60 atm will implement other way later
             for x in range(len(self.framedelay)):
                 self.framedelay[x] = (self.framedelay[x]*GAME_SETUP.framerate)##target frames = 60 atm will implement other way later

        self.static_Cinit()

    def static_Cinit(self): #custom initialisation for each tile if anything else nneds to be done
        pass

    def getfirstsurface(self):##returns first frame
        return self.frames[0]

    def loadme(self):##can move this back into init
        if self.loaded == True:
            pass
        else:
            print('preload images for this item:',len(self.frames),'\ncontent array:\n',self.frames,'\n[][]{}{}[][]')
            for x in range(0,len(self.frames)):
                print('len',str(len(self.frames)))
                print('item loading:'+str(self.frames[x]),'x='+str(x))
                self.frames[x] = pygame.image.load(self.tpath+self.dpath+self.frames[x])
                print('loaded:',self.frames[x],'as pygame surface')
            self.loaded = True

class BLANK(Tile):#intentionally blank
    ##
    ##positional
    ##frames
    frames = ['BLANK.png']#,['BLANK.png']]
    ##stats
    ##flags id0
    blocking = False

class UNKNOWN(Tile):## unknown tile id
    ##
    ##positional
    ##frames
    frames = ['UNUSED.png','BLANK.png']#,['UNUSED.png']]
    ##stats
    ##flags idx
    blocking = False

class DIRT_01(Tile):
    ##
    ##positional
    ##frames
    frames = ['DIRT_01.png']#,['BLANK.png']]
    ##stats
    ##flags id1
  

class DIRT_02(Tile):
    ##
    ##positional
    ##frames
    frames = ['DIRT_01_A.png']#,['BLANK.png']]
    ##stats
    ##flags id2
    #def static_Cinit(self):
    #input(self.frames)

class GRASS_01(Tile):
    ##
    ##positional
    ##frames
    frames = ['GRASS_01.png']#,['BLANK.png']]
    ##stats
    ##flags id3
 

class WATR_02(Tile):
    ##
    dpath = 'Anim\\WATR_02\\'
    ##positional
    ##frames
    frames = ['WATR_02_A.png','WATR_02_B.png']#,['WATR_02_B.png']]
    framedelay = [120,60]#,[0]]
    ##stats
    TILE_ID = 4
    ##flags
    animated = True
