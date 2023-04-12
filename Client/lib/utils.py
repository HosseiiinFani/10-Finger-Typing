import pygame
from pygame.locals import *

def handle_resize(min_x, min_y, event):
    width, height = event.size
    if width < min_x:
        width = min_x
    if height < min_y:
        height = min_y
    return pygame.display.set_mode((width,height), HWSURFACE|DOUBLEBUF|RESIZABLE)