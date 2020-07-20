"""a box that lets the user enter text"""
import pygame as pg
from utilities import FONT

class TextBox(pg.sprite.Sprite):
    """allow the user to enter text and do something after they do."""

    def __init__(self):
        super(TextBox, self).__init__()
        self.text = ''
        self.width = 200
        self.position = (320 - self.width/2, 350)
        # you should replace this callback with something else
        self.callback = lambda blah: print('!! ' + blah + ' !!')
        self.redraw()
        self.cursor_show = True
        self.cursor_pos = 4
        self.cursor = pg.surface.Surface((16, 24))
        self.cursor.fill((254, 255, 255))

    def draw(self, screen):
        """draw the textbox on the given surfaces"""
        screen.blit(self.surf, self.position)
        self.cursor_show = not self.cursor_show
        if self.cursor_show:
            screen.blit(self.cursor, (self.cursor_pos + self.position[0], 4 + self.position[1]))

    def redraw(self):
        """draw the text and stuff onto the surface"""
        self.surf = pg.surface.Surface((self.width, 32))
        self.surf.fill((32, 32, 32))
        rendered_text = FONT.render(self.text, False, (192, 192, 255))
        self.cursor_pos = 4 + rendered_text.get_width()
        self.surf.blit(rendered_text, (4, 4))

    def handle_event(self, event):
        """deal with incoming keypresses"""
        if event.type != pg.KEYDOWN:
            raise Exception('what are you doing textbox cannot handle this event')
        if event.key in (pg.K_RETURN, pg.K_KP_ENTER):
            self.callback(self.text)
            self.text = ''
        elif event.key == pg.K_BACKSPACE:
            self.text = self.text[:-1]
        else:
            self.text += event.unicode
        self.redraw()
