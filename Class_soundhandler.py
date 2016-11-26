##handles bgm and sfx
##imports
import pygame
import os
class Audio_common:
    #inits
    pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
    pygame.init()                      #initialize pygame
    ##paths
    BGMpath = 'Data\\snd\\MUS\\'##flipped slashes
    SFXpath = 'Data\\snd\\'

class MUShandler(Audio_common):

    ##vars
    BGM_NAME = ''
    ## inits
    MUS_BGM = pygame.mixer.music
   

    def __init__ (self):
        pass
    def get_loaded(self):
        return self.BGM_NAME
    
    def LoadMUS(self,mDAT):
        #self.Music_FLAG = True
        #self.LoadedSound = mixer.music
        #print(os.listdir(self.BGMpath))
        self.MUS_BGM.load(self.BGMpath+str(mDAT))
        self.BGM_NAME = str(mDAT)

    def PlayMUS(self,TIMES= -1):
        if self.MUS_BGM == None:# or self.Music_FLAG == False:
            print('track MUS is None!')
        else:
            self.MUS_BGM.play(TIMES)
    def StopMUS(self):
        if self.MUS_BGM == None:# or self.Music_FLAG == False:
            print('track MUS is None!')
        else:
            self.MUS_BGM.stop()
    def PausMUS(self):
        if self.MUS_BGM == None:# or self.Music_FLAG == False:
            print('track MUS is None!')
        else:
            self.MUS_BGM.pause()
    def UpausMUS(self):
        if self.MUS_BGM == None:# or self.Music_FLAG == False:
            print('track MUS is None!')
        else:
            self.MUS_BGM.unpause()

class SFX_handler(Audio_common):
    ##defs
    SFX_CHANNELS = 16
    ##vars
    SFX_NAMES = ['']*SFX_CHANNELS
    ## inits
    SFX_BOARD = [pygame.mixer.Sound]*SFX_CHANNELS #channels

    def __init__(self):
        pass
    
    ##pygame mixer
    def LoadSND(self,sDAT,channel):
        #self.Music_FLAG = False
        #self.LoadedSound = mixer.Sound(self.SFXpath+str(sDAT))
        if channel > self.SFX_CHANNELS:
            pass
        else:
            #self.SFX_BOARD[channel].load(self.BGMpath+str(mDAT))
            self.SFX_BOARD[channel] = pygame.mixer.Sound(self.SFXpath+str(sDAT))
            self.SFX_NAMES[channel] = str(sDAT)

    def PlaySND(self,channel):
        if self.SFX_BOARD[channel] == None:# or self.Music_FLAG == True:##should really be name not sfx obj
            pass
        else:
            #mixer.Sound.play(self.LoadedSound)
            self.SFX_BOARD[channel].play()

    def StopSND(self,channel):
        if self.SFX_BOARD[channel] == None or channel > self.SFX_CHANNELS:# or self.Music_FLAG == True:
            pass
        else:
            #mixer.Sound.stop()
            #self.LoadedSound.stop()
            self.SFX_BOARD[channel].stop()