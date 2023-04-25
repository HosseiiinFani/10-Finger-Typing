import pygame
import pickle
from UI.Input import Input, PasswordInput
from UI.Button import Button
from lib.colors import BG
from setup import *
from lib.utils import handle_resize
import math
from Transitions.ChangeScene import ChangeTo
import json

def View():
    center = (screen.get_width()//2, screen.get_height()//2)
    file_levels = open('./levels.json')
    _levels = dict(json.load(file_levels))
    levels = list(_levels.keys())
    file_levels.close()
    card_width = 190
    card_height = 100
    padding = 20

    def transferContext(level):
        with open('context.pickle', 'wb') as f:
            pickle.dump(level, f)
    def GoToLevel(level):
        selectedLevel = _levels[level]
        transferContext(selectedLevel)
        raise ChangeTo("main")

    levels_len = len(levels)
    max_w = screen.get_width() // card_width
    
    rows = math.ceil(levels_len / max_w)
    if rows == 1: rows += 1

    def GetMenuButton(x, y):
        try:
            return Button(screen, base_font, (padding + x * card_width, (padding + card_height * (y-1)) + 50, card_width-padding//2, card_height-padding//2), (23,145,142), levels[(y-1)*max_w:y*max_w][x], (0,0,0), lambda: GoToLevel(levels[(y-1)*max_w:y*max_w][x]), fixed_pos=True)
        except:
            pass

    level_buttons = [
        GetMenuButton(x, y)
        for y in range(1, rows) for x in range(max_w)
    ]

    def BackToMain():
        raise ChangeTo("main_menu")
    
    back_button = Button(screen, base_font, (10, 10, 140, 40), (23,145,142), "Back", (0,0,0), BackToMain)
    UI_ELEMS = [back_button]

    run = True

    while run:
        for event in pygame.event.get():
            screen.fill(BG)
    
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.VIDEORESIZE:
                newScreen = handle_resize(min_x,min_y,event)
                max_w = newScreen.get_width() // card_width
                rows = math.ceil(levels_len / max_w)
                if rows == 1: rows += 1
                level_buttons = [
                    GetMenuButton(x, y)
                    for y in range(1, rows) for x in range(max_w)
                ]
            try:
                [element.render(event) for element in UI_ELEMS]
                [element.render(event) for element in level_buttons]
            except ChangeTo as e:
                return e
            except: pass
       
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    View()
