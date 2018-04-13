import pygame
from pygame.locals import *
import time

from model import *
from view import *
from control import *
from classes import *

if __name__ == '__main__':
    pygame.init()
    running = True
    while running:
        wrench = Item("wrench.png", (200,200))
        wrench.image = pygame.transform.scale(wrench.image, (50, 60))
        stock = Backdrop("StockPhoto1.jpg", (640, 480))
        room =  Room({}, [wrench], stock)
        rooms = {"bridge":room}
        Modl = SpaceGameModel(rooms)

        SCRNtemp = PygameWindowView(Modl)
        SCRNtemp.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
