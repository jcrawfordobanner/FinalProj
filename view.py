#Draws the model onto the view screen

import pygame

class PygameWindowView(object):
    """Draws the model"""
    def __init__(self, model, width = 640,height = 480):
        pygame.init()
        size = (width,height)
        pygame.display.init()
        self.screen = pygame.display.set_mode(size)
        self.model = model

    def draw(self):
        self.model.draw(self.screen)
        pygame.display.update()
