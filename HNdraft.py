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



class Scene(pygame.sprite.LayeredUpdates):
    def __init__(self):
        pygame.sprite.LayeredUpdates.__init__(self)
        self.backgrounds = []
        self.messages = []
        self.items = pygame.sprite.Group()
        self.curren_disp = pygame.sprite.Group

    def draw(self):
        self.
        self.messages.draw()
        self.items.draw()

    def update(self, click_pos):
        for item in self.items.sprites():
            item.update(click_pos)
        pygame.sprite.Group.

class GameModel(object):
    def __init__(self):
        self.scenes = []
        self.inventory = Inventory()


class PygameWindowView(object):
    def __init__(self,model,width,height):
        self.model = model
        size = (width,height)
        self.model.screen = pygame.display.set_mode(size)
