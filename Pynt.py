import pygame

pygame.init()
from pygame import *
from pygame import mixer

mixer.init()

import Text as txt

WINX = 1250
WINY = 726

empty = (0,0,0,0)

win = pygame.display.set_mode((WINX, WINY))
alpha = pygame.Surface((WINX, WINY),pygame.SRCALPHA)
drawing = pygame.Surface((WINX,WINY),pygame.SRCALPHA)
scrolling_things = pygame.Surface((WINX,WINY),pygame.SRCALPHA)
textsurface = pygame.Surface((WINX, WINY), pygame.SRCALPHA)

pygame.display.set_caption("Pynt 0.6")

prevx = None
prevy = None
ismousepressed = False
brush_width = 5
BLUE_INDEX = 5
YELLOW_INDEX = 2
RED_INDEX = 1
RADIUS = 32
BUTTONWIDTH = 65
BUTTONSPACING = 10
RESET_BACKGROUND_BUTTON_OFFSET = 30
MOUSE_LEFT_SCREEN_OFFSET = 1
WIDTHCIRCLEPOS = (1190,50)
BGCOLORLIST =([0,0,0],[100,100,100],[200,200,200],[255,255,255],[100,100,255])
bg_color_index = 0
is_ukraine_action_started = False
is_ussr_action_started = False
pressedkey = pygame.key.get_pressed()
CurrentBGColor = BGCOLORLIST[bg_color_index]
is_transparence_moving = False
brush_transparency = 255
transparency_slider_x = 1043
brush_color = (255,255,255,brush_transparency)
istyping = False
selecting_place_to_type = False
 

# classes




class Ukraine:
    state       : int = 0
    final_state : int = 5

    def clicked_blue(self):
        if self.state == 0:
            self.state = 1
        elif self.state != 1:
            self.state = 0

    def clicked_yellow(self):
        if self.state == 1:
            self.state = 2
        else:
            self.state = 0

    def clicked_other_color(self):
        self.state = 0

    def pressed_u(self):
        if self.state == 2:
            self.state = 3

    def released_u(self):
        if self.state > 2:
            self.state = 2

    def changed_bg(self):
        if self.state >= 3 and self.state < self.final_state:
            self.state += 1

    def is_finished(self):
        return self.state == self.final_state
ukraine = Ukraine() # ukraine = OBJECT

class USSR:
    state       = 0
    final_state = 1

    def clicked_red(self):
        if self.state != 0:
            state = 0
        else:
            state = 1

    def clicked_yellow(self):
        if self.state != 1 :
            self.state = 0
        else:
            self.state = 2

    def clicked_other_color(self):
        self.state = 0

    def pressed_r(self):
        if self.state != 2 :
            self.state = 0
        else:
            self.state = 3

    def released_r(self):
        if self.state != 3:
            self.state = 0
        else:
            self.state = 2

    def BG_changed(self):
        if self.state != 3 or 4 or 5 or self.final_state :
            self.state = 0
        else:
            self.state = self.state + 1

    def Ussr_state_check(self):
        if self.state >= self.final_state:
            print("123")
Ussr = USSR()

def drawcross(middlex , rightdown):
    pygame.draw.line(drawing,(255,0,0),(middlex,75),(825,10),10)
    pygame.draw.line(drawing,(255,0,0),(middlex,10),(825,75),10)

def Scale(surface, color, slider_color, x, y, length, width, units_per_pixel, variable_to_change):
    slider_radius = width + 1
    slider_x = None
    #if slider_x != mx:
    slider_x      = x + length
    slider_y          = y + width / 2
    pygame.draw.rect(surface, (color), (x,y,length,width))
    if slider_x >= x + length + 1:
        slider_x = x + length
    if slider_x <= x - 1:
        slider_x = x - length
    if my >= slider_y - slider_radius / 2 and my <= slider_y + slider_radius / 2 and mx >= slider_x - slider_radius / 2 and mx <= slider_x + slider_radius / 2 and ismousepressed:
        slider_x = mx
    pygame.draw.circle(surface, (slider_color),(slider_x, slider_y), slider_radius)


     





# app

