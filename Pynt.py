import pygame

pygame.init()
from pygame import *
from pygame import mixer

mixer.init()

WINX = 1250
WINY = 726

empty = (0,0,0,0)

win = pygame.display.set_mode((WINX, WINY))
alpha = pygame.Surface((WINX, WINY),pygame.SRCALPHA)
drawing = pygame.Surface((WINX,WINY),pygame.SRCALPHA)

pygame.display.set_caption("Pynt 0.6")

prevx = None
prevy = None
ismousepressed = False
brush_width = 1
brush_color = (255,255,255) 
RADIUS = 32
BUTTONWIDTH = 65
BUTTONSPACING = 10
RESET_BACKGROUND_BUTTON_OFFSET = 30
MOUSE_LEFT_SCREEN_OFFSET = 1
WIDTHCIRCLEPOS = (1190,50)
BGCOLORLIST =([0,0,0],[100,100,100],[200,200,200],[255,255,255],[100,100,255])
bg_color_index = 0
is_ukraine_action_started = False
pressedkey = pygame.key.get_pressed()
CurrentBGColor = BGCOLORLIST[bg_color_index]

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
    final_state = 6

    def clicked_red():
        if state  != 0 :
            state  = 0
        else:
            state  = 1
    
    def clicked_yellow():
        if state != 1 :
            state = 0
        else:
            state = 2

    def pressed_r():
        if state != 2 :
            state = 0
        else:
            state = 3
    
    def BG_changed():
        if state != 3 or 4 or 5 or final_state :
            state = 0
        else:
            state = state + 1



def drawcross(middlex , rightdown):
    pygame.draw.line(drawing,(255,0,0),(middlex,75),(825,10),10)
    pygame.draw.line(drawing,(255,0,0),(middlex,10),(825,75),10)


colors = [(255,0,0,255),(255,132,0,255),(255,255,0,255),(0,255,0,255),(0,255,255,255),(31,79,255,255),(95,0,184,255),(255,0,255,255)]
BLUE_INDEX = 5
YELLOW_INDEX = 2


run = True
while run:
    pressedkey = pygame.key.get_pressed()
    mx, my = pygame.mouse.get_pos()

    startx = BUTTONSPACING
    endx = startx + BUTTONWIDTH

    starty = BUTTONSPACING 
    endy = starty + BUTTONWIDTH

    pygame.draw.rect(drawing,(112,112,112),(0,0,WINX,100))
    #K_LSHIFT
    for i in range(len(colors)):
        pygame.draw.rect(drawing,colors[i],(startx,starty,BUTTONWIDTH,BUTTONWIDTH))
        startx = endx + BUTTONSPACING 
        endx = startx + BUTTONWIDTH

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
                else:
                    ukraine.clicked_other_color()
                
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
            drawing.fill
            drawing.set_alpha(255)

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

# рисует песочные часы лол    pygame.draw.polygon(win,(255,255,255), [(mx,my),(mx10,my10),(mx,my10),(mx10,my)])
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
                ukraine.changed_bg()
        elif event.type == pygame.MOUSEWHEEL:
            if brush_width == 50:
                brush_width = 1
                pygame.draw.circle(win,(112,112,112),(1190,50),(25))
            else:
                brush_width = brush_width + 1

  
#цвета

    highlight_color()

    if pressedkey[K_u]:
        ukraine.pressed_u()
    else:
        ukraine.released_u()

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
        mixer.music.play(-1)
        pygame.draw.rect(win,(75,75,255),(0,0,WINX,400))
        pygame.draw.rect(win,(255,255,0),(0,400,WINX,WINY))


    win.blit(drawing,(0,0))
    win.blit(alpha,(0,0))
    alpha.fill(empty)
    pygame.time.delay(0)
    pygame.display.update()