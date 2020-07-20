"""main menu"""
import pygame as pg
import menu
from text_box import TextBox
from event import SCREEN_TRANSITION
from lore import Lore
from utilities import multiline


class MainMenu(menu.Menu):
    """main menu"""

    def __init__(self):
        menu.Menu.__init__(self)
        self.options = ['1. Start!', '2. ???', '3. Quit']
        self.header = "Meow"
        self.text_box = TextBox()
        self.text_box.callback = self.process_text
        self.result_surf = None

    def handle_events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                self.text_box.handle_event(event)

    def draw(self, screen):
        menu.Menu.draw(self, screen)
        self.text_box.draw(screen)
        if self.result_surf is not None:
            #center results on the right of the screen
            position = (self.surf.get_width() - self.result_surf.get_width(),
                        int(self.surf.get_height()/2 - self.result_surf.get_height()/2))
            screen.blit(self.result_surf, position)

    def process_text(self, text):
        """process the text the user entered as a menu selection"""
        self.result_surf = None  # clear the result from last time
        if text == '1':
            self.result_surf = multiline('Woo! lets play', line_length=30)
        elif text == '2':
            lore = Lore().bake()
            lore.old_screen = self
            new_event = pg.event.Event(SCREEN_TRANSITION, new_screen=lore)
            pg.event.post(new_event)
        elif text == '3':
            pg.event.post(pg.event.Event(pg.QUIT))
        else:
            print("wrong choice lol")
            self.result_surf = multiline("wrong choice lol", line_length=30)
