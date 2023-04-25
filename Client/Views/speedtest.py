import pygame
from lib.colors import BG
from setup import *
from lib.consts import KEYBUTTONS
from timeit import default_timer as timer
from time import gmtime, strftime
from pygame.locals import USEREVENT
import pickle
from Transitions.ChangeScene import ChangeTo
import random

def View():
    y = 600
    screen.fill(BG)

    pygame.display.set_mode((min_x,y), HWSURFACE|DOUBLEBUF)

    sentences = ["As may be imagined, the dinner which was soon afterwards partaken of by the family was anything but a cheerful meal. For the first time Io sat opposite to her husband gloomy and silent, scarcely touching the food before her. Are you not well, my love? asked Oscar anxiously. I ought not to have suffered you to walk to church in the heat!! It did me no harm; it was my own will to walk, replied Io coldly.", "Our first mile lay through a clump of pine-wood, where snow had recently fallen. When I looked at my comrade's broad back, and observed the vigour of his action as he trod deep into the virgin snow at every stride, scattering it aside like fine white powder as he lifted each foot, I thought how admirably he was fitted for a pioneer in the wilderness, or for the work of those dauntless, persevering men who go forth to add to the world's geographical knowledge, and to lead the expeditions sent out in search of such lost heroes as Franklin and Livingstone.", "Be calm! I entreat you to hear me, before you give vent to your hatred on my devoted head. Have I not suffered enough that you seek to increase my misery? Life, although it may only be an accumulation of anguish, is dear to me, and I will defend it. Remember, thou hast made me more powerful than thyself; my height is superior to thine; my joints more supple. But I will not be tempted to set myself in opposition to thee. I am thy creature, and I will be even mild and docile to my natural lord and king, if thou wilt also perform thy part, the which thou owest me. Oh, Frankenstein, be not equitable to every other, and trample upon me alone, to whom thy justice, and even thy clemency and affection, is most due. Remember, that I am thy creature; I ought to be thy Adam; but I am rather the fallen angel, whom thou drivest from joy for no misdeed. Everywhere I see bliss, from which I alone am irrevocably excluded. I was benevolent and good; misery made me a fiend. Make me happy, and I shall again be virtuous"]
    data = sentences[random.randint(0, len(sentences)-1)]
    l = data.split()
    n = 12
    data = [' '.join(l[x:x+n]) for x in list(range(0, len(l), n))]
    # print([l[x:x+n] for x in list(range(0, len(l), n))])
    _data = iter(data)
    current = next(_data)
    states = [False] * len(current.split())

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

    def transferContext(wpm, errors):
        removeContext()
        with open('context.pickle', 'wb') as f:
            pickle.dump({'wpm': wpm, 'errors': errors}, f)
    remaining = 60

    def finishTest():
        wpm = round((current_chr // 5) / ((60 - remaining) / 60))
        transferContext(wpm, len(list(filter(lambda x: x == False, states))))

    writing_text = ""
    while run:
        screen.fill(BG)
        time_text.fill(BG)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    try:
                        if writing_text == current.split()[current_word]: states[current_word] = True
                        current_word += 1
                        current_chr += len(current.split()[current_word]) + 1
                        if current_chr >= len(current)-1: raise IndexError
                        writing_text = ""
                    except IndexError:
                        try:
                            current = next(_data)
                        except StopIteration:
                            finishTest()
                            return "results"
                        states = [False] * len(current.split())
                        current_sentence += 1
                        current_chr = 0
                        current_word = 0
                        x = 0
                        writing_text = ""
                        screen.fill(BG)
                    
                        
                if not event.key in [pygame.K_BACKSPACE, pygame.K_RSHIFT, pygame.K_LSHIFT, pygame.K_CAPSLOCK, pygame.K_ESCAPE, pygame.K_TAB, pygame.K_RETURN, pygame.K_SPACE]:
                    writing_text += event.unicode
                    b_p = True
                if event.key == pygame.K_BACKSPACE: writing_text = writing_text[:-1]
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

        remaining = 60 - (int(timer() - start_time))

        if remaining == 0:
            finishTest()
            return "results"

        progress_surface = base_font.render(' '.join(current.split()[:current_word]), False, (0,0,0))
        progress_base_x = progress_surface.get_width() + 4
        writing_text_surf = base_font.render(writing_text, False, (0,0,0))
        screen.blit(writing_text_surf, ((base_x + progress_base_x), (1) * 120))

        for i, _word in enumerate(current.split()[:current_word]):
            progress_surface = base_font.render(' '.join(current.split()[:i]), False, (0,0,0))
            progress_base_x = progress_surface.get_width() + 4
            current_text_surf = base_font.render(_word, False, (0,255,0) if states[i] == True else (255,0,0))
            screen.blit(current_text_surf, ((base_x + progress_base_x), (1) * 120))



        time_text = base_font.render(f'Time: {strftime("%M:%S", gmtime(remaining))}', False, (0,0,0))
        screen.blit(time_text, (10, 10))
        text.fill(BG)
        time_text.fill(BG)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    View()