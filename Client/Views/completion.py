import pygame
from lib.colors import BG
from setup import *
import pickle
from lib.utils import handle_resize
from UI.Button import Button
from Transitions.ChangeScene import ChangeTo

protected = True

def View():
    center = (screen.get_width()//2, screen.get_height()//2)

    def BackToMain():
        removeContext()
        raise ChangeTo("main_menu")
 
    back_button = Button(screen, base_font, (center[0]-70, 220, 140, 40), (23,145,142), "Back", (0,0,0), BackToMain)
    UI_ELEMS = [back_button]

    run = True

    with open('context.pickle', 'rb') as f:
        context = pickle.load(f)
    pygame.event.post(pygame.event.Event(USEREVENT+1, {}))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.VIDEORESIZE:
                newScreen = handle_resize(min_x,min_y,event)
                center = (newScreen.get_width()//2, newScreen.get_height()//2)
 
            screen.fill(BG)
            try:
                [element.render(event) for element in UI_ELEMS]
            except ChangeTo as e:
                return e
        if context["score"] < int(context["level_score"]) // 2:
            line1 = base_font.render(f'Ah! you finished {context["level"]}', False, (0, 0, 0))
            line3 = base_font.render(f'Try harder next time!', False, (0, 0, 0))
            screen.blit(line3, (center[0]-line3.get_width()//2, 190))
        else:
            line1 = base_font.render(f'Great Job! you finished {context["level"]}', False, (0, 0, 0))
        line2 = base_font.render(f'with a score of {context["score"]} in {context["time"]} with {context["errors"]} errors!', False, (0,0,0))
        screen.blit(line1, (center[0]-line1.get_width()//2, 150))
        screen.blit(line2, (center[0]-line2.get_width()//2, 170))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    View()