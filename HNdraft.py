"Hadleigh's working doc"

import pygame
from pygame.locals import*
import time


class Backdrop(object):
    def __init__(self, image_name, size):

        im = pygame.image.load(image_name)
        self.size = (size[0], int(size[1]*4/5))
        self.image = pygame.transform.scale(im, self.size)
        self.rect = self.image.get_rect()

    def draw(self, scrn, loc = (0,0)):
        scrn.blit(self.image, loc)


class Textbox(pygame.Surface):
    """Changed so that it now takes text argument as a tuple,
    to make printing lines on the same thing easier"""

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, size, text):
        pygame.Surface.__init__(self,size)
        pygame.sprite.Sprite.__init__(self)
        self.width = size[0]
        self.height = size[1]/5
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.imageout = pygame.Surface((self.width,self.height))
        self.imageout.fill((0, 50, 60))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rectout = self.imageout.get_rect()
        self.rectout.x=0
        self.rectout.y= size[1]- self.height

        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.imagein = pygame.Surface((self.width*0.9,self.height*0.75))
        self.imagein.fill((250,255,255))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rectin = self.imagein.get_rect()
        self.rectin.x=  int((self.width - self.width*0.9)/2)
        self.rectin.y= size[1]-self.height +  int((self.height-self.height*0.75)/2)

        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 28)
        self.text = text

    def draw(self, screen):
        screen.blit(self.imageout, (0, self.rectout.y))
        self.imagein.fill((250,255,255))
        if isinstance(self.text, tuple):
            loc_y = 0
            for line in self.text:
                self.textsurface = self.font.render(line, False,(0,0,0))
                self.imagein.blit(self.textsurface,(0,loc_y))
                loc_y += 20
        elif isinstance(self.text, str):
            self.textsurface = self.font.render(self.text, False,(0,0,0))
            self.imagein.blit(self.textsurface,(0,0))
        screen.blit(self.imagein, (self.rectin.x,self.rectin.y))

    def update(self, words):
        self.text = words


class Item(pygame.sprite.Sprite):
    def __init__(self, img, loc, scl = 1):
        pygame.sprite.Sprite.__init__(self)
        self.image= ratio_scale(img, scl)
        self.Rect = pygame.Rect(self.image.get_rect()).move(loc)
        self.loc = loc
        self.hidd= False
        self.take = True

    def draw(self, scrn):
        scrn.blit(self.image, self.loc)

    def click(self,pos):
        if pygame.Rect(self.Rect).collidepoint( pos[0], pos[1]):
            return True
        else:
            return False

    def update(self, pos):
        if self.click(pos):
            if self.take:
                self.hidd = True


