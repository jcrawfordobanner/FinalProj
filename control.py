#Dictates how the player can interact with the model
from model import *
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
