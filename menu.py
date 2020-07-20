"""a menu base class and some other helpful menu things"""
import pygame as pg
from utilities import FONT, TITLE_FONT


class Menu(pg.sprite.Sprite):
    """base class for menus"""
    def __init__(self):
        super(Menu, self).__init__()
        self.surf = pg.image.load('menu.png').convert()
        self.surf.set_colorkey((255, 255, 255), pg.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.options = ['1. option', '2. another options',
                        '3. yo dawg i herd u liek option']
        self.header = 'header'
        self.popup = pg.Surface([20, 20])

    def bake(self):
        """draw all the menu options and title onto the base sprite"""
        # draw the menu options onto the sprite.
        for i, opt in enumerate(self.options):
            text = FONT.render(opt, False, (254, 255, 255))
            self.surf.blit(text, (150, 200+i*25))
            print('blit ' + str(200+i*25) + ' ' + opt)
        # draw the header
        text = TITLE_FONT.render(self.header, False, (254, 255, 255))
        x_pos = self.surf.get_width()/2 - text.get_width()/2
        self.surf.blit(text, (x_pos, 100))

        # draw the header onto the sprite
    def draw(self, screen):
        """draw itself on the given surface"""
        screen.blit(self.surf, (0, 0))
        screen.blit(self.popup, (600, 440))
        #I considered rendering the text every frame, but since it doesn't change, we don't need to.
        # for i,opt in enumerate(self.options):
        #     text = font.render(opt.text, False, (255,255,255))
        #     screen.blit(text, (150, 200+i*25))
        # print('blit'+str(200+i*25))

    def handle_events(self, events):
        """placeholder event handle"""
        for event in events:
            if event.type == pg.KEYDOWN:
                # print(event.key)
                self.popup = FONT.render(event.unicode, False, (0, 255, 0))
                # self.surf.blit()


class Meow(pg.sprite.Sprite):
    """fading sprite"""

    def __init__(self):
        super(Meow, self).__init__()
        self.surf = pg.image.load('meow.png').convert()
        self.surf.set_colorkey((255, 255, 255), pg.RLEACCEL)
        self.rect = self.surf.get_rect()

    def draw(self, screen):
        screen.blit(self.surf, (500, 100))

