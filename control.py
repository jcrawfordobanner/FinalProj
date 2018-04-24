#Dictates how the player can interact with the model
from model import *
import pygame
class MouseController(object):
    """ Handles input for space game """
    def __init__(self, model):
        self.model = model

    def handle_event(self, event,scren):
        """ Event handler"""
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            self.model.update(pos)

        if event.type != KEYDOWN:
            return
        if self.model.eventflags.get('1')==True:
            self.model.textbox.update(self.model.messages['game_intro'])
            scren.draw()
            if event.key == pygame.K_j:
                self.model.eventflags['1']=False
                self.model.textbox.update(self.model.messages['scene1'])
                scren.draw()
                self.model.eventflags['2']=True
                pygame.time.wait(2005)
                self.model.textbox.update(self.model.messages['bridge_intro'])
                scren.draw()
            if event.key == pygame.K_k:
                self.model.eventflags['1']=False
                self.model.textbox.update(self.model.messages['scene2'])
                scren.draw()
            if event.key == pygame.K_l:
                self.model.textbox.update(self.model.messages['scene3'])
                scren.draw()
                self.model.eventflags['1']=False

        elif self.model.eventflags.get('2')==True:
            pygame.time.wait(2005)
            self.model.textbox.update(self.model.messages['bridge_intro'])
            scren.draw()
            if event.key == pygame.K_j:
                pygame.time.wait(2005)
                self.model.textbox.update(self.model.messages['scene4'])
                scren.draw()
                self.model.eventflags['2']=False
            if event.key == pygame.K_k:
                pygame.time.wait(2005)
                self.model.eventflags['2']=False
                self.model.textbox.update(self.model.messages['scene5'])
                scren.draw()
            if event.key == pygame.K_l:
                pygame.time.wait(2005)
                self.model.textbox.update(self.model.messages['scene6'])
                scren.draw()
                self.model.eventflags['2']=False

        elif self.model.eventflags.get('2')==True:
            pygame.time.wait(2005)
            self.model.textbox.update(self.model.messages['bridge_intro'])
            scren.draw()
            if event.key == pygame.K_j:
                pygame.time.wait(2005)
                self.model.textbox.update(self.model.messages['scene4'])
                scren.draw()
                self.model.eventflags['2']=False
            if event.key == pygame.K_k:
                pygame.time.wait(2005)
                self.model.eventflags['2']=False
                self.model.textbox.update(self.model.messages['scene5'])
                scren.draw()
            if event.key == pygame.K_l:
                pygame.time.wait(2005)
                self.model.textbox.update(self.model.messages['scene6'])
                scren.draw()
                self.model.eventflags['2']=False
