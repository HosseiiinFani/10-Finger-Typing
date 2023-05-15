import pygame
from lib.colors import BG
from setup import *
import pickle
from Transitions.ChangeScene import ChangeTo
from UI.Button import Button

def View():

    def BackToMain():
        raise ChangeTo("main_menu")
    
    back_button = Button(screen, base_font, (10, 10, 140, 40), (23,145,142), "Back", (0,0,0), BackToMain)
    UI_ELEMS = [back_button]

    run = True

    wpm = 0
    errors = 0

    with open('context.pickle', 'rb') as f:
        loaded_obj = pickle.load(f)
        if loaded_obj:
            wpm = loaded_obj['wpm']
            errors = loaded_obj['errors']
        else:
            raise ChangeTo("main_menu")
    while run:
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT:
                run = False

            screen.fill(BG)
            try:
                [element.render(event) for element in UI_ELEMS]
            except ChangeTo as e:
                return e
        wpm_text = base_font.render(f"WPM: {wpm}", False, (0,0,0))
        errors_text = base_font.render(f"Errors: {errors}", False, (0,0,0))
        screen.blit(wpm_text, (100,100))
        screen.blit(errors_text, (100,120))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    View()