import pygame
from pygame.locals import *
import time

class PygameWindowView(object):
    def __init__(self, model, size):
        self.model = model
        self.model.screen = pygame.display.set_mode(size)

    def draw(self):
        """Draw the current game state to the screen"""

class SpaceGameModel(object):
    def __init__(self, size):
        self.scenes = []
        self.inventory = Inventory()
        self.width = size[0]
        self.height = size[1]

    def update(self):
        """Update the game state"""


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

class PyGameController(object):
    """ Handles input for space game """
    def __init__(self,model):
        self.model = model

    def handle_event(self,event):
        """ Event handler"""
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_LEFT:
            #action
        if event.key == pygame.K_RIGHT:
            #action





if __name__ == '__main__':
    pygame.init()

    size = (640, 480)

    model = SpaceGameModel
    view = PyGameWindowView(model, size)
    controller = PyGameController(model)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            controller.handle_event(event)
        model.update()
        view.draw()
        time.sleep(.001)

    pygame.quit()
