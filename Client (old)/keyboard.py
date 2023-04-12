import pygame
pygame.init()
display = pygame.display.set_mode((800,267))
display.fill((91,239,247))
nor_k = pygame.image.load('n_keyboard')
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
           
button ={'w':Button((132,53),"w",(55,54)),"a":Button((92,106),"a",(55,54)),"d":Button((199,106),"d",(55,54)),"s":Button((145,106),"s",(55,54)),
         "q":Button((79,53),"q",(55,54)),"e":Button((186,53),"e",(55,54)),"z":Button((119,160),"z",(55,54)),"x":Button((172,160),"x",(55,54)),
         "c":Button((226,160),"c",(55,54))," ":Button((213,213)," ",(320,55))}
button_shift ={"İ":Button((0,160),"İ",(120,53)),"į":Button((653,160),"į",(150,53))}
button_name = ''
run = True
b_p = False
shift_p = False
#button_pressed
while run:
    display.blit(nor_k,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #if event.type == pygame.MOUSEMOTION:
            #x,y = pygame.mouse.get_pos()
            #print(x,y)
        if event.type == pygame.KEYDOWN:
            button_name = chr(event.key)
            #print(button_name)
            if button_name == 'İ' or button_name == 'į':
                shift_p = True
            else:
                b_p = True
        if event.type == pygame.KEYUP:
            if event.key == 304 or event.key == 303:
                shift_p = False
            else:
                b_p = False
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
        print('WE DO NOT HAVE THIS KEY!')
    pygame.display.update()
pygame.quit()


