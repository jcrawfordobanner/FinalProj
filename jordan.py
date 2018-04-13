import os, sys
import pygame
from pygame.locals import *
from helper import *

class Items(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
     def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(img,-1)


class Inventory(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.items = []
    def add_item(self, item):
        self.items.append(item)


class Characters(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
     def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(img,-1)

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


     def zewords(self,text):
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 28)
        self.textsurface = myfont.render(text, False,(0,0,0))
        self.imagein.blit(self.textsurface,(0,0))

class PyManMain:
    """The Main PyMan Class - This class handles the main
    initialization and creating of the Game."""

    def __init__(self, width=640,height=480):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width
                                               , self.height))

    def make_textbox(self):
        self.textbox=Textbox(self.width,self.height/4)
        self.screen.blit(self.textbox.imageout,(0,self.height-(self.height/4)))
        self.screen.blit(self.textbox.imagein,(30,int(self.height*0.75)+15))

    def update_textbox(self,words):
        self.make_textbox()
        self.textbox.zewords(words)
        self.screen.blit(self.textbox.imagein,(30,int(self.height*0.75)+15))

    #def event(key):
        #if key == K_l:


    def MainLoop(self):
        running = True
        self.make_textbox()
        pygame.display.update()
        self.update_textbox("You are in a room with two doors, a TV and a rubber duck.")
        pygame.display.update()
        pygame.time.wait(1000)
        self.update_textbox("Please choose one of the following:")
        pygame.display.update()
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                elif event.type == KEYDOWN:
                    if ((event.key == K_l)
                    or (event.key == K_k)
                    or (event.key == K_i)
                    or (event.key == K_j)):
                        self.event(event.key)


if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.MainLoop()
