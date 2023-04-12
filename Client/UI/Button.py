import pygame
from lib.utils import handle_resize
from setup import min_x, min_y

class Button:
    highlighted = False
    def __init__(self, screen, base_font, pos, color, label, text_color, onClick, fixed_pos=False, formula=None):
        self.screen = screen
        self.base_font = base_font
        self.label = label
        self.color = color
        self.base_color = color
        self.text_color = text_color
        self.button_rect = pygame.Rect(pos)
        self.pos = pos
        self._pos = pos
        self.onClick = onClick
        self.fixed_pos = fixed_pos
        self.formula = formula

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
 
    def _render(self, event):
        pygame.draw.rect(self.screen, self.color if not self.highlighted else tuple(map(lambda x: x-100, self.color)), self.button_rect)
        button_surface = self.base_font.render(self.label, True, self.text_color)
        self.screen.blit(button_surface, (self.pos[0] + (self.pos[2]//2 - (button_surface.get_width()//2)), self.pos[1] + (self.pos[3]//2 - (button_surface.get_height()//2))))
        if not self.fixed_pos:
            self.center_self(event)
        else:
            self.goto_original(event)

    def handleClick(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                self.onClick()
    
    def render(self, event):
        self.handleClick(event)
        self._render(event)

    def highlight(self):
        self.highlighted = True

    def unhighlight(self):
        self.highlighted = False

    def change_label(self, newLabel):
        # print(f"Changed from {self.label} to {newLabel}")
        self.label = newLabel

    @property
    def position(self):
        return self._pos
    def move(self, pos):
        self.pos = pos
        self.button_rect = pygame.Rect(pos)
