import os
import pygame
from pygame.locals import *
from lib.colors import BG

pygame.init()

clock = pygame.time.Clock()
  
screen = pygame.display.set_mode((800,367), HWSURFACE|DOUBLEBUF|RESIZABLE)


base_font = pygame.font.Font(None, 32)

center = (screen.get_width()//2, screen.get_height()//2)

base_url = 'http://127.0.0.1:8080'

min_x, min_y = 800, 367

recommended_times = [45, 75, 100]

def removeContext():
    if os.path.isfile("context.pickle"): os.remove('context.pickle')
