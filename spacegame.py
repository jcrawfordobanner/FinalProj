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
    unlock = Item('unlock', (700, 500),Scl)
    wrench = Item("wrench", (200,200), Scl,"Wrench.PNG", True)
    redB2 = Item('scene1', (550, 500), Scl, 'Rbutton1.PNG')
    greenB1 = Item("greenB1", (600, 500), Scl, "Gbutton1.PNG")
    blueB1 = Item('blueB1', (650, 500), Scl, 'Bbutton1.PNG')
    box1 = Item('box1', (970, 500), Scl, 'Box01.PNG')
    box2 = Item('box2', (600, 200), Scl, 'Box02.PNG')
    neato = Item('neato', (550, 450), Scl, 'Neato.PNG' )
    bugbag = Item('bugbag', (500, 200), Scl, 'InsectProt.PNG')
    prangle = Item('prangle', (460, 65), Scl, 'Prangle.PNG', True)
    bluebin = Item('bluebin', (780, 310), Scl, 'BlueBin.PNG')
    hdrive = Item('drive', (500, 400), Scl, 'HardDrive.PNG', True)
    telescope = Item('tele', (400, 300), Scl, "Telescope.PNG")
    #doors
    redB1 = Item('scene1', (550, 500), Scl, 'Rbutton1.PNG')
    tobrid = Item('brido', (1050, 250), Scl)
    p_tobrid = Item('Ptobrid', (350, 600), Scl)
    b_tohall = Item('Btohall', (330, 600), Scl)
    c_tohall = Item('Ctohall', (0, 350), 1)
    tohall = Item('halldo',(250,520), .85)
    h_tostor = Item('Hstordo',(550,520), Scl)
    tostor = Item('stordo', (10, 250), 1.1)
    tocock = Item('cockdo',(750,300), Scl)
    tocomm = Item('commdo',(550,250), Scl)
    o_tocomm = Item('Otocomm', (1050, 600),Scl)
    toobs = Item('obsdo',(250,0), .8)
    toair = Item('airdo',(1070,330),Scl)
    totank = Item('tankdo',(800,100),Scl)

    hall1 = Room([wrench, h_tostor,tocomm, tobrid], Backdrop("Hallway1.PNG", size))
    startRoom = Room([greenB1, redB1, blueB1], Backdrop("StartRm.jpg", size))
    bridge = Room([greenB1, redB2, blueB1, b_tohall, tocock], Backdrop("Bridge.PNG", size))
    StorRm = Room([box1, box2, neato, bluebin, bugbag, prangle,tohall, toair, totank], Backdrop('StorRoom.PNG', size))
    cockpit = Room([p_tobrid],Backdrop("PilotBay.PNG",size))
    obser = Room([o_tocomm, telescope],Backdrop("Observator.PNG", size))
    comms = Room([c_tohall,toobs, hdrive],Backdrop("CommsRoom.PNG", size))
    oxytank = Room([tostor, unlock], Backdrop("O2tank.PNG", size))
    airlock = Room([tostor], Backdrop("Airlock.PNG", size))

    rooms = {"hallway":hall1, 'startRoom':startRoom, 'bridge':bridge, 'storage':StorRm, "cockpit":cockpit,"commroom":comms,"observation":obser,"tank":oxytank,"lock":airlock}
    doors ={'brido':'bridge', "scene1":"bridge","halldo":"hallway", "stordo":"storage", "Hstordo":"storage","cockdo":"cockpit", 'Btohall':"hallway",
            "commdo":"commroom","obsdo":"observation","airdo":"lock","tankdo":"tank", "Ptobrid":"bridge", 'Otocomm':'commroom', 'Ctohall':'hallway'}
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
                if Modl.choices>=50:
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
