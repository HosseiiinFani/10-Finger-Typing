import pygame
import sys

pygame.init()
  
clock = pygame.time.Clock()
  
# it will display on screen
screen = pygame.display.set_mode([600, 500])

BLACK = (0,0,0)

# basic font for user typed
base_font = pygame.font.Font(None, 32)
user_text = ''

# color_active = pygame.Color('lightskyblue3')
# color_passive = pygame.Color('chartreuse4')

class Input:
    text = ""
    def __init__(self, pos, color, rounded=8, text_color=(0,0,0), placeholder=""):
        self.input_rect = pygame.Rect(pos)
        self.placeholder_rect = pygame.Rect(pos)
        self.outline = pygame.Rect(tuple(map(lambda x, y: x + y, pos, (-rounded//2,-rounded//2,rounded,rounded))))
        self.placeholder = placeholder
        self.rounded = rounded
        self.text_color = text_color 
        self.color = color
        self.outline_color = color

    @property
    def value(self):
        return self.text
    def render(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_rect.collidepoint(event.pos):
                self.active = True
                self.outline_color = BLACK
            else:
                self.active = False
                self.outline_color = self.color
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
        if self.text == "":
            pygame.draw.rect(screen, self.color, self.placeholder_rect)
            placeholder_surface = base_font.render(self.placeholder, True, (127,127,127))
            self.placeholder_rect.width = max(90, placeholder_surface.get_width()+self.rounded*1.5)
            self.outline.width = max(100, placeholder_surface.get_width()+18)
            screen.blit(placeholder_surface, (self.input_rect.x+5, self.input_rect.y+5))
        else:
            pygame.draw.rect(screen, self.color, self.input_rect)
            text_surface = base_font.render(self.text, True, self.text_color)
            self.input_rect.width = max(90, text_surface.get_width()+self.rounded*1.5)
            self.outline.width = max(100, text_surface.get_width()+18)
            screen.blit(text_surface, (self.input_rect.x+5, self.input_rect.y+5))
        pygame.draw.rect(screen, self.outline_color, self.outline, self.rounded, self.rounded)

input_field = Input((200, 200, 140, 32), (123,224, 52), placeholder="Username")  
pwd_field = Input((200, 400, 140, 32), (123,224, 52), placeholder="Password")  

while True:
    for event in pygame.event.get():
  
      # if user types QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
      
        screen.fill((255,255,255))
        input_field.render(event)
        pwd_field.render(event)
    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.flip()
      
    # clock.tick(60) means that for every second at most
    # 60 frames should be passed.
    clock.tick(60)