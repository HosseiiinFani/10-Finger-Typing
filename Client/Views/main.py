import pygame
import sys
import pygame.freetype
# import socketio
from lib.colors import BG
from lib.consts import BUTTONS, BUTTON_SHIFT, KEYBUTTONS, happy, sad
from setup import *
from UI.Button import Button
import pickle
from timeit import default_timer as timer
from time import gmtime, strftime
from Transitions.ChangeScene import ChangeTo
from pygame.locals import USEREVENT

# sio = socketio.Client()
# sio.connect('http://localhost:8080')

protected = True

def View():
    raw_data = None
    difficulty = None
    level_score = None
    level_name = None
    with open('context.pickle', 'rb') as f:
        loaded_obj = pickle.load(f)
        if loaded_obj:
            difficulty = loaded_obj['difficulty']
            level_score = loaded_obj['score']
            level_name = loaded_obj['name']
            raw_data = loaded_obj['phrases']
        else:
            raise ChangeTo("play")
    data = iter(raw_data)
    current = next(data)
    states = [False for _ in current]
    current_idx = 0 

    errors = 0
    time = ''

    def emitCorrect():
        pass
        # screen.blit(happy, (screen.get_width()-120, 20))
    def emitWrong():
        nonlocal errors
        errors += 1
        # screen.blit(sad, (screen.get_width()-120, 20))
    def Pause():
        raise ChangeTo("pausemenu")

    def transferContext(level, score, _errors, time, level_score):
        removeContext()
        with open('context.pickle', 'wb') as f:
            pickle.dump({'level': level, 'score': score, 'errors': _errors, 'time': time, 'level_score': level_score}, f)

    button_name = ''

    b_p = False
    shift_p = False
    caps_p = False

    
    font=pygame.freetype.SysFont(None, 50)
    font.origin=True
 
    M_ADV_X = 4
    
    text_surf_rect = font.get_rect(current)
    baseline = text_surf_rect.y
    text_surf = pygame.Surface(text_surf_rect.size)
    text_surf_rect.center = (330, 50)
    metrics = font.get_metrics(current)

    pause_button = Button(screen, base_font, (screen.get_width()-80, 20, 70, 40), (23,145,142), "menu", (0,0,0), Pause, fixed_pos=True, formula="(screen.get_width()-80, 20, 70, 40)")

    KEYS = KEYBUTTONS
    UI_ELEMS = [pause_button]

    selected_button = None

    pygame.display.flip()
    run = True

    start_time = timer()

    errors_text = base_font.render(f'Errors: {errors}', False, (0,0,0))
    time_text = base_font.render(f'Time: {strftime("%M:%S", gmtime(int(timer() - start_time)))}', False, (0,0,0))

    screen.fill(BG)

    wrong = False

    while run:
        text_surf.fill(BG)

        errors_text = base_font.render(f'Errors: {errors}', False, (0,0,0))
        events = pygame.event.get()
        for event in events:
            screen.fill(BG)
            try: 
                next_button = list(filter(lambda x: x.label == current[current_idx], KEYS))[0]
                next_button.highlight()
            except:
                pass
            [element.render(event) for element in KEYS]

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key != pygame.K_LSHIFT and event.key != pygame.K_RSHIFT and event.key != pygame.K_CAPSLOCK:
                    button_name = event.unicode
                    b_p = True
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT: 
                    shift_p = True
                    button_name = ''
                elif event.key == pygame.K_CAPSLOCK:
                    caps_p = not caps_p  
                else:
                    b_p = True
                if ord(button_name if button_name != '' else 'a') == 8:
                        # current_idx -= 1
                        pass
                else:
                    if b_p:
                        if event.unicode == current[current_idx]:
                            emitCorrect()
                            current_idx += 1
                            if current_idx >= len(current):
                                current_idx = 0
                                try:
                                    current = next(data)
                                    states = [False for _ in current]
                                    text_surf_rect = font.get_rect(current)
                                    baseline = text_surf_rect.y
                                    text_surf = pygame.Surface(text_surf_rect.size)
                                    text_surf_rect.center = (225, 50)
                                    metrics = font.get_metrics(current)
                                except StopIteration:
                                    time = strftime("%M:%S", gmtime(int(timer() - start_time)))
                                    _time = int(timer() - start_time)
                                    target_time = recommended_times[difficulty-1]
                                    time_penalty = 0
                                    total_letters = sum(len(character) for character in raw_data)
                                    if _time > target_time:
                                        remainder = _time - target_time
                                        time_penalty = remainder // 5 # 1 score per 5 secs.
                                    error_penalty = 0
                                    if errors > 0.2 * total_letters:
                                        errors_percent = round((errors / total_letters), 1)
                                        remainder = abs(errors_percent - 0.2)
                                        error_penalty = remainder * level_score
                                    final_score = level_score - time_penalty - error_penalty
                                    transferContext(level_name, max(round(final_score), 0), errors, time, level_score)
                                    return "completion"

                            wrong = False
                        else:
                            wrong = True
                            emitWrong()
                            states[current_idx] = True

            if event.type == pygame.KEYUP:
                if selected_button:
                    selected_button.unhighlight()
                shift_p = False
                b_p = False
                
            try:
                [element.render(event) for element in UI_ELEMS]
            except ChangeTo as e:
                return e

            try:
                if shift_p:
                    if b_p:
                        selected_button = list(filter(lambda x: x.shifted == button_name, KEYS))[0]
                        selected_button.highlight()
                else:
                    if b_p:
                        selected_button = list(filter(lambda x: x.label == button_name, KEYS))[0]
                        selected_button.highlight()
            except:
                pass
        pygame.event.post(pygame.event.Event(USEREVENT+1, {}))


  
        x = 0
        for (idx, (letter, metric, state)) in enumerate(zip(current, metrics, states)):
            if idx == current_idx:
                if state:
                    color = 'red'
                else:
                    color = "gray"
            elif idx < current_idx:
                color = "green"
            else:
                color = 'black'
            font.render_to(text_surf, (x, baseline), letter, color)
            x += metric[M_ADV_X]
        
        # time_text.fill(BG)
        time_text = base_font.render(f'Time: {strftime("%M:%S", gmtime(int(timer() - start_time)))}', False, (0,0,0))
        screen.blit(time_text, (30, 40))
        screen.blit(text_surf, (180, 30))
        screen.blit(errors_text, (40, 20))
        ### MARK: 004501``
        # if wrong: screen.blit(sad, (screen.get_width()-150, 20))
        # else: screen.blit(happy, (screen.get_width()-150, 20))
        pygame.display.update()
        clock.tick(60)
        rest = list(filter(lambda x: x.label != current[current_idx], KEYS))
        [r.unhighlight() for r in rest]

if __name__ == '__main__':
    View()
