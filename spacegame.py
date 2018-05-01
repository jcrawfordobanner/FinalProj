import pygame
from pygame.locals import *
import time

from model import *
from view import *
from control import *
from classes import *
import narrative

if __name__ == '__main__':
    pygame.init()
    size = (1152,864+36) #(2048, 1536)
    wrench = Item("wrench","wrench.png", (200,200), .75, True)
    redB1 = Item('scene1', 'Rbutton1.PNG', (550, 500), .75)
    greenB1 = Item("greenB1", "Gbutton1.PNG", (600, 500), .75)
    blueB1 = Item('blueB1', 'Bbutton1.PNG', (650, 500), .75)
    hall1 = Backdrop("Hallway1.PNG", size)
    bridge = Room([greenB1, redB1, blueB1], Backdrop("Bridge.PNG", size))


    rooms = {"hallway":Room([wrench], hall1), 'startRoom':bridge}
    doors ={"scene1":"hallway"}

    Modl = SpaceGameModel(size, rooms, doors)
    SCRNtemp = PygameWindowView(Modl,size)
    Contrl = MouseController(Modl)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        Contrl.handle_event(event)
        SCRNtemp.draw()
        time.sleep(.05)
        #Modl.update('SHIT ROCK UGH')

    pygame.quit()
