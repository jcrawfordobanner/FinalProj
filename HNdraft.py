"Hadleigh's working doc"

import pygame
from pygame.locals import*
import time


class Backdrop(object):
    def __init__(self, image_loc, scrn):

        self.image = pygame.image.load(image_loc)
        self.rect = self.image.get_rect()

    def draw(self):
        self.image.blit(self.image, (0,0))
        #pygame.display.update()

class Background(pygame.Surface):
    # Constructor. Pass in the color of the block,
    # and its x and y position
     def __init__(self,img):
        self.image, self.rect = load_image(img,-1)

     def draw(self):
        pygame.display.update()

class Textbox(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect

    def zewords(self,text):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 28)
        textsurface = myfont.render(text)
        self.image.blit(textsurface)


class Item(pygame.sprite.Sprite):
    def __init__(self,img, loc, grp):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(img,-1)
        self.loc = loc
        self.clicked = False
        self.group = grp

    def draw(self):
        pygame.draw.rect(self.img, pygame.Rect(self.rect))


    def update(self, click_pos):
        if self.loc == click_pos:
            self.clicked = True
            self.remove()


class Character(pygame.sprite.Sprite):
    def __init__(self, loc):
        pygame.sprite.Sprite.__init__(self)

class Inventory(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)

        



class Room(pygame.sprite.LayeredUpdates):
    def __init__(self, msgs, items):
        pygame.sprite.LayeredUpdates.__init__(self)
        self.messages = msgs
        self.items = items

    def draw(self):
        self.messages.draw()
        self.items.draw()

    def update(self, click_pos):
        for item in self.items.sprites():
            item.update(click_pos)


class GameModel(object):
    def __init__(self):

        self.scenes = []
        self.inventory = Inventory()


class PygameWindowView(object):
    def __init__(self, backdrp ,width = 640,height = 480):
        size = (width,height)
        #pygame.display.init()
        self.screen = pygame.display.set_mode(size)
        self.backdrop = backdrp
    def draw(self):
        self.backdrop.draw()
        pygame.display.update()



class MouseController(object):
    def __init__(self, model):
        self.model = model

if __name__ == '__main__':
    pygame.init()
