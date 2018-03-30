"Hadleigh's working doc"

import pygame
from pygame.locals import*
import time


class Backdrop(pygame.Surface):
    def __init__(self, image):
        pygame.Surface.__init__()
        self.image = image

    def draw(self):
        self.blit(self.image)

class Item(pygame.sprite.Sprite):
    def __init__(self, loc):
        pygame.sprite.Sprite.__init__(self)

    def draw(self):

    def update(self):

class Character(pygame.sprite.Sprite):
    def __init__(self, loc):
        pygame.sprite.Sprite.__init__(self)

class Message(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Scene(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)


class GameModel(object):
    def __init__(self):
        self.scenes = []
        self.messages = []


class PygameWindowView(object):
    def __init__(self):
