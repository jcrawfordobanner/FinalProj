import pygame
from pygame.locals import*
import time


class Backdrop(object):
    def __init__(self, image_name, size):

        im = pygame.image.load(image_name)
        self.image = pygame.transform.scale(im, size)
        self.rect = self.image.get_rect()

    def draw(self, scrn, loc = (0,0)):
        scrn.blit(self.image, loc)


class Textbox(pygame.Surface):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, width,height,text=''):
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

        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 28)
        self.text = text
        self.textsurface = myfont.render(text, False,(0,0,0))
        self.imagein.blit(self.textsurface,(0,0))

        self.width=width
        self.height=height

    def draw(self, screen):
        size=screen.get_size()
        myfont = pygame.font.SysFont('Comic Sans MS', 28)
        screen.blit(self.imageout, (0, size[1]-(size[1]/4)))
        screen.blit(self.imagein, (30,int(size[1]*0.75)+15))
        self.imagein.fill((0,255,0))
        self.textsurface = myfont.render(self.text, False,(0,0,0))
        self.imagein.blit(self.textsurface,(0,0))

    def update(self, words):
        self.text = words


class Item(pygame.sprite.Sprite):
    def __init__(self, img, loc):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load(img) #see if needs fixing
        self.rect = self.image.get_rect()
        self.loc = loc
        self.clicked = False

    def draw(self, scrn):
        scrn.blit(self.image, self.loc)

    def update(self, click_pos):
        if self.loc == click_pos:
            self.clicked = True

class Character(pygame.sprite.Sprite):
    def __init__(self, loc):
        pygame.sprite.Sprite.__init__(self)

class Inventory(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.items = []
    def add_item(self, item):
        self.items.append(item)

class Room(pygame.sprite.LayeredUpdates):
    def __init__(self, msgs, items, backdrops):
        pygame.sprite.LayeredUpdates.__init__(self)
        self.messages = msgs
        self.items = items
        self.backdrop = backdrops
        self.items_vis = []
        for i in range(len(items)):
            if items[i].clicked == False:
                self.items_vis.append(items[i])

    def draw(self, scrn):
        self.backdrop.draw(scrn)
        for item in self.items_vis:
            item.draw(scrn)

    def update(self, click_pos):
        for item in self.items.sprites():
            item.update(click_pos)

class Narrative(object):
    def __init__(self,model):
        self.events = [1,2,3,4]
        self.model=model

    def scene1(self,model):
        model.update('You pressed the red button')
        actuallydraw()
        pygame.time.wait(3005)
        model.update('Congratulations...you died')
        actuallydraw()
        pygame.time.wait(3005)
        model.update('Game Over')
        actuallydraw()
    def scene2(self,model):
        model.update('You pressed the blue button')
        actuallydraw()
        pygame.time.wait(3005)
        model.update('Congratulations...you win')
        actuallydraw()
        pygame.time.wait(3005)
        model.update('Game Over')
        actuallydraw()
    def scene3(self,model):
        model.update('You pressed the green button')
        actuallydraw()
        pygame.time.wait(3005)
        model.update('Unfortunately nothing happened. You stay until you die of thirst')
        actuallydraw()
        pygame.time.wait(3005)
        model.update('Game Over')
        actuallydraw()


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

    def update(self,words=''):
        """Changes the model based upon new information"""
        #for r in self.allrooms:
            #r.update()
        self.textbox.update(words)

class MouseController(object):
    """ Handles input for space game """
    def __init__(self, model):
        self.model = model

    def handle_event(self, event):
        """ Event handler"""
        if event.type != KEYDOWN:
            return
        if event == pygame.K_k:
            story.scene1(self.model)
        if event.key == pygame.K_l:
            story.scene2(self.model)
        if event.key == pygame.K_l:
            story.scene3(self.model)

class PygameWindowView(object):
    """Draws the model"""
    def __init__(self, model, width = 640,height = 480):
        pygame.init()
        size = (width,height)
        pygame.display.init()
        self.screen = pygame.display.set_mode(size)
        self.model = model

    def draw(self):
        self.model.draw(self.screen)
        pygame.display.update()

current_event = 0




if __name__ == '__main__':
    pygame.init()

    wrench = Item("wrench.png", (200,200))
    wrench.image = pygame.transform.scale(wrench.image, (50, 60))
    stock = Backdrop("StockPhoto1.jpg", (640, 480))
    room =  Room({}, [wrench], stock)
    rooms = {"bridge":room}

    Modl = SpaceGameModel(rooms)
    SCRNtemp = PygameWindowView(Modl)
    Contrl = MouseController(Modl)

    story =Narrative(Modl)
    def actuallydraw():
            SCRNtemp.draw()
            SCRNtemp.draw()

    Modl.update('You have awoke inside of a room.')
    actuallydraw()
    pygame.time.wait(3005)
    Modl.update('In it you see three buttons, one red, one blue and one green.')
    actuallydraw()
    pygame.time.wait(3005)
    Modl.update('What do you do?')
    actuallydraw()
    pygame.time.wait(3005)
    Modl.update('j: red k: blue l: green')
    actuallydraw()
    current_event=1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            Contrl.handle_event(event)

    pygame.quit()
