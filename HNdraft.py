"Hadleigh's working doc"

import pygame
from pygame.locals import*
import time


class Backdrop(object):
    def __init__(self, image_name, size):

        im = pygame.image.load(image_name)
        self.image = pygame.transform.scale(im, size)
        self.rect = self.image.get_rect()

    def draw(self, scrn, loc = (0,0)):
        scrn.blit(self.image, loc)


class Textbox(pygame.Surface):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, text, width,height):
        pygame.Surface.__init__(self,(width,height))
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.imageout = pygame.Surface((width,height))
        self.imageout.fill((255,0,0))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rectout = self.imageout.get_rect()
        self.rectout.x=0
        self.rectout.y=1000

        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.imagein = pygame.Surface((width*0.9,height*0.75))
        self.imagein.fill((0,255,0))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rectin = self.imagein.get_rect()
        self.rectin.x=0
        self.rectin.y=1000

        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 28)
        self.text = text
        self.textsurface = myfont.render(text, False,(0,0,0))
        self.imagein.blit(self.textsurface,(0,0))

    def draw(self, screen):
        sreen.blit(self.imageout, (0, screen.height-(screen.height/4)))
        sreen.blit(self.imagein, (30,int(screen.height*0.75)+15))

    def update(self, words):
        self.text = words


class Item(pygame.sprite.Sprite):
    def __init__(self, img, loc):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.move(loc)
        self.loc = loc
        self.hidd= False

    def draw(self, scrn):
        scrn.blit(self.image, self.loc)

    def update(self):
        pass # not sure if need to update this here



class Inventory(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.items = []
    def add_item(self, item):
        self.items.append(item)

class Room(pygame.sprite.LayeredUpdates):
    def __init__(self, msgs, items, backdrops):
        pygame.sprite.LayeredUpdates.__init__(self)
        self.messages = msgs
        self.items = items
        self.backdrop = backdrops
        self.items_vis = []
        for k in range(len(items)):
            if items[k].hidd == False:
                self.items_vis.append(items[k])

    def draw(self, scrn):
        self.backdrop.draw(scrn)
        for item in self.items_vis:
            item.draw(scrn)

    def update(self):
        for m in self.messages:
            m.update(words)


class Narrative(object):
    def __init__(self):
        self.events = {}


class SpaceGameModel(object):
    def __init__(self, rooms):
        self.allrooms = rooms
        self.room = self.allrooms["bridge"]
        self.inventory = Inventory()

    def draw(self, scrn):
        self.room.draw(scrn)

    def update(self, click_pos, click):
        for r in self.allrooms:
            r.update()



class PygameWindowView(object):
    def __init__(self, model, width = 640,height = 480):
        pygame.init()
        size = (width,height)
        pygame.display.init()
        self.screen = pygame.display.set_mode(size)
        self.model = model

    def draw(self):
        self.model.draw(self.screen)
        pygame.display.update()

class MouseController(object):
    def __init__(self, model):
        self.model = model


def ratio_scale(im, scl_factor):
    orig_size = im.get_rect()

if __name__ == '__main__':
    pygame.init()
    running = True
    while running:
        wrench = Item("wrench.png", (200,200))
        wrench.image = pygame.transform.scale(wrench.image, (50, 60))
        stock = Backdrop("StockPhoto1.jpg", (1000, 1000))
        room =  Room({}, [wrench], stock)
        rooms = {"bridge":room}
        Modl = SpaceGameModel(rooms)

        SCRNtemp = PygameWindowView(Modl)
        SCRNtemp.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
