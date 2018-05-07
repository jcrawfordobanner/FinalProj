
import pygame
from pygame.locals import *
import time

from model import *
from view import *

from classes import *
import narrative

class MouseController(object):
    """ Handles input for space game """
    def __init__(self, model):
        self.model = model

    def handle_event(self, event):
        """ Event handler"""
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            itemC = self.model.get_clicked(pos)
            if itemC:
                self.model.choices+=1
            #print(itemC)
            #print(itemC+"2")
            msg = self.model.messages.get(itemC)

            door = self.model.doors.get(itemC)
            if door:
                self.model.room = self.model.allrooms[door]
                # print(self.model.room)
            if self.model.puzzles.get(itemC) in self.model.inventor.items:
                msg = self.model.messages.get(itemC+'2')
            if str(self.model.choices) in self.model.messages and msg!=None:
                msg = msg + self.model.messages.get(str(self.model.choices))
            elif str(self.model.choices) in self.model.messages and msg==None:
                msg=self.model.messages.get(str(self.model.choices))
            self.model.update(pos, msg)


            # if self.model.doors.get(itemC):
            #     self.model.room = self.model.allrooms[self.model.doors[itemC]]
            #     self.model.update(pos)
            #     print(self.model.room)
        if event.type != KEYDOWN:
            return
