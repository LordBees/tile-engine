##primary modules
import os,sys,random,pygame
import MEGA
import BeeLibv3 as Blib
##aux modules
##settings for game(framerate ect)
import GAME_SETUP

##data objects relavent to game(in this code atleast)
#import Class_Player,Class_tiles
import Class_Player as playerPawn##player
import Class_maphandler##manages map data 
import Class_soundhandler##for sfx class
#import Class_soundhandler #moved to maphandler(bgm bit atleast)
class gamemain:
    ##inits
    Running = True
    Paused = False
    ##config variables##
    arrowmap = [0]*4
    xoff = 0##render window offset
    yoff = 0
    scrollxborder = 25##how close to screen edge before scroll
    scrollyborder = 25
    ##defines##
    disp_res = GAME_SETUP.resolution
    G_title = GAME_SETUP.title
    TARG_FPS = GAME_SETUP.framerate##will remove this later
    cwd = os.getcwd()
    ##paths##
    PATH_TILEPATH = 'Data\\tiles\\'
    PATH_MAPS = 'Data\\maps\\'##changed slashes
    ##class init
    ##base init
    player = playerPawn.Player()
    #soundhandler_BGM = Class_soundhandler.MUShandler()##music backing
    #sfx
    soundhandler_SFX = Class_soundhandler.SFX_handler()##init class
    ##files
    currentmap_data = None
    F_options = None

    

    def __init__(self):
        ##pygame initialisation##
        pygame.init()

        self.gameDisplay = pygame.display.set_mode(self.disp_res)
        pygame.display.set_caption(self.G_title)
        self.clock = pygame.time.Clock()
        ##base init
        
        self.preload()
        self.mainloop()

    ##loop functions
    def preload(self):
        #debug overrides
        #startingmap = 'map1'#'map3'#'map2'#'map1'
        ##init
        self.F_options = MEGA.mega2('Data\\Configuration.MEGA')##init options
        smap = self.F_options.fetch('OPTIONS.txt')##get map options before map load
        #print(self.F_options.fetch('OPTIONS.txt'))
        #input(smap)
        self.currentmap_data = Class_maphandler.maphandler(smap[0].split(' = ')[1])#(startingmap)
        self.currentmap_data.PS_BGM(True)
        ##sfx setup
        self.soundhandler_SFX.LoadSND('HS_SE_000.wav',0)#testing
        #input('moop')

    def blit_tiles(self):
        #pass
        #for columns in tile_D:
        #    for items in range(len(columns)):
        #        gameDisplay.blit(columns[items][0],columns[items][1])
        tdat = self.currentmap_data.tiledata
        #print(tdat)
        #input('press to blit step')
        for columns in range(len(tdat)):
            for items in range(len(tdat[columns])):
                #print('][][][')
                #print(tdat[columns][items].getfirstsurface())
                #input('step@@@')
                if tdat[columns][items].animated == True:##if anim = True
                    if int(tdat[columns][items].framedelay_watcher) == int(tdat[columns][items].framedelay[tdat[columns][items].currframe]):
                        #input('equal')
                        if tdat[columns][items].currframe == len(tdat[columns][items].frames) - 1:##if frame =2 len of array, reset 
                            tdat[columns][items].currframe = 0
                        else:
                            tdat[columns][items].currframe = tdat[columns][items].currframe+1#else increment
                        tdat[columns][items].framedelay_watcher = 0

                    else:
                        tdat[columns][items].framedelay_watcher = tdat[columns][items].framedelay_watcher+ 1##watcher ++
                    #print(tdat[columns][items].framedelay_watcher)
                    self.gameDisplay.blit(tdat[columns][items].frames[tdat[columns][items].currframe],(columns*GAME_SETUP.tex_width,items*GAME_SETUP.tex_width))## render frame
                else:
                    self.gameDisplay.blit(tdat[columns][items].frames[0],(columns*GAME_SETUP.tex_width,items*GAME_SETUP.tex_width))## just render first frame

    def blit_statics(self):
        pass


    def blit_player(self):
       ##draw player if need
        if self.player.visible  == False:
            print('invisible')
        else:
            framex = 0
            if self.arrowmap[0] == 1:
                framex = 2
                self.player.move(-self.player.speed/GAME_SETUP.framerate,0)##tied to framerate
            elif self.arrowmap[1] == 1:
                framex = 3
                self.player.move(self.player.speed/GAME_SETUP.framerate,0)
            elif self.arrowmap[2] == 1:
                framex = 0
                self.player.move(0,-self.player.speed/GAME_SETUP.framerate)
            elif self.arrowmap[3] == 1:
                framex = 1
                self.player.move(0,self.player.speed/GAME_SETUP.framerate)
            else:##else framex = still frame
                framex = 4

            if self.player.animated:
                pass
                #pygame.blit()
            else:
                self.gameDisplay.blit(self.player.frames[framex][0],self.player.getpos())


    def collision_check(self):
        pass


    def blit_UI(self):
        pass

    def blit_frame(self):##blit order
        self.blit_tiles()
        self.blit_statics()
        self.blit_player()
        self.collision_check()
        self.blit_UI()
        
    
    #self.preload()
    def mainloop(self):
        ###GAME     CODE###
        
        while self.Running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True
                    self.running = False
                ############################
                #########KEY EVENTS#########
                ############################
                if event.type == pygame.KEYDOWN: #for key pressed events(not depress)
                    if event.key == pygame.K_LEFT:
                        self.arrowmap[0] = 1
                    elif event.key == pygame.K_RIGHT:
                        self.arrowmap[1] = 1
                    elif event.key == pygame.K_UP:
                        self.arrowmap[2] = 1
                    elif event.key == pygame.K_DOWN:
                        self.arrowmap[3] = 1
                    elif event.key == pygame.K_p:##pause event
                        self.Paused = not self.Paused
                        self.soundhandler_SFX.PlaySND(0)
                    elif event.key == pygame.K_o:
                        self.currentmap_data = Class_maphandler.maphandler('map4')
                        self.currentmap_data.PS_BGM(True)
 
            
                if event.type == pygame.KEYUP:##for key depress events
                    if event.key == pygame.K_LEFT:
                        self.arrowmap[0] = 0
                    elif event.key == pygame.K_RIGHT:
                        self.arrowmap[1] = 0
                    elif event.key == pygame.K_UP:
                        self.arrowmap[2] = 0
                    elif event.key == pygame.K_DOWN:
                        self.arrowmap[3] = 0
                    elif event.key == pygame.K_ESCAPE:##escapes and closes
                        self.Running = False
                ############################

                ##game events
                
                ##end game events

                ############################
                ############################
                ############################
            ##render
            self.gameDisplay.fill((255,255,255))##fill screen to prevent HOM
            #print(self.arrowmap)
            self.blit_frame()
            #game_loop(leveldata_tiles)
                
            #print('f')
            #gameDisplay.fill((255,255,255))
    
            pygame.display.update()
            self.clock.tick(self.TARG_FPS)
            ##end render
        ###END GAME CODE###
    pygame.quit()
gamemain()



