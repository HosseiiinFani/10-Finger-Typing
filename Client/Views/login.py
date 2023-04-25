import pygame
import sys
from UI.Input import Input, PasswordInput
from UI.Button import Button
from lib.colors import BG
from setup import *
from requests import post
import pickle
import json
from lib.utils import handle_resize
from Transitions.ChangeScene import ChangeTo

protected = False

def View():
    global screen, center
    run = True

    def Login():
        if username_field.value == "" or pwd_field.value == "":
            raise ValueError()
            return
        creds = { 'username': username_field.value, 'password': pwd_field.value }
        response = post(base_url + '/api/users/login', json=creds)
        data = json.loads(response.text)
        if data['message'] == "error":
            raise PermissionError()
        else:
            with open('data.pickle', 'wb') as f:
                pickle.dump({'user': data['message']}, f)
            raise ChangeTo("main_menu")

    def BackToSignup():
        raise ChangeTo("signup")

    login_button = Button(screen, base_font, (center[0]-70, 200, 140, 40), (23,145,142), "Login", (0,0,0), Login)
    signup_button = Button(screen, base_font, (center[0]-200, 250, 400, 40), (23,145,142), "Don't have an account? Signup", (0,0,0), BackToSignup)
    username_field = Input((center[0]-70, 100, 140, 32), (123,224, 52), screen, base_font, placeholder="Username")  
    pwd_field = PasswordInput((center[0]-70, 150, 140, 32), (123,224, 52), screen, base_font, placeholder="Password")  
    UI_ELEMS = [username_field, pwd_field, login_button, signup_button]

    center = (screen.get_width()//2, screen.get_height()//2)

    err = False
    while run:

        for event in pygame.event.get():
    
            if event.type == pygame.QUIT:
                run = False

            screen.fill(BG)
            try:
                [element.render(event) for element in UI_ELEMS]
            except ChangeTo as e:
                return e
            except PermissionError:
                err_surface = base_font.render('Login Failed!', False, (255, 0, 0))
                err = True
            except ValueError:
                err_surface = base_font.render('Please fill out all the fields.', False, (255, 0, 0))
                err = True
        if err: screen.blit(err_surface, (center[0]-140, 300))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    View()