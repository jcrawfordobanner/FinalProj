import pygame
from pygame.locals import *
import time

from model import *
from view import *
from control import *
from classes import *
import narrative

def mainz():
    size = (1152,864+36) #(2048, 1536)
    Scl = 1152/2048
    unlock = Item('unlock', (650, 500),0.75,'special.png')
    wrench = Item("wrench", (200,200), Scl,"wrench.png", True)
    redB2 = Item('scene1', (550, 500), Scl, 'Rbutton1.PNG')
    greenB1 = Item("greenB1", (600, 500), Scl, "Gbutton1.PNG")
    blueB1 = Item('blueB1', (650, 500), Scl, 'Bbutton1.PNG')
    box1 = Item('box1', (950, 300), Scl, 'Box01.PNG')
    box2 = Item('box2', (600, 200), Scl, 'Box02.PNG')
    neato = Item('neato', (550, 450), Scl, 'Neato.PNG' )
    bugbag = Item('bugbag', (500, 200), Scl, 'InsectProt.PNG')
    prangle = Item('prangle', (660, 65), Scl, 'Prangle.PNG', True)
    bluebin = Item('bluebin', (800, 140), Scl, 'BlueBin.PNG')
    #doors
    redB1 = Item('scene1', (550, 500), Scl, 'Rbutton1.PNG')
    tohall = Item('halldo',(350,600), Scl)
    tostor = Item('stordo',(550,520), Scl)
    tocock = Item('cockdo',(750,300), Scl)
    tocomm = Item('commdo',(400,300), Scl)
    toobs = Item('obsdo',(600,300), Scl)
    toair = Item('airdo',(500,100),.1)
    totank = Item('tankdo',(600,700),.75)

    hall1 = Room([wrench, tostor,redB1,tocomm], Backdrop("Hallway1.PNG", size))
    startRoom = Room([greenB1, redB1, blueB1], Backdrop("StartRm.jpg", size))
    bridge = Room([greenB1, redB2, blueB1, tohall, tocock,unlock], Backdrop("Bridge.PNG", size))
    StorRm = Room([box1, box2, neato, bluebin, bugbag, prangle,tohall], Backdrop('StorRoom.PNG', size))
    cockpit = Room([redB1],Backdrop("cock.jpg",size))
    obser = Room([tocomm],Backdrop("obby.jpg", size))
    comms = Room([tohall,toobs],Backdrop("comm.jpg", size))
    oxytank = Room([tostor], Backdrop("tank.jpg", size))
    airlock = Room([tostor], Backdrop("lcok.jpg", size))

    rooms = {"hallway":hall1, 'startRoom':startRoom, 'bridge':bridge, 'storage':StorRm, "cockpit":cockpit,"commroom":comms,"observation":obser,"tank":oxytank,"lock":airlock}
    doors ={"scene1":"bridge","halldo":"hallway","stordo":"storage","cockdo":"cockpit","commdo":"commroom","obsdo":"observation","airdo":"lock","tankdo":"tank"}
    puzzles ={"unlock":"wrench"}

    Modl = SpaceGameModel(size, rooms, doors,puzzles)


    return Modl

if __name__ == '__main__':
    def main_loop():
        size = (1152,864+36) #(2048, 1536)
        pygame.init()
        running = True
        gameover=False
        while running:
            pygame.display.init()
            Modl=mainz()
            SCRNtemp = PygameWindowView(Modl,size)
            Contrl = MouseController(Modl)
            while not gameover:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running=False
                    Contrl.handle_event(event)
                time.sleep(1/8)
                SCRNtemp.draw()
                print(Modl.choices)
                if Modl.choices>=20:
                    gameover=True
            time.sleep(1/8)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key==K_SPACE:
                        gameover=False
                    if event.type == pygame.QUIT:
                        running=False
        pygame.quit()

    main_loop()
