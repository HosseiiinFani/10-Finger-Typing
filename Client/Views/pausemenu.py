import pygame
import sys
from UI.Button import Button
from lib.colors import BG
from setup import *
import pickle
from Transitions.ChangeScene import ChangeTo

protected = True

def View():

    center = (screen.get_width()//2, screen.get_height()//2)
    run = True

    def Play():
        raise ChangeTo("main")
    def Pass():
        pass
    def BackToMain():
        raise ChangeTo("main_menu")
    
    def _logout():
        with open('data.pickle', 'wb') as f:
            pickle.dump(None, f)
    def Quit():
        global run
        _logout()
        run = False

    play_button = Button(screen, base_font, (center[0]-70, 160, 140, 40), (23,145,142), "Resume", (0,0,0), Play)
    back_button = Button(screen, base_font, (center[0]-70, 220, 140, 40), (23,145,142), "Back", (0,0,0), BackToMain)
    quit_button = Button(screen, base_font, (center[0]-70, 280, 140, 40), (23,145,142), "Quit", (0,0,0), Quit)
    UI_ELEMS = [play_button, back_button, quit_button]
    
    with open('data.pickle', 'rb') as f:
        loaded_obj = pickle.load(f)
        if loaded_obj['user']:
            user_button = Button(screen, base_font, (center[0]-70, 100, 140, 40), BG, str(loaded_obj['user'][1]), (0,0,0), Pass)
            UI_ELEMS.append(user_button)

    while run:
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT:
                run = False

            screen.fill(BG)
            try:
                [element.render(event) for element in UI_ELEMS]
            except ChangeTo as e:
                return e
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    View()