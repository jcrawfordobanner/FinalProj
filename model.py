#Keeps track of all of the variables being changed in each scene
from classes import *
import narrative
class SpaceGameModel(object):
    """Model of the game"""
    def __init__(self, size, rooms):
        self.allrooms = rooms #dictionary of all rooms
        self.room = self.allrooms["bridge"]
        self.inventory = Inventory()
        self.eventflags = {'1':True,'2':False,'3':False,'4':False,'5':False}
        self.messages = narrative.messages
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
