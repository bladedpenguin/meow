"""a little game about various things"""
import pygame as pg
# import menu
from main_menu import MainMenu
# from lore import Lore
from event import SCREEN_TRANSITION

class Game:
    """run the whole game"""
    def __init__(self):
        self.display = pg.display.set_mode([640, 480])
        self.next_screen = None
        self.running = True
        # menu = menu.Menu()
        self.screen = MainMenu()
        # screen = Lore()
        self.screen.bake()
        self.clock = pg.time.Clock()
    def main(self):
        """Run the main tickloop"""
        while self.running:
            #handle events
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == SCREEN_TRANSITION:
                    if event.new_screen is not None:
                        self.next_screen = event.new_screen
                    self.screen = self.next_screen
            self.screen.handle_events(events)

            self.display.fill((0, 0, 0))
            self.screen.draw(self.display)

            self.clock.tick(60)
            pg.display.update()
        print("goodbye!")
        pg.quit()

##actually do the thing
game = Game()
game.main()
