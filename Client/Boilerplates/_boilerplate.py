import pygame
import sys
from UI.Input import Input, PasswordInput
from UI.Button import Button
from lib.colors import BG
from setup import *

def View():

    def Function():
        pass

    text_field = Input((center[0]-70, 100, 140, 32), (123,224, 52), screen, base_font, placeholder="Username")  
    pwd_field = PasswordInput((center[0]-70, 150, 140, 32), (123,224, 52), screen, base_font, placeholder="Password")  
    button = Button(screen, base_font, (center[0]-70, 200, 140, 40), (23,145,142), "Login", (0,0,0), Function)

    UI_ELEMS = []

    run = True

    while run:
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT:
                run = False

            screen.fill(BG)
            try:
                [element.render(event) for element in UI_ELEMS]
            except:
                pass
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    View()