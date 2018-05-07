from classes import *
import narrative
import pygame
from pygame.locals import*
import time


class SpaceGameModel(object):
    """Model of the game"""
    def __init__(self, size, rooms, doors,puzzles):
        self.allrooms = rooms #dictionary of all rooms
        self.room = self.allrooms["startRoom"]
        self.inventor = Inventory()
        self.messages = narrative.messages
        self.textbox= Textbox(size, self.messages['game_intro'])
        self.doors = doors
        self.puzzles=puzzles
        self.choices=0


    def draw(self, scrn):
        self.room.draw(scrn)
        self.textbox.draw(scrn)

    def get_clicked(self, pos):
        clicked_item = False
        for item in self.room.items:
            if item.click(pos):
                clicked_item = item.click(pos)
        return clicked_item

    def update(self, pos, words = None):
        """Changes the model based upon new information"""

        if words:
            self.textbox.update(words)
        for key in self.allrooms:
            self.allrooms[key].update(pos)
        for item in self.room.items:
            if item.hidd and item.take:
                self.inventor.add_item(item)
        # if self.get_clicked(pos) in self.doors:
        #     self.room = self.allrooms[self.doors.get(self.get_clicked(pos))]
