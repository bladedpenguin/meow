"""a menu that shows the game's lore"""
import pygame as pg
import menu
from utilities import multiline
# from main_menu import MainMenu
from event import SCREEN_TRANSITION

class Lore(menu.Menu):
    """a kind of menu that shows flavortext"""
    def __init__(self):
        menu.Menu.__init__(self)
        print('lore init')
        self.options = []
        self.header = '' #since we want to fill the screen with text, keep options and headers empty
        self.text = "in the deep dankness of the unknown future, great starships take decades or centuries to travel between the stars. The acceleration from their tireless engines is so constant that it feels like gravity to the crew. Most people spend the decades in coldsleep caskets, but for some reason, you find yourself and your party awake..."
        self.old_screen = None

    def bake(self):
        menu.Menu.bake(self)
        # turn our string into an image of a text block:
        surf = multiline(self.text, line_length=60)
        ## position the image of text in the center of the screen
        position = tuple(map(lambda i, j: int(i/2 - j/2), self.surf.get_size(), surf.get_size()))
        # print(position)
        # position = (int(self.surf.get_width()/2 - surf.get_width()/2),
        #  int(self.surf.get_height()/2 - surf.get_height()/2)
        self.surf.blit(surf, position)
        return self
    def handle_events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                pg.event.post(pg.event.Event(SCREEN_TRANSITION, new_screen=self.old_screen))
