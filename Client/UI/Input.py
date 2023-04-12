import pygame
from lib.colors import BLACK
from lib.utils import handle_resize
from setup import min_x, min_y

class Input:
    text = ""
    active = False
    def __init__(self, pos, color, screen, base_font, rounded=8, text_color=(0,0,0), placeholder="", fixed_pos=False, formula=None):
        self.screen = screen
        self.base_font = base_font
        self.input_rect = pygame.Rect(pos)
        self.placeholder_rect = pygame.Rect(pos)
        self.outline = pygame.Rect(tuple(map(lambda x, y: x + y, pos, (-rounded//2,-rounded//2,rounded,rounded))))
        self.placeholder = placeholder
        self.rounded = rounded
        self.text_color = text_color 
        self.color = color
        self.outline_color = color
        self.pos = pos
        self.fixed_pos = fixed_pos
        self.formula = formula

    @property
    def value(self):
        return self.text

    def center_self(self, event):
        if event.type == pygame.VIDEORESIZE:
            screen = handle_resize(min_x,min_y,event)
            center = (screen.get_width()//2, screen.get_height()//2)
            self.move((center[0] - self.position[2]//2,) + self.position[1:])
    def goto_original(self, event):
        if event.type == pygame.VIDEORESIZE:
            screen = handle_resize(min_x,min_y,event)
            dest = eval(self.formula)
            self.move(dest)

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
            pygame.draw.rect(self.screen, self.color, self.placeholder_rect)
            placeholder_surface = self.base_font.render(self.placeholder, True, (127,127,127))
            self.placeholder_rect.width = max(90, placeholder_surface.get_width()+self.rounded*1.5)
            self.outline.width = max(100, placeholder_surface.get_width()+18)
            self.screen.blit(placeholder_surface, (self.input_rect.x+5, self.input_rect.y+5))
        else:
            pygame.draw.rect(self.screen, self.color, self.input_rect)
            text_surface = self.base_font.render(self.text, True, self.text_color)
            self.input_rect.width = max(90, text_surface.get_width()+self.rounded*1.5)
            self.outline.width = max(100, text_surface.get_width()+18)
            self.screen.blit(text_surface, (self.input_rect.x+5, self.input_rect.y+5))
        pygame.draw.rect(self.screen, self.outline_color, self.outline, self.rounded, self.rounded)
        if not self.fixed_pos:
            self.center_self(event)
        else:
            self.goto_original(event)
    
    @property
    def position(self):
        return self.pos
    def move(self, pos):
        rounded = self.rounded
        self.input_rect = pygame.Rect(pos)
        self.placeholder_rect = pygame.Rect(pos)
        self.outline = pygame.Rect(tuple(map(lambda x, y: x + y, pos, (-rounded//2,-rounded//2,rounded,rounded))))


class PasswordInput(Input):
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
            pygame.draw.rect(self.screen, self.color, self.placeholder_rect)
            placeholder_surface = self.base_font.render(self.placeholder, True, (127,127,127))
            self.placeholder_rect.width = max(90, placeholder_surface.get_width()+self.rounded*1.5)
            self.outline.width = max(100, placeholder_surface.get_width()+18)
            self.screen.blit(placeholder_surface, (self.input_rect.x+5, self.input_rect.y+5))
        else:
            pygame.draw.rect(self.screen, self.color, self.input_rect)
            text_surface = self.base_font.render("*" * len(self.text), True, self.text_color)
            self.input_rect.width = max(90, text_surface.get_width()+self.rounded*1.5)
            self.outline.width = max(100, text_surface.get_width()+18)
            self.screen.blit(text_surface, (self.input_rect.x+5, self.input_rect.y+5))
        pygame.draw.rect(self.screen, self.outline_color, self.outline, self.rounded, self.rounded)
        if not self.fixed_pos:
            self.center_self(event)
        else:
            self.goto_original(event)
 