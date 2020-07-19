"""useful stuffs"""
import pygame as pg

pg.init()
TITLE_FONT = pg.font.Font('hobbitonbrushhand.ttf', 48)
FONT = pg.font.Font('hobbitonbrushhand.ttf', 24)

def multiline(text, color=(254, 255, 255), line_length=80):
    """return a surface with all this text printed on it"""
    finished_lines = []  # surface array
    lines = text.splitlines()
    # line break anywhere theres an existing line break in the text
    for line in lines:
        words = line.split(' ')
        while len(words) > 0:
            finished_line = words.pop(0)
            # line break when it gets too wide

            while len(words) > 0 and len(finished_line) + len(words[-1]) < line_length:
                finished_line += ' ' + words.pop(0)
            print(finished_line)  # debug
            # render the line and tack it onto the end of finished_lines
            finished_lines.append(FONT.render(finished_line, False, color))
    # ok we have a list of surfaces with the lines written on them
    widths = map(lambda fl: fl.get_width(), finished_lines)
    # print(list(widths))
    width = max(widths)  # make it as wide as the widest
    max_height = max(map(lambda fl: fl.get_height(), finished_lines))

    # height = sum(heights) ##add them up to get the height
    height = max_height * len(finished_lines)  # make them evenly spaced
    surf = pg.Surface((width, height))
    surf.set_colorkey((0, 0, 0), pg.RLEACCEL)

    for i, fl in enumerate(finished_lines):
        surf.blit(fl, (0, i*max_height))
    # surf.set_alpha(128)
    return surf
