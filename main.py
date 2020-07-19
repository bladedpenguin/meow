"""a little game about various things"""
import pygame as pg
# import menu
from mainmenu import MainMenu
# from lore import Lore

screen = pg.display.set_mode([640, 480])
running = True
# menu = menu.Menu()
menu = MainMenu()
# menu = Lore()
menu.bake()
clock = pg.time.Clock()
font = pg.font.Font('hobbitonbrushhand.ttf',24)

#main tickloop
while running:
    #handle events
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
    menu.handle_events(events)

    screen.fill((0, 0, 0))
    menu.draw(screen)

    clock.tick(60)
    pg.display.flip()
print("goodbye!")
pg.quit()
