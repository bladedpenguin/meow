"""main menu"""
import pygame as pg
import menu


class MainMenu(menu.Menu):
    """main menu"""
    def __init__(self):
        menu.Menu.__init__(self)
        self.options = ['1. Start!', '2. ???', '3. Quit']
        self.header = "Meow"
        self.text_box = menu.TextBox()
    def handle_events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                self.text_box.handle_event(event)
    def draw(self, screen):
        menu.Menu.draw(self, screen)
        self.text_box.draw(screen)
