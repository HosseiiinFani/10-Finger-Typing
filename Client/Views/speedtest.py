import pygame
from UI.Input import Input, PasswordInput
from UI.Button import Button
from lib.colors import BG
from setup import *
from lib.consts import KEYBUTTONS
from lib.utils import handle_resize
from timeit import default_timer as timer
from time import gmtime, strftime
from pygame.locals import USEREVENT

def View():
    y = 600
    screen.fill(BG)

    pygame.display.set_mode((min_x,y), HWSURFACE|DOUBLEBUF)

    M_ADV_X = 4
    data = "Military chocolate is part of the ration given out to troops. However, to stop them from eating all the chocolate in one go, they made it taste terrible! This made sure that"
    l = data.split()
    n = 12
    data = [' '.join(l[x:x+n]) for x in list(range(0, len(l), n))]
    # print([l[x:x+n] for x in list(range(0, len(l), n))])
    _data = iter(data)
    current = next(_data)
    states = [False]

    current_sentence = 0

    font=pygame.freetype.SysFont(None, 50)
    font.origin=True
 
    M_ADV_X = 4

    base_size = 6
    
    text_surf_rect = font.get_rect(current)
    baseline = text_surf_rect.y
    text_surf = pygame.Surface(text_surf_rect.size)
    text_surf_rect.center = (30, 40)
    metrics = font.get_metrics(current)
    
    KEYS = KEYBUTTONS
    [key.set_base(55,y - 300) for key in KEYS]

    start_time = timer()
    time_text = base_font.render(f'Time: {strftime("%M:%S", gmtime(int(timer() - start_time)))}', False, (0,0,0))
    UI_ELEMS = []

    run = True

    current_text = ''

    base_x, base_y = 30, 0
    position = [0,0]
    current_word = 0
    current_chr = 0

    progress_surface = base_font.render(' '.join(current.split()[:current_word]), False, (0,0,0))
    progress_base_x = progress_surface.get_width() + 4
    current_text_surf = base_font.render(current.split()[current_word], False, (0,0,0))

    text = base_font.render('', False, (0,0,0))

    screen.fill(BG)

    color = (0,0,0)
    while run:
        screen.fill(BG)
        time_text.fill(BG)
        # try:
        #     print(current_word, current_sentence, current.split()[current_word])
        # except: pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    try:
                        current_text = ''
                        current_word += 1
                        current_chr += len(current.split()[current_word]) + 1
                        if current_chr >= len(current)-1: raise IndexError
                        if current_word % 2 == 0: color = (255,0,0) 
                        else: color = (0,0,0)
                    except IndexError:
                        current = next(_data)
                        current_sentence += 1
                        current_chr = 0
                        current_word = 0
                        x = 0
                        screen.fill(BG)
                        
                if not event.key in [pygame.K_BACKSPACE, pygame.K_RSHIFT, pygame.K_LSHIFT, pygame.K_CAPSLOCK, pygame.K_ESCAPE, pygame.K_TAB, pygame.K_RETURN, pygame.K_SPACE]:
                    current_text += event.unicode
                    b_p = True
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT: 
                    shift_p = True
                    button_name = ''
                else:
                    b_p = True
                    
            [element.render(event) for element in KEYS]

            try:
                [element.render(event) for element in UI_ELEMS]
            except:
                pass
        pygame.event.post(pygame.event.Event(USEREVENT+1, {}))
        for i, sentence in enumerate(data[current_sentence:current_sentence+3]):    
            text = base_font.render(sentence, False, (0,0,0))
            screen.blit(text, (30, (i+1) * 80))

        # x = 0
        # for (idx, (letter, metric, state)) in enumerate(zip(current, metrics, states)):
        #     if idx == current_idx:
        #         if state:
        #             color = 'red'
        #         else:
        #             color = "gray"
        #     elif idx < current_idx:
        #         color = "green"
        #     else:
        #         color = 'black'
        #     font.render_to(text_surf, (x, baseline), letter, color)
        #     x += metric[M_ADV_X]
        
        remaining = 60 - (int(timer() - start_time))
        if remaining == 0:
            pass
        # print(metrics[M_ADV_X][1])
        progress_surface = base_font.render(' '.join(current.split()[:current_word]), False, (0,0,0))
        progress_base_x = progress_surface.get_width() + 4
        current_text_surf = base_font.render(current.split()[current_word], False, color)
        screen.blit(current_text_surf, ((base_x + progress_base_x), (1) * 120))
        time_text = base_font.render(f'Time: {strftime("%M:%S", gmtime(remaining))}', False, (0,0,0))
        screen.blit(time_text, (10, 10))
        text.fill(BG)
        time_text.fill(BG)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    View()