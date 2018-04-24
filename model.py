#Keeps track of all of the variables being changed in each scene
from classes import *

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
