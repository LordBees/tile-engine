##primary modules
import os,sys,random,pygame
import MEGA
##aux modules
##settings for game(framerate ect)
import GAME_SETUP

##data objects relavent to game(in this code atleast)
#import Class_Player,Class_tiles
import Class_Player as player##player
import Class_maphandler##manages map data 

##inits
Running = True
##config variables##
arrowmap = [0]*4
##defines##
disp_res = GAME_SETUP.resolution
G_title = GAME_SETUP.title
TARG_FPS = GAME_SETUP.framerate##will remove this later
cwd = os.getcwd()
##paths##
PATH_TILEPATH = 'Data//tiles//'
PATH_MAPS = 'Data//maps//'
##pygame initialisation##
pygame.init()

gameDisplay = pygame.display.set_mode(disp_res)
pygame.display.set_caption(G_title)
clock = pygame.time.Clock()
##base init
player = player.Player()

##loop functions
def preload():
    pass

def blit_tiles():
    pass
    #for columns in tile_D:
    #    for items in range(len(columns)):
    #        gameDisplay.blit(columns[items][0],columns[items][1])

def blit_statics():
    pass
def blit_player():
   ##draw player if need
    if player.visible  == False:
        print('invisible')
    else:
        framex = 0
        if arrowmap[0] == 1:
            framex = 2
            player.move(-player.speed/GAME_SETUP.framerate,0)##tied to framerate
        elif arrowmap[1] == 1:
            framex = 3
            player.move(player.speed/GAME_SETUP.framerate,0)
        elif arrowmap[2] == 1:
            framex = 0
            player.move(0,-player.speed/GAME_SETUP.framerate)
        elif arrowmap[3] == 1:
            framex = 1
            player.move(0,player.speed/GAME_SETUP.framerate)
        else:##else framex = still frame
            framex = 4

        if player.animated:
            pass
            #pygame.blit()
        else:
            gameDisplay.blit(player.frames[framex][0],player.getpos())

def collision_check():
    pass

def blit_frame():##blit order
    blit_tiles()
    blit_statics()
    blit_player()
    collision_check()
        
###GAME     CODE###
preload()
startingmap = 'map1'
currentmap_data = Class_maphandler.maphandler(startingmap)
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        ############################
        #########KEY EVENTS#########
        ############################
        if event.type == pygame.KEYDOWN: #for key pressed events(not depress)
            if event.key == pygame.K_LEFT:
                arrowmap[0] = 1
            elif event.key == pygame.K_RIGHT:
                arrowmap[1] = 1
            elif event.key == pygame.K_UP:
                arrowmap[2] = 1
            elif event.key == pygame.K_DOWN:
                arrowmap[3] = 1
            
        if event.type == pygame.KEYUP:##for key depress events
            if event.key == pygame.K_LEFT:
                arrowmap[0] = 0
            elif event.key == pygame.K_RIGHT:
                arrowmap[1] = 0
            elif event.key == pygame.K_UP:
                arrowmap[2] = 0
            elif event.key == pygame.K_DOWN:
                arrowmap[3] = 0
            elif event.key == pygame.K_ESCAPE:##escapes and closes
                Running = False
        ##game events
                
        ##end game events
    gameDisplay.fill((255,255,255))##fill screen to prevent HOM
    print(arrowmap)
    blit_frame()
    #game_loop(leveldata_tiles)
        ############################
        ############################
        ############################
    #print('f')
    #gameDisplay.fill((255,255,255))
    
    pygame.display.update()
    clock.tick(TARG_FPS)
###END GAME CODE###
pygame.quit()



