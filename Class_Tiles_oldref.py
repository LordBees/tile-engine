import pygame
class tile:
    datapath = 'DATA\\TILES\\'
    tileobj = ''
    valid_ext = ['png','jpg']
    def __init__(self,image,tid,params):
        self.image = image
        self.tid = tid
        self.params = params
        self.preload_setup()
    
    def set_flags(self):
        pass
    def get_tileimage(self):
        return self.image
    def get_tileid(self):
        return self.tid
    def get_params(self):
        return self.params
    def get_tileobj(self):
        return self.tileobj
    def preload_setup(self):
        self.tileobj = pygame.image.load(self.datapath+self.image)
class tile_DIRT01(tile):
    def __init__(self,image = 'DIRT_01.png',tid = '1',params = []):
        self.image = image
        self.tid = tid
        self.params = params
        self.preload_setup()
    
class tile_Dirt02(tile):
    def __init__(self,image= 'Dirt01_A.png',tid = '2',params = []):
        self.image = image
        self.tid = tid
        self.params = params
        self.preload_setup()
    

