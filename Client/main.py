import pygame
from setup import *
import os

import Views.login as login
import Views.main as Main
import Views.signup as signup
import Views.menu as menu
import Views.pausemenu as pausemenu
import Views.completion as completion
import Views.play as play

scenes = {
    'login': login,
    'signup': signup,
    'main': Main,
    'main_menu': menu,
    'pausemenu': pausemenu,
    'completion': completion,
    'play': play
}

def main():
    scene = 'login'
    run = True
    while run:
        try:
            next_scene = scenes[scene].View()
            scene = str(next_scene) if next_scene != None else None
        except KeyError:
            return
        

if __name__ == "__main__":
    main()
    pygame.quit()
    if os.path.isfile("data.pickle"): os.remove('data.pickle')
    if os.path.isfile("context.pickle"): os.remove('context.pickle')
