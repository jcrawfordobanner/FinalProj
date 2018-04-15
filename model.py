#Keeps track of all of the variables being changed in each scene

from classes import *


class SpaceGameModel(object):
    """Model of the game"""
    def __init__(self, rooms):
        self.allrooms = rooms
        self.room = self.allrooms["bridge"]
        self.inventory = Inventory()
        self.textbox=Textbox(640,480/4)

    def draw(self, scrn):
        self.room.draw(scrn)
        self.textbox.draw(scrn)

    def update(self,words='hoi'):
        """Changes the model based upon new information"""
        #for r in self.allrooms:
            #r.update()
        self.textbox.update(words)
        for room in self.rooms:
            room.update()
        self.inventory.update()
