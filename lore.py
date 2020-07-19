"""a menu that shows the game's lore"""
import menu
from utilities import multiline

class Lore(menu.Menu):
    """a kind of menu that shows flavortext"""
    def __init__(self):
        menu.Menu.__init__(self)
        self.options = []
        self.header = 'Lore'
        self.text = "in the deep dankness of the unknown future, great starships take decades or centuries to travel between the stars. Thier tireless engines never stop, and the acceleration is so constant that crews often mistake it for gravity. Most people while away the decades in coldsleep caskets, but for some reason, you find yourself and your party awake..."

    def bake(self):
        menu.Menu.bake(self)
        surf = multiline(self.text, line_length=60)
        # position = (self.surf.get_size() - map((lambda i: i/2), surf.get_size()))
        position = tuple(map(lambda i, j: int(i/2 - j/2), self.surf.get_size(), surf.get_size()))
        print(position)
        # position = self.surf.get_width() - 
        self.surf.blit(surf, position)
