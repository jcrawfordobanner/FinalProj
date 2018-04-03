import pygame
from pygame.locals import *
import time

if __name__ == '__main__':
    pygame.init()

    size = (640, 480)
    screen = pygame.display.set_mode(size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        time.sleep(.001)

    pygame.quit()
