class SpaceGameModel(object):
    def __init__(self, rooms):
        self.allrooms = rooms
        self.room = self.allrooms["bridge"]
        self.inventory = Inventory()
        self.textbox=Textbox(640,480/4)

    def draw(self, scrn):
        self.room.draw(scrn)
        self.textbox.draw(scrn)