run = True
while run:
    mx, my = pygame.mouse.get_pos()

    startx = BUTTONSPACING
    endx = startx + BUTTONWIDTH

    colors = [(255,0,0),(255,132,0),(255,255,0),(0,255,0),(0,255,255),(31,79,255),(95,0,184),(255,0,255)]

    Scale(drawing, (200,200,200), (100,100,100), 500, 300, 300, 20, 1, brush_transparency)

    txt.dotext(win, textsurface, textsurface, ismousepressed)

    starty = BUTTONSPACING
    endy = starty + BUTTONWIDTH

    pygame.draw.rect(drawing,(112,112,112),(0,0,WINX,100))


    for i in range(len(colors)):
        pygame.draw.rect(drawing,colors[i],(startx,starty,BUTTONWIDTH,BUTTONWIDTH))
        startx = endx + BUTTONSPACING
        endx = startx + BUTTONWIDTH

    pygame.draw.rect(drawing, (150 , 150 , 150), (850,10,200,80))
    pygame.draw.rect(drawing, (200, 200, 200), (915,20, 127,5))
    pygame.draw.circle(scrolling_things, (230, 230, 230), (transparency_slider_x, 22), 5)

    circlex = startx + RADIUS
    pygame.draw.circle(drawing, (255,255,255), (circlex,45), 32)

    circlex = circlex + RADIUS + BUTTONSPACING + RADIUS
    pygame.draw.circle(drawing, (0,0,0), (circlex,42), 32)

    startx = endx + BUTTONSPACING
    endx = startx + BUTTONWIDTH
    startx = endx + BUTTONSPACING
    endx = startx + BUTTONWIDTH

    drawcross(startx, endx)
    pygame.draw.circle(drawing,(brush_color),WIDTHCIRCLEPOS,brush_width*0.5)

    def select_color():
        global brush_transparency
        if my > 100:
            return

        startx = BUTTONSPACING
        endx = startx + BUTTONWIDTH

        # Squares
        for i in range(len(colors)):
            if mx <= endx and mx >= startx:

                if i == BLUE_INDEX:
                    ukraine.clicked_blue()
                elif i == YELLOW_INDEX:
                    ukraine.clicked_yellow()
                    Ussr.clicked_yellow()
                elif i == RED_INDEX:
                    Ussr.clicked_red()
                else:
                    ukraine.clicked_other_color()
                    Ussr.clicked_other_color()

                return colors[i]

            startx = startx + BUTTONWIDTH + BUTTONSPACING
            endx = startx + BUTTONWIDTH

        for color in [(255,255,255), (0,0,0)]:
            # White circle
            if mx <= endx and mx >= startx:
                return color

            startx = endx + BUTTONSPACING
            endx = startx + BUTTONWIDTH

        # Cross
        if mx <= endx and mx >= startx:
            drawing.fill(empty)

    if my <= 30:
        brush_transparency = (transparency_slider_x - 915) * 2 - 1
        if transparency_slider_x <= 914:
            transparency_slider_x = 915
        if transparency_slider_x >= 1044:
            transparency_slider_x = 1043
        if mx >= transparency_slider_x - 5 and mx <= transparency_slider_x + 5 and ismousepressed:
            is_transparence_moving = True
        else:
            is_transparence_moving = False
        if ismousepressed:
            transparency_slider_x = mx


        startx = endx + BUTTONSPACING
        endx = startx + BUTTONWIDTH


    def highlight_color():
        if my > 100 or not ismousepressed:
            return

        startx = BUTTONSPACING
        endx = startx + BUTTONWIDTH

        for i in range(len(colors)):
            if mx <= endx and mx >= startx:
                pygame.draw.rect(alpha, (0,0,0,100), (startx,starty,BUTTONWIDTH,BUTTONWIDTH))

            startx = startx + BUTTONWIDTH + BUTTONSPACING
            endx = startx + BUTTONWIDTH

        for i in range(2):
            if mx <= endx and mx >= startx:
                pygame.draw.circle(alpha, (0,0,0,25), (startx + RADIUS, 45), 32)

            startx = endx + BUTTONSPACING
            endx = startx + BUTTONWIDTH

    nextbgcolor = (bg_color_index + 1) % len(BGCOLORLIST)
    pygame.draw.circle(drawing, BGCOLORLIST[nextbgcolor], (WINX-15,WINY-15), 10)

    if my >= WINY - MOUSE_LEFT_SCREEN_OFFSET or my <= MOUSE_LEFT_SCREEN_OFFSET or mx >= WINX - MOUSE_LEFT_SCREEN_OFFSET or mx <= MOUSE_LEFT_SCREEN_OFFSET:
        ismousepressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ismousepressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            ismousepressed = False
            new_color = select_color()
            if new_color != None:
                brush_color = new_color
            if mx > WINX - RESET_BACKGROUND_BUTTON_OFFSET and my > WINY - RESET_BACKGROUND_BUTTON_OFFSET:
                bg_color_index = (bg_color_index + 1) % len(BGCOLORLIST)
                nextbgcolor = (bg_color_index + 1) % len(BGCOLORLIST)
                pygame.draw.circle(drawing, BGCOLORLIST[nextbgcolor], (WINX-15,WINY-15), 10)
                pygame.draw.rect(win,(BGCOLORLIST[bg_color_index]),(0,0,WINX,WINY))
                Ussr.BG_changed()
                ukraine.changed_bg()
        elif event.type == pygame.MOUSEWHEEL:
            if brush_width == 50 or brush_width <= 0:
                brush_width = 1
                pygame.draw.circle(win,(112,112,112),(1190,50),(25))
            elif event.y == -1  :
                brush_width = brush_width - 1
            else                :
                brush_width = brush_width + 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                txt.text.text = txt.text.text[0:-1]
            else:
                txt.text.text += event.unicode

#цвета
# хохол

    highlight_color()

    if pressedkey[K_u]:
        ukraine.pressed_u()
    else:
        ukraine.released_u()

    if pressedkey[K_r]:
        Ussr.pressed_r()
    else:
        Ussr.released_r()

    if ismousepressed:
        if prevx != None:
            pygame.draw.line(drawing, brush_color, (mx, my), (prevx, prevy), brush_width)
        prevx = mx
        prevy = my
    elif not pressedkey[K_LSHIFT]:
        prevx = None

    if ukraine.is_finished() and not is_ukraine_action_started:
        is_ukraine_action_started = True
        mixer.music.load("secret.ogg")
        mixer.music.play(0)
        pygame.draw.rect(win,(75,75,255),(0,0,WINX,400))
        pygame.draw.rect(win,(255,255,0),(0,400,WINX,WINY))

    pygame.draw.rect(drawing, (txt.text.act_rect_color), txt.text.activation_rect)

    if is_ussr_action_started:
        is_ussr_action_started = False

    Ussr.Ussr_state_check()

    if not is_ukraine_action_started:
        win.fill(BGCOLORLIST[bg_color_index])

    win.blit(drawing,(0,0))
    win.blit(alpha,(0,0))
    win.blit(scrolling_things,(0,0))
    alpha.fill(empty)
    scrolling_things.fill(empty)
    pygame.time.delay(0)
    pygame.display.update()