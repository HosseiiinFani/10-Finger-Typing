import pygame
import sys
from UI.Input import Input, PasswordInput
from UI.Button import Button
from lib.colors import BG
from setup import *
from requests import post
from Transitions.ChangeScene import ChangeTo

protected = False

def View():
    center = (screen.get_width()//2, screen.get_height()//2)

    name_field = Input((center[0]-70, 50, 140, 32), (123,224, 52), screen, base_font, placeholder="Name")  
    username_field = Input((center[0]-70, 100, 140, 32), (123,224, 52), screen, base_font, placeholder="Username")  
    pwd_field = PasswordInput((center[0]-70, 150, 140, 32), (123,224, 52), screen, base_font, placeholder="Password")  


    def Signup():
        if name_field.value == "" or username_field.value == "" or pwd_field.value == "":
            raise ValueError()
            return
        creds = { 'name': name_field.value,'username': username_field.value, 'password': pwd_field.value }
        response = post(base_url + '/api/users', json=creds)
        if response.status_code == 200:
            raise ChangeTo("login")
        else:
            raise PermissionError()
        
    def BackToLogin():
        raise ChangeTo("login")

    signup_button = Button(screen, base_font, (center[0]-70, 200, 140, 40), (23,145,142), "Sign up", (0,0,0), Signup)
    login_button = Button(screen, base_font, (center[0]-200, 250, 400, 40), (23,145,142), "Already have an account? Login", (0,0,0), BackToLogin)

    UI_ELEMS = [username_field, pwd_field, name_field, signup_button, login_button]

    err = False

    run = True

    while run:
        for event in pygame.event.get():
    
            if event.type == pygame.QUIT:
                run = False

            screen.fill(BG)
            try:
                [element.render(event) for element in UI_ELEMS]
            except ValueError:
                err_surface = base_font.render('Please fill out all the fields.', False, (255, 0, 0))
                err = True
            except ChangeTo as e:
                return e
            except PermissionError:
                pass
        if err: screen.blit(err_surface, (center[0]-140, 300))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    View()