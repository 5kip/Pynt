import pygame

pygame.init()
from pygame import *
from pygame import mixer

mixer.init()

istyping = False
check_mousepress_varsepressed = False
choosing_place_for_text = False
class Textclass:
    def __init__(self):

        # Text itself
        self.text            =  ""
        self.position        = (100, 100)
        self.act_rect_color  = (200, 200, 200)
        self.size            = 48
        self.color           = (  240, 30, 100)
        self.offset_x = 5
        self.offset_y = 10
        
        # Button to start text input
        self.act_rect_pos    = (300, 300)
        self.activation_rect = pygame.Rect(self.act_rect_pos, (100, 100))

        #Text Outline
        self.box_color = ()

        for el in self.color:
            el = min(el + 50, 255)
            self.box_color += (el,)
        self.box = pygame.Rect(self.position, (self.size, self.size))

text = Textclass()
def dotext(main_surface, text_surface, other_surface, check_mousepress_var):
    mx, my = pygame.mouse.get_pos()

    global choosing_place_for_text
    global check_mousepress_varsepressed
    def TypeText():
        Font = pygame.font.SysFont(None, text.size)
        Text = Font.render(text.text, True, text.color)
        outline = pygame.Rect(text.position, (max(Text.get_width() + 10,100), text.size))
        pygame.draw.rect(other_surface, (text.box_color), text.box, 2)
        other_surface.blit(Text, [text.position[0] + text.offset_x, text.position[1] + text.offset_y])

    def AddText(text, color, size, x, y):
        Font = pygame.font.SysFont(None, size)
        Text = Font.render(text, True, color)
        text_surface.blit(Text, (x,y))

    colorlist = [(255, 255, 255), (255, 0, 0), (50, 255, 50), (50,50, 255), (100, 100, 100)]

    pygame.draw.rect(other_surface, (text.act_rect_color), (text.activation_rect))

    if check_mousepress_var and text.activation_rect.collidepoint(mx, my):
        choosing_place_for_text = True
        AddText(text.text, text.color, text.size, text.position[0] + text.offset_x, text.position[1]+ text.offset_y)
        text.text = ""
    if not text.activation_rect.collidepoint(mx, my) and check_mousepress_var:
        choosing_place_for_text = False
        text.position = (mx, my)
        istyping = True
    
    TypeText()