import pygame
from pygame.locals import *
import time

#from model import *
#from view import *
#from control import *
from classes import *

#Draws the model onto the view screen

#import pygame ----

class PygameWindowView(object):
    def __init__(self, model, size):
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode(size)
        self.model = model

    def draw(self):
        self.model.room.draw(self.screen)
        self.model.textbox.draw(self.screen)
        pygame.display.update()

#Keeps track of all of the variables being changed in each scene
#from classes import * -------
#from narrative import * -------
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
                'scene2':('You pressed the green button', 'Unfortunately nothing happened. You stay until you die of thirst', 'Game Over'),
                "scene3":('You pressed the blue button', 'Congratulations...you suck', 'Game Over'),
                'game_intro': ('You have awoke inside of a room.', 'In it you see three buttons, one red, one blue and one green.', 'What do you do?', 'j: red k: blue l: green')}
 # dictionary of all possible messages to be displayed on the textbox
        self.textbox= Textbox(size, self.messages['game_intro'])

    def update(self, pos, words=None):
        """Changes the model based upon new information"""
        #TODO work on the update process

        if words:
            self.textbox.update(words)
        for room in self.allrooms:
            self.allrooms[room].update(pos) #might be repeating the same process
        for item in self.room.items:
            if item.hidd and item.take:
                self.inventory.add_item(item)


#Dictates how the player can interact with the model
#from model import * -------


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
                self.model.textbox.update(self.model.messages['scene1'])
                self.model.eventflags['1']=False
                self.model.eventflags['2']=True
            if event.key == pygame.K_k:
                self.model.eventflags['1']=False
                self.model.textbox.update(self.model.messages['scene2'])
            if event.key == pygame.K_l:
                self.model.textbox.update(self.model.messages['scene3'])
                self.model.eventflags['1']=False
            return

        if self.model.eventflags.get('2')==True:
            self.model.textbox.update(self.model.messages['game_intro'])
            if event.key == pygame.K_j:
                self.model.textbox.update(self.model.messages['scene1'])
                self.model.eventflags['1']=False
                self.model.eventflags['2']=True
            if event.key == pygame.K_k:
                self.model.eventflags['1']=False
                self.model.textbox.update(self.model.messages['scene2'])
            if event.key == pygame.K_l:
                self.model.textbox.update(self.model.messages['scene3'])
                self.model.eventflags['1']=False
            return


if __name__ == '__main__':
    pygame.init()
    size = (1200, 1000)
    wrench = Item("wrench.png", (200,200), .75)
    stock = Backdrop("Hallway1.PNG", size)
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
