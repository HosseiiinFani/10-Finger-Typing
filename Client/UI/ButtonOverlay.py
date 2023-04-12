import pygame
from lib.consts import ghermez, sabz, tosi, soorati 

class Button:
    def __init__(self,pos,name,size):
        self.pos = pos
        self.name = name
        self.size = size
    def get_pos(self):
        return self.pos
    def highlight(self,a, display):
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
