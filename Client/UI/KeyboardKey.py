from .Button import Button
from setup import screen, base_font, min_x, min_y
import pygame

class KeyboardKey(Button):
    original_key = ""

    x = 55
    y = 50
    button_size = 40
    spacing = 50
    y_spacing = 50

    base_x = 55
    base_y = 55
    base_size = 40
    base_spacing = 50
    base_yspacing = 50

    def __init__(self, key, row, column, color, multiply=1, prev_mult=1, alg=0, shift_value=None, non_shiftable=False):
        'alg -> alignment. 0=left, 1=right'
        self.row = row
        self.column = column
        self.multiply = multiply
        self.prev_mult = prev_mult
        self.original_key = key
        self.shift_value = shift_value
        self.non_shiftable = non_shiftable
        if multiply > 1:
            if alg == 0:
                position = (self.x + (self.spacing*column) - int(self.button_size * (multiply-1)),self.y+row*self.y_spacing,int(self.button_size*multiply),self.button_size)
                formula = "(self.x + (self.spacing*column) - int(self.button_size * (multiply-1)),self.y+row*self.y_spacing,int(self.button_size*multiply),self.button_size)"
            elif alg == 1:
                position = (self.x+self.spacing*column,self.y+row*self.y_spacing,int(self.button_size*multiply),self.button_size)
                formula = "(self.x+self.spacing*column,self.y+row*self.y_spacing,int(self.button_size*multiply),self.button_size)"
        else:
            position = (self.x+self.spacing*column,self.y+row*self.y_spacing,int(self.button_size*multiply),self.button_size)
            formula = "(self.x+self.spacing*column,self.y+row*self.y_spacing,int(self.button_size*multiply),self.button_size)"
        
        super().__init__(screen, base_font, position, color, key, (0,0,0), fixed_pos=True, formula=formula, onClick=None)

    @property
    def key(self):
        return self.label

    def goto_original(self, event):
        if event.type == pygame.VIDEORESIZE:
            width, height = event.size
            if width < min_x:
                width = min_x
            if height < min_y:
                height = min_y
            column, row, multiply, prev_mult = self.column, self.row, self.multiply, self.prev_mult
            self.button_size = self.base_size * (width / min_x)
            self.spacing = self.base_spacing * (width / min_x)
            self.y_spacing = self.base_yspacing * (height / min_y)
            self.x = self.base_x * (width / min_x)
            dest = eval(self.formula)
            self.move(dest)

    def render(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                if self.non_shiftable:
                    pass
                else:
                    if self.shift_value:
                        super().change_label(self.shift_value)
                        pass
                    else:
                        newLabel = chr(ord(self.key) - 32)
                        self.change_label(newLabel)
        else:
            self.change_label(self.original_key)
        try:
            self._render(event)
        except:
            print(f"Couldn't render {self.__str__()}")

    @property
    def shifted(self):
        if self.non_shiftable: 
            return self.original_key
        else:
            if self.shift_value:
                return self.shift_value
            else:
                newLabel = chr(ord(self.original_key) - 32)
                return newLabel
 

    def __repr__(self) -> str:
        return f"<KeyboardKey {self.key}/>"

    def __str__(self) -> str:
        return f"<KeyboardKey {self.key}/>"