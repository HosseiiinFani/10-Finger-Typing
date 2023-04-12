import pygame
from UI.KeyboardKey import KeyboardKey

nor_k = pygame.image.load('lib/keyboard.png')
f__nor__k = pygame.transform.scale(nor_k,(800,267))
tosi = pygame.image.load('lib/gray.png')
sabz = pygame.image.load('lib/green.png')
ghermez = pygame.image.load('lib/red.png')
soorati = pygame.image.load('lib/pink.png')

happy = pygame.image.load('lib/happy.jpg')
sad = pygame.image.load('lib/sad.jpg')

happy = pygame.transform.scale(happy, (50,50))
sad = pygame.transform.scale(sad, (50,50))

from UI.ButtonOverlay import Button
BUTTONS ={"w":Button((132,153),"w",(55,54)),"a":Button((92,207),"a",(55,54)),"d":Button((199,207),"d",(55,54)),"s":Button((145,207),"s",(55,54)),
        "q":Button((79,153),"q",(55,54)),"e":Button((186,153),"e",(55,54)),"z":Button((119,260),"z",(55,54)),"x":Button((172,260),"x",(55,54)),
        "c":Button((226,260),"c",(55,54))," ":Button((213,313)," ",(320,55)),"r":Button((240,153),"r",(55,54)),"t":Button((292,153),"t",(55,54)),
        "y":Button((346,153),"y",(55,54)),"u":Button((400,153),"u",(55,54)),"i":Button((453,153),"i",(55,54)),"o":Button((506,153),"o",(55,54)),
        "p":Button((560,153),"p",(55,54)),"f":Button((253,207),"f",(55,54)),"g":Button((306,207),"g",(55,54)),"h":Button((359,207),"h",(55,54)),
        "j":Button((412,207),"j",(55,54)),"k":Button((464,207),"k",(55,54)),"l":Button((518,207),"l",(55,54)),"v":Button((280,260),"v",(55,54)),
        "b":Button((332,260),"b",(55,54)),"n":Button((386,260),"n",(55,54)),"m":Button((440,260),"m",(55,54)), ",":Button((492,260),",",(55,54)),
        ".":Button((545,260),".",(55,54)), "/":Button((598,260),"/",(55,54))}

BUTTON_SHIFT ={"İ":Button((0,260),"İ",(120,53)),"į":Button((653,260),"į",(150,53))}

COLOR0 = (138, 180, 251)
COLOR1 = (143, 132, 250)
COLOR2 = (217, 115, 249)
COLOR3 = (255, 103, 108)
COLOR4 = (255, 150, 153)
COLOR5 = (232, 172, 251)
COLOR6 = (181, 173, 251)
COLOR7 = (185, 209, 253)
WHITE =  (255,255,255)

row1 = [KeyboardKey("`", 1, 0, COLOR0, multiply=2, shift_value="~"), KeyboardKey("1", 1, 1, COLOR0, shift_value="!"), KeyboardKey("2", 1, 2, COLOR0, shift_value="@"), KeyboardKey("3", 1, 3, COLOR1, shift_value="#"), KeyboardKey("4", 1, 4, COLOR2, shift_value="$"),KeyboardKey("5", 1, 5, COLOR3, shift_value="%"), KeyboardKey("6", 1, 6, COLOR3, shift_value="^"), KeyboardKey("7", 1, 7, COLOR4, shift_value="&"), KeyboardKey("8", 1, 8, COLOR4, shift_value="*"), KeyboardKey("9", 1, 9, COLOR5, shift_value="("), KeyboardKey("0", 1, 10, COLOR6, shift_value=")"), KeyboardKey("-", 1, 11, COLOR7, shift_value="_"), KeyboardKey("=", 1, 12, COLOR7, shift_value="+"), KeyboardKey("BACK", 1, 13, COLOR7, multiply=2, alg=1, non_shiftable=True) ]
row2 = [KeyboardKey("TAB", 2, 0, COLOR0, multiply=2, non_shiftable=True), KeyboardKey("q", 2, 1, COLOR0), KeyboardKey("w", 2, 2, COLOR0), KeyboardKey("e", 2, 3, COLOR1), KeyboardKey("r", 2, 4, COLOR2),KeyboardKey("t", 2, 5, COLOR3), KeyboardKey("y", 2, 6, COLOR3), KeyboardKey("u", 2, 7, COLOR4), KeyboardKey("i", 2, 8, COLOR4), KeyboardKey("o", 2, 9, COLOR5), KeyboardKey("p", 2, 10, COLOR6), KeyboardKey("[", 2, 11, COLOR7, shift_value="{"), KeyboardKey("]", 2, 12, COLOR7, shift_value="}"), KeyboardKey("\\", 2, 13, COLOR7, multiply=2, alg=1, shift_value="|") ]
row3 = [KeyboardKey("LOCK", 3, 0, COLOR0, multiply=2, non_shiftable=True), KeyboardKey("a", 3, 1, COLOR0), KeyboardKey("s", 3, 2, COLOR0), KeyboardKey("d", 3, 3, COLOR1), KeyboardKey("f", 3, 4, COLOR2),KeyboardKey("g", 3, 5, COLOR3), KeyboardKey("h", 3, 6, COLOR3), KeyboardKey("j", 3, 7, COLOR4), KeyboardKey("k", 3, 8, COLOR4), KeyboardKey("l", 3, 9, COLOR5), KeyboardKey(";", 3, 10, COLOR6, shift_value=":"), KeyboardKey("'", 3, 11, COLOR7, shift_value="\""), KeyboardKey("ENTER", 3, 12, COLOR7, multiply=3.3, alg=1, non_shiftable=True) ]
row4 = [KeyboardKey("SHIFT", 4, 0, COLOR0, multiply=2, non_shiftable=True), KeyboardKey("z", 4, 1, COLOR0), KeyboardKey("x", 4, 2, COLOR0), KeyboardKey("c", 4, 3, COLOR1), KeyboardKey("v", 4, 4, COLOR2),KeyboardKey("b", 4, 5, COLOR3), KeyboardKey("n", 4, 6, COLOR3), KeyboardKey("m", 4, 7, COLOR4), KeyboardKey(",", 4, 8, COLOR4, shift_value="<"), KeyboardKey(".", 4, 9, COLOR5, shift_value=">"), KeyboardKey("/", 4, 10, COLOR6, shift_value="?"), KeyboardKey("SHIFT", 4, 11, COLOR7, multiply=4.6, alg=1, non_shiftable=True) ]
row5 = [KeyboardKey("", 5, 0, COLOR0, non_shiftable=True), KeyboardKey("", 5, 1, COLOR0, non_shiftable=True), KeyboardKey("", 5, 2, COLOR1, non_shiftable=True), KeyboardKey(" ", 5, 3, COLOR1, multiply=7.2, alg=1, non_shiftable=True), KeyboardKey("", 5, 9, COLOR1, non_shiftable=True), KeyboardKey("", 5, 10, COLOR7, non_shiftable=True), KeyboardKey("", 5, 11, COLOR7, non_shiftable=True), KeyboardKey("", 5, 12, COLOR7, non_shiftable=True), KeyboardKey("", 5, 13, COLOR7, non_shiftable=True)]

KEYBUTTONS = row1 + row2 + row3 + row4 + row5