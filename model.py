class SpaceGameModel(object):
    def __init__(self, rooms):
        self.allrooms = rooms
        self.room = self.allrooms["bridge"]
        self.inventory = Inventory()

    def draw(self, scrn):
        self.room.draw(scrn)
