import pygame
import sys
from UI.Input import Input, PasswordInput
from UI.Button import Button
from lib.colors import BG
from setup import *
import pickle
from Transitions.ChangeScene import ChangeTo

protected = True

def View():

    center = (screen.get_width()//2, screen.get_height()//2)

    def Play():
        raise ChangeTo("play")
    def Logout():
        raise ChangeTo("logout")
    def _logout():
        with open('data.pickle', 'wb') as f:
            pickle.dump(None, f)

    play_button = Button(screen, base_font, (center[0]-70, 160, 140, 40), (23,145,142), "Play", (0,0,0), Play)
    logout_button = Button(screen, base_font, (center[0]-70, 220, 140, 40), (23,145,142), "Logout", (0,0,0), Logout)

    UI_ELEMS = [play_button, logout_button]

    run = True

    while run:
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT:
                run = False

            screen.fill(BG)
            try:
                [element.render(event) for element in UI_ELEMS]
            except ChangeTo as e:
                if e == "login": _logout()
                return e
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    View()