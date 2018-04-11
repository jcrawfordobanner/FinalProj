"Hadleigh's working doc"

import pygame
from pygame.locals import*
import time


class Backdrop(object):
    def __init__(self, image_name):

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()

    def draw(self, scrn, loc = (0,0)):
        scrn.blit(self.image, loc)
        #pygame.display.update()

# class Background(pygame.Surface):
#     # Constructor. Pass in the color of the block,
#     # and its x and y position
#      def __init__(self,img):
#         self.image, self.rect = load_image(img,-1)
#
#      def draw(self):
#         pygame.display.update()

class Textbox(pygame.Surface):

    # Constructor. Pass in the color of the block,
    # and its x and y position
     def __init__(self,width,height):
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


class Item(pygame.sprite.Sprite):
    def __init__(self, img, loc):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load(img) #see if needs fixing
        self.rect = self.image.get_rect()
        self.loc = loc
        self.clicked = False

    def draw(self, scrn):
        scrn.blit(self.image, self.loc)


    def update(self, click_pos):
        if self.loc == click_pos:
            self.clicked = True

class Character(pygame.sprite.Sprite):
    def __init__(self, loc):
        pygame.sprite.Sprite.__init__(self)

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
        for i in range(len(items)):
            if items[i].clicked == False:
                self.items_vis.append(items[i])

    def draw(self, scrn):
        self.backdrop.draw(scrn)
        for item in self.items_vis:
            item.draw(scrn)

    def update(self, click_pos):
        for item in self.items.sprites():
            item.update(click_pos)


class SpaceGameModel(object):
    def __init__(self, rooms):
        self.allrooms = rooms
        self.room = self.allrooms["bridge"]
        self.inventory = Inventory()

    def draw(self, scrn):
        self.room.draw(scrn)

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

if __name__ == '__main__':
    pygame.init()
    running = True
    while running:
        kiwi = Item("Wrench.jpg", (0,0))
        stock = Backdrop("StockPhoto1.jpg")
        room =  Room({}, [kiwi], stock)
        rooms = {"bridge":room}
        Modl = SpaceGameModel(rooms)

        SCRNtemp = PygameWindowView(Modl)
        SCRNtemp.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
