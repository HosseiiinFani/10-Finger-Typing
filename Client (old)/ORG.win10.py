import pygame,ctypes

pygame.init()

display = pygame.display.set_mode((800,367))
pygame.display.set_caption('10 FINGER TYPING')

black = (0,0,0)
display.fill((91,239,247))
nor_k = pygame.image.load('n_keyboard.png')
f__nor__k = pygame.transform.scale(nor_k,(800,267))
tosi = pygame.image.load('toosi.png')
soorati = pygame.image.load('soorati.png')


class Button:
    def __init__(self,pos,name,size):
        self.pos = pos
        self.name = name
        self.size = size
    def get_pos(self):
        return self.pos
    def highlight(self,a):
        if a == 1:
            talgh = soorati
            talgh = pygame.transform.scale(talgh,self.size)
        else:
            talgh = tosi
            talgh = pygame.transform.scale(talgh,self.size)
        display.blit(talgh,(self.pos))

button ={"w":Button((132,153),"w",(55,54)),"a":Button((92,207),"a",(55,54)),"d":Button((199,207),"d",(55,54)),"s":Button((145,207),"s",(55,54)),
         "q":Button((79,153),"q",(55,54)),"e":Button((186,153),"e",(55,54)),"z":Button((119,260),"z",(55,54)),"x":Button((172,260),"x",(55,54)),
         "c":Button((226,260),"c",(55,54))," ":Button((213,313)," ",(320,55)),"r":Button((240,153),"r",(55,54)),"t":Button((292,153),"t",(55,54)),
         "y":Button((346,153),"y",(55,54)),"u":Button((400,153),"u",(55,54)),"i":Button((453,153),"i",(55,54)),"o":Button((506,153),"o",(55,54)),
         "p":Button((560,153),"p",(55,54)),"f":Button((253,207),"f",(55,54)),"g":Button((306,207),"g",(55,54)),"h":Button((359,207),"h",(55,54)),
         "j":Button((412,207),"j",(55,54))}
button_shift ={"İ":Button((0,260),"İ",(120,53)),"į":Button((653,260),"į",(150,53))}
button_caps = {"ĭ":Button((0,206),"ĭ",(92,53))}
button_name = ''

sentence = ('')
run = True
b_p = False
shift_p = False
flag = False
caps_p = False

#button_pressed
while run:
    display.fill((255,255,102))
   
    sentenceText = pygame.font.Font(None,48)
    text = sentenceText.render(sentence, True, black)
    textRect = text.get_rect()
    textRect.center = (800/2,100/2)
    display.blit(text,textRect)
    
    display.blit(nor_k,(0,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
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

    try:
        if shift_p:
            button_shift['İ'].highlight(1)
            button_shift['į'].highlight(1)
            if b_p:
                button[button_name].highlight(1)
        else:
            if b_p:
                button[button_name].highlight(2)
                    
    except:
        print('WE DO NOT SUPPORT THIS KEY!')
    # send to server

    pygame.display.update()
pygame.quit()