class Inventory(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.takeable_items = []
        self.items = []
    def add_item(self, item):
        self.items.append(item)
        self.add(item)

class Room(pygame.sprite.LayeredUpdates):
    def __init__(self, items, backdrops):
        pygame.sprite.LayeredUpdates.__init__(self)

        self.items = []
        for item in items:
            self.add(item)
            self.items.append(item)
        self.backdrop = backdrops
        self.items_vis = []
        for item in self.items:
            if not item.hidd:
                self.items_vis.append(item)

    def draw(self, scrn):
        self.backdrop.draw(scrn)
        for item in self.items_vis:
            item.draw(scrn)

    def update(self, pos):
        for item in self.items_vis:
            if item.click(pos):
                self.items_vis.remove(item)
            item.update(pos)


# class Narrative(object):
#     def __init__(self):
#         self.events = {'1':False,'2':False,'3':False,'4':False,'5':False}
#         # self.model=model
#         self.event_msgs = {"intro":('You are now in the bridge', 'There is a paper clip and toothbrush and stapler', 'j:paper clip k:toothbrush l:stapler'), "scene1":('You pressed the red button', 'A door opens to your right'),
#                 "scene3":('You pressed the blue button', 'Congratulations...you suck', 'Game Over')}


class SpaceGameModel(object):
    """Model of the game"""
    def __init__(self, size, rooms):
        self.allrooms = rooms #dictionary of all rooms
        self.room = self.allrooms["bridge"]
        self.inventory = Inventory()
        self.eventflags = {'1':True,'2':False,'3':False,'4':False,'5':False}
        self.messages = {"bridge_intro":('You are now in the bridge', 'There is a paper clip and toothbrush and stapler',
                'j:paper clip k:toothbrush l:stapler'),
                "scene1":('You pressed the red button', 'A door opens to your right'),
                "scene3":('You pressed the blue button', 'Congratulations...you suck', 'Game Over'),
                'game_intro': ('You have awoke inside of a room.', 'In it you see three buttons, one red, one blue and one green.', 'What do you do?', 'j: red k: blue l: green')}
 # dictionary of all possible messages to be displayed on the textbox
        self.textbox= Textbox(size, self.messages['game_intro'])


    def draw(self, scrn):
        self.room.draw(scrn)
        self.textbox.draw(scrn)

    def update(self, pos, words=None):
        """Changes the model based upon new information"""

        if words:
            self.textbox.update(words)
        for key in self.allrooms:
            self.allrooms[key].update(pos)
        for item in self.room.items:
            if item.hidd and item.take:
                self.inventory.add_item(item)

class PygameWindowView(object):
    def __init__(self, model, size):
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode(size)
        self.model = model

    def draw(self):
        self.model.draw(self.screen)
        pygame.display.update()


class MouseController(object):
    """ Handles input for space game """
    def __init__(self, model):
        self.model = model

    def handle_event(self, event):
        """ Event handler"""
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            self.model.update(pos)

        if event.type != KEYDOWN:
            return
        if self.model.eventflags.get('1')==True:
            self.model.textbox.update(self.model.messages['game_intro'])
            if event.key == pygame.K_j:
                self.model.eventflags['1']=False
                self.model.eventflags['2']=True
                self.model.textbox.update(self.model.messages['scene3'])
            if event.key == pygame.K_k:
                self.model.eventflags['1']=False
                self.model.textbox.update(self.model.messages['scene1'])
            # if event.key == pygame.K_l:
            #     self.model.textbox.update(self.model.messages['scene3'])
            #     self.model.events_key['1']=False
            return

        # elif story.events.get('2')==True:
        #     if event.key == pygame.K_j:
        #         story.scene4(self.model)
        #         story.events['2']=False
        #     if event.key == pygame.K_k:
        #         story.scene5(self.model)
        #         story.events['2']=False
        #     if event.key == pygame.K_l:
        #         story.scene6(self.model)
        #         story.events['2']=False
        #     return

def ratio_scale(filename, scl_factor):
    im = pygame.image.load(filename)
    orig_size = im.get_rect()
    image = pygame.transform.scale(im, (int(orig_size.w*scl_factor), int(orig_size.h*scl_factor)))
    return image

if __name__ == '__main__':
    pygame.init()
    size = (1200, 900)
    wrench = Item("wrench.png", (200,200), .75)
    stock = Backdrop("StockPhoto1.jpg", size)
    #
    # messages = {"intro":('You are now in the bridge', 'There is a paper clip and toothbrush and stapler', 'j:paper clip k:toothbrush l:stapler'), "scene1":('You pressed the red button', 'A door opens to your right'),
    #         "scene3":('You pressed the blue button', 'Congratulations...you suck', 'Game Over')}
    rooms = {'bridge':Room([wrench], stock)}

    Modl = SpaceGameModel(size, rooms)
    SCRNtemp = PygameWindowView(Modl,size)
    Contrl = MouseController(Modl)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        Contrl.handle_event(event)
        SCRNtemp.draw()
        time.sleep(.1)
        #Modl.update('SHIT ROCK UGH')


    pygame.quit()
