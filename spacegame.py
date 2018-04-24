import pygame
from pygame.locals import *
import time

from model import *
from view import *
from control import *
from classes import *

if __name__ == '__main__':
    pygame.init()
    size = (1200, 1000)
    wrench = Item("wrench.png", (200,200), .75)
    stock = Backdrop("Hallway1.PNG", size)
    #
    # messages = {"intro":('You are now in the bridge', 'There is a paper clip and toothbrush and stapler', 'j:paper clip k:toothbrush l:stapler'), "scene1":('You pressed the red button', 'A door opens to your right'),
    #         "scene3":('You pressed the blue button', 'Congratulations...you suck', 'Game Over')}
    rooms = {'bridge':Room([wrench], stock)}

    Modl = SpaceGameModel(size, rooms)
    SCRNtemp = PygameWindowView(Modl,size)
    Contrl = MouseController(Modl)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        Contrl.handle_event(event,SCRNtemp)
        SCRNtemp.draw()
        time.sleep(.1)
        #Modl.update('SHIT ROCK UGH')


    pygame.quit()
