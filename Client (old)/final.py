import pygame,ctypes
import pygame.freetype
import socketio

# sio = socketio.Client()
# sio.connect('http://localhost:8080')

pygame.init()
display = pygame.display.set_mode((800,367))

nor_k = pygame.image.load('n_keyboard.png')
f__nor__k = pygame.transform.scale(nor_k,(800,267))
tosi = pygame.image.load('toosi.png')
sabz = pygame.image.load('sabz.png')
ghermez = pygame.image.load('ghermaz.png')
soorati = pygame.image.load('soorati.png')
bg = (91,239,247)

class Button:
    def __init__(self,pos,name,size):
        self.pos = pos
        self.name = name
        self.size = size
    def get_pos(self):
        return self.pos
    def highlight(self,a):
        if a == -1:
            talgh = ghermez
        if a == 1:
            talgh = sabz
        if a == 2:
            talgh = soorati
        if a == 0:
            talgh = tosi
        talgh = pygame.transform.scale(talgh,self.size)
        display.blit(talgh,(self.pos))

def main():
    # just some demo data for you to type
    data = "salam farmande."
    current = data
    states = [False for _ in current]
    current_idx = 0 # points to the current letter, as you have already guessed

    def emitCorrect():
        pass
        # sio.emit('ping', {'message': 'Correct!'})
    def emitWrong():
        # global current_idx
        # states[current_idx] = True
        # current_idx += 1
        pass
        # sio.emit('ping', {'message': 'Wrong!'})
    
    black = (0,0,0)
    # display.fill((91,239,247))


    button ={"w":Button((132,153),"w",(55,54)),"a":Button((92,207),"a",(55,54)),"d":Button((199,207),"d",(55,54)),"s":Button((145,207),"s",(55,54)),
            "q":Button((79,153),"q",(55,54)),"e":Button((186,153),"e",(55,54)),"z":Button((119,260),"z",(55,54)),"x":Button((172,260),"x",(55,54)),
            "c":Button((226,260),"c",(55,54))," ":Button((213,313)," ",(320,55)),"r":Button((240,153),"r",(55,54)),"t":Button((292,153),"t",(55,54)),
            "y":Button((346,153),"y",(55,54)),"u":Button((400,153),"u",(55,54)),"i":Button((453,153),"i",(55,54)),"o":Button((506,153),"o",(55,54)),
            "p":Button((560,153),"p",(55,54)),"f":Button((253,207),"f",(55,54)),"g":Button((306,207),"g",(55,54)),"h":Button((359,207),"h",(55,54)),
            "j":Button((412,207),"j",(55,54)),"k":Button((464,207),"k",(55,54)),"l":Button((518,207),"l",(55,54)),"v":Button((280,260),"v",(55,54)),
            "b":Button((332,260),"b",(55,54)),"n":Button((386,260),"n",(55,54)),"m":Button((440,260),"m",(55,54))}
    button_shift ={"İ":Button((0,260),"İ",(120,53)),"į":Button((653,260),"į",(150,53))}
    button_caps = {"ĭ":Button((0,206),"ĭ",(92,53))}
    button_name = ''

    sentence = ('')
    run = True
    b_p = False
    shift_p = False
    flag = False
    caps_p = False

    
    font = pygame.freetype.Font(None, 50)
    font.origin = True
    font_height = font.get_sized_height()
    M_ADV_X = 4
    
    text_surf_rect = font.get_rect(current)
    baseline = text_surf_rect.y
    text_surf = pygame.Surface(text_surf_rect.size)
    text_surf_rect.center = (225, 50)
    metrics = font.get_metrics(current)

    while True:
        display.fill(bg)
        display.blit(nor_k,(0,100))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key != 1073742049 and event.key != 1073742053 and event.key != 1073741881 :
                    button_name = chr(event.key)
                if event.key == 1073742049 or event.key == 1073742053:
                    shift_p = True
                    button_name = ""
                elif event.key == 1073741881:
                    caps_p = not caps_p  
                    button_name = ""
                else:
                    b_p = True
                try:
                    if ord(button_name) == 8:
                        current_idx -= 1
                except:
                    pass
                else:
                    if event.unicode == current[current_idx].lower():
                        # if we press the correct letter, move the index
                        emitCorrect()
                        current_idx += 1
                        if current_idx >= len(current):
                            current_idx = 0
                            current = "asdgajhdg"
                            states = [False for _ in current]
                            text_surf_rect = font.get_rect(current)
                            baseline = text_surf_rect.y
                            text_surf = pygame.Surface(text_surf_rect.size)
                            text_surf_rect.center = (display.get_rect().centerx, 50)
                            metrics = font.get_metrics(current)
                    else:
                        emitWrong()
                        states[current_idx] = True

            if event.type == pygame.KEYUP:
                if event.key == 1073742049 or event.key == 1073742053:
                    shift_p = False
                    button_name = ""
                else:
                    b_p = False

                for x in button:
                    if button_name == x and (shift_p or caps_p):
                        sentence += button_name.upper()
                        print(sentence)
                    elif button_name == x and not shift_p :
                        sentence += button_name
                        print(sentence)
                try:
                    if ord(button_name) == 8:
                        sentence = sentence[ : -1]
                except:
                    pass


                    for x in button:
                        if button_name == x and (shift_p or caps_p):
                            sentence += button_name.upper()
                            print(sentence)
                        elif button_name == x and not shift_p :
                            sentence += button_name
                            print(sentence)
                        try:
                            if ord(button_name) == 8:
                                sentence = sentence[ : -1]
                        except:
                            pass

        button[current[current_idx]].highlight(0)
        try:
            if shift_p:
                button_shift['İ'].highlight(1)
                button_shift['į'].highlight(1)
                if b_p:
                    button[button_name].highlight(1)
            else:
                if b_p:
                    button[button_name].highlight(-1 if states[current_idx] else 1)
                        
        # except:
        #     # print('WE DO NOT SUPPORT THIS KEY!')
        #     pass
        # try:
        #     button[current[current_idx]].highlight(0)
        except:
            pass

        # clear everything                        
        # display.fill(bg)
        text_surf.fill(bg)
        
        x = 0
        # render each letter of the current sentence one by one
        for (idx, (letter, metric, state)) in enumerate(zip(current, metrics, states)):
            # select the right color
            if idx == current_idx:
                if state:
                    color = 'red'
                else:
                    color = "yellow"
            elif idx < current_idx:
                color = "green"
            else:
                color = 'black'
            # render the single letter
            font.render_to(text_surf, (x, baseline), letter, color)
            # and move the start position
            x += metric[M_ADV_X]
          
        display.blit(text_surf, text_surf_rect)
        pygame.display.flip()

if __name__ == '__main__':
    main()
