class SpaceGameModel(object):
    """Model of the game"""
    def __init__(self, size, rooms):
        self.allrooms = rooms #dictionary of all rooms
        self.room = self.allrooms["startRoom"]
        self.inventory = Inventory()
        self.eventflags = {'1':True,'2':False,'3':False,'4':False,'5':False}
        self.messages = narrative.messages
        self.textbox= Textbox(size, self.messages['game_intro'])


    def draw(self, scrn):
        self.room.draw(scrn)
        self.textbox.draw(scrn)

    def get_clicked(self, pos):
        for item in self.room.items:
            clicked_item = item.click(pos)
        return clicked_item

    def update(self, pos, words=None):
        """Changes the model based upon new information"""

        if words:
            self.textbox.update(words)
        for key in self.allrooms:
            self.allrooms[key].update(pos)
        for item in self.room.items:
            if item.hidd and item.take:
                self.inventory.add_item(item)
