import os,sys
import MEGA,GAME_SETUP
import BeeLibv3 as Blib
import Class_Tiles, Class_soundhandler

class maphandler:
    ##paths
    mpath = 'Data//maps//'
    BGMpath = 'Data//snd//MUS//'
    ##data
    data_mega = None
    tiledata = []##tile objects
    collisiondata  = []##tile collsion data(nimplemented yet)
    staticsdata = []##static coord table##nimp
    tilesxdat = [Class_Tiles.BLANK(),Class_Tiles.DIRT_01(),Class_Tiles.DIRT_02(),Class_Tiles.GRASS_01(),Class_Tiles.WATR_02()]
    tilesxunknown = Class_Tiles.UNKNOWN()
    soundhandler_BGM = Class_soundhandler.MUShandler()##music backing
    ##vars
    name = ''##file name
    dispname = ''## display name
    bgmmusic = ''##music to go with map
    bgm_on = True ##mutes when false
    def __init__(self,mapfile):
        self.clear()
        ##cpyd from  mega
        if mapfile[-5:].upper() == '.MEGA':
            print('is')
        else:
            mapfile+='.MEGA'
        ##

        if os.path.isfile(self.mpath+mapfile):
            self.name = mapfile
            
            self.data_mega = MEGA.mega2(self.mpath+mapfile)
            ##processing
            self.mega_process()
            self.process_collision()
        else:
            print('LOG /maphandler- no file specified or bad file given')
            print('________________ file given - '+str(self.mpath+mapfile))
    def clear(self):##wipes buffers
        self.tiledata = []
        self.collisiondata  = []
        self.staticsdata = []

    def mega_process(self):##processes data from mega 
        files = self.data_mega.peek()
        data = []

        if 'META.txt' in files:##configs for map
            data = self.data_mega.fetch('META.txt')
            for x in range(len(data)):
                item = data[x].split(' = ')
                if item[0] == 'MUS':##split into variable and argument
                    self.bgmmusic = item[1]
                    self.soundhandler_BGM.LoadMUS(item[1])
                #if item[0] == '':
                    #pass
            data = []##clear data@end


        if 'map_T.txt' in files:##assigns tiles to texture slots
            data = self.data_mega.fetch('map_T.txt')

            for x in range(len(data)):##csving dat
                data[x] = Blib.csv2array(data[x])
            #input(data)
            next = ''
            for x in range(len(data)):
                temp = []
                #input(len(data[x]))
                for y in range(len(data[x])):
                    next = str(data[x][y])
                    ##tile assigning
                    #input(next)
                    print(next)
                    if str(next) == '0': #int(next) == 0:##could replace with loading all tex then checking against id
                        temp.append(self.tilesxdat[0])#Class_Tiles.BLANK())
                    elif str(next) == '1':#int(next) == 1:
                        temp.append(self.tilesxdat[1])#Class_Tiles.DIRT_01())
                    elif str(next) == '2':#int(next) == 2:
                        temp.append(self.tilesxdat[2])#Class_Tiles.DIRT_02())
                    elif str(next) == '3':#int(next) == 3:
                        temp.append(self.tilesxdat[3])#Class_Tiles.GRASS_01())
                    elif str(next) == '4':#int(next) == 4:
                        temp.append(self.tilesxdat[4])#Class_Tiles.WATR_02()

                    else:
                        #input(next)
                        temp.append(self.tilesxunknown)#Class_Tiles.UNKNOWN())
                    if temp[y].loaded == True:##can remove this when shifted 2 init in tiles
                        pass
                    else:
                        temp[y].loadme()
                    

                self.tiledata.append(temp)
                print('array out after conversion')
                print(temp)
                #input()
                temp = []
            data = []


        if 'map_C.txt' in files:##redundant now(will put in as override) later
            data = self.data_mega.fetch('map_C.txt')##same format as map_T for convienience

            for x in range(len(data)):##csving dat
                data[x] = Blib.csv2array(data[x])

            for x in range(len(data)):##overrides collision data for class instances
                for y in range(len(data[x])):
                    if int(data[x][y]) == 1:
                        self.tiledata[x][y].blocking = True
                    elif int(data[x][y]) == 0:
                         self.tiledata[x][y].blocking = False

            #data = []
        else:##process collision from tile class instead(already set so we do nothing)
            pass


        if 'dat_E.txt' in files:## entity placement
            data = self.data_mega.fetch('dat_E.txt')

            for x in data:
                pass

            data = []

    def process_collision(self):##processes collision data if not already populated
        if len(self.collisiondata) == 0:
            pass## do data
        else:
            print('LOG /maphandler- skipped collision gen as len != 0')
    ##mus/snd stuff
    ##mus
    def PP_BGM(self,trueorfalse):##playpause bgm
        if trueorfalse:
            pass
            #soundhandler_BGM.
        else:
            pass

    def PS_BGM(self,trueorfalse):##playstop
        if trueorfalse:
            self.soundhandler_BGM.PlayMUS()
        else:
            self.soundhandler_BGM.StopMUS()

    ##snd
