import pygame

pygame.init()
from pygame import *
from pygame import mixer

mixer.init()

istyping = False
ismousepressed = False
choosing_place_for_text = False

class Textclass:
    def __init__(self):

        # Text itself
        self.text            =  ""
        self.position        = (-50, -50)
        self.act_rect_color  = (200, 200, 200)
        self.size            = 48
        self.color                       = (240, 30, 100)
        self.offset_x = 5
        self.offset_y = 10
        
        # Button to start text input
        self.act_rect_pos    = (860, 20)
        self.activation_rect = pygame.Rect(self.act_rect_pos, (100, 100))

        #Text Outline
        self.box_color = ()

        for el in self.color:
            el = min(el + 50, 255)
            self.box_color = self.box_color + (el,)
        self.box = pygame.Rect(self.position, (self.size, self.size))

text = Textclass()

def TypeText():
    Font = pygame.font.SysFont(None, text.size)
    Text = Font.render(text.text, True, text.color)
    outline = pygame.Rect(text.position, (max(Text.get_width() + 10,100), text.size))
    pygame.draw.rect(textsurface, (text.box_color), outline, 2)
    textsurface.blit(Text, [text.position[0] + text.offset_x, text.position[1] + text.offset_y])

def AddText(text, color, size, x, y):
    Font = pygame.font.SysFont(None, size)
    Text = Font.render(text, True, color)
    drawing.blit(Text, (x,y))

colorlist = [(255, 255, 255), (255, 0, 0), (50, 255, 50), (50,50, 255), (100, 100, 100)]

TypeText()

pygame.draw.rect(drawing, (text.act_rect_color), (text.activation_rect))
if text.activation_rect.collidepoint(mx, my) and ismousepressed:
    ismousepressed = False
    choosing_place_for_text = True
    AddText(text.text, text.color, text.size, text.position[0] + text.offset_x, text.position[1] + text.offset_y)
    text.text = ""
if choosing_place_for_text and not text.activation_rect.collidepoint(mx, my) and ismousepressed:
    text.position = (mx, my)
    choosing_place_for_text = False
    istyping = True

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        Run = False
    elif event.type == pygame.KEYDOWN:
        if istyping:
            if event.key == pygame.K_BACKSPACE:
                text.text = text.text[0:-1]
            else:
                text.text += event.unicode
    elif event.type == pygame.MOUSEBUTTONDOWN:
        ismousepressed = True
    elif event.type == pygame.MOUSEBUTTONUP:
        ismousepressed = False

win.blit(textsurface, (0,0))
win.blit(drawing,(0,0))
textsurface.fill((0,0,0))

pygame.display.update()