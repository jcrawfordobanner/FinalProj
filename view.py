#Draws the model onto the view screen

import pygame

class PygameWindowView(object):
    def __init__(self, model, size):
        self.screen = pygame.display.set_mode(size)
        self.model = model

    def draw(self):
        self.model.draw(self.screen)
        pygame.display.update()
