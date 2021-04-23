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

themesactive = None
lshiftpressed = None
prevx = None
prevy = None
ismousepressed = False
width = 1
brushcolor = (255,255,255) 
RADIUS = 32
BUTTONWIDTH = 65
BUTTONSPACING = 10
ishighlighted = False
SCREENEDGEXLEFT = 1
SCREENEDGEXRIGHT = WINX-1
SCREENEDGEYUP = 1
SCREENEDGEYDOWN = WINY-1
WIDTHCIRCLEPOS = (1190,50)
BGCOLORLIST =([0,0,0],[100,100,100],[200,200,200],[255,255,255],[100,100,255])
BGCLRIndex = 0
cleared = None
nextbgcolor = 1
bgcolorlistlen = len(BGCOLORLIST)
BGChangeButtonColor = BGCOLORLIST[nextbgcolor]
currentukraine = 0
maxukraine = 4
yellowallowed = False
bgallowed = False
OHYEAUKRAINE = False

def drawcross(middlex , rightdown):
    pygame.draw.line(drawing,(255,0,0),(middlex,75),(825,10),10)
    pygame.draw.line(drawing,(255,0,0),(middlex,10),(825,75),10)
#def checkforukraine():
    #if currentukraine >= neededukraine:
        #neededukraine = neededukraine + 1
        #currentukraine = currentukraine + 1
        #if currentukraine == maxukraine:
            #neededukraine = 0
            #currentukraine = 0
    #elif currentukraine == maxukraine:
        #currentukraine = 0
        #neededukraine =  0
def ClearUkraine():
    currentukraine = 0
    neededukraine = 0
    yellowallowed = False
    bgallowed = False


colors = [(255,0,0),(255,132,0),(255,255,0),(0,255,0),(0,255,255),(31,79,255),(95,0,184),(255,0,255)]

run = True
while run:
    neededukraine = 0
    if cleared:
        drawing.fill(empty)
        cleared = False
    pressedkey = pygame.key.get_pressed()
    mx, my = pygame.mouse.get_pos()
    startx = 10
    endx = 75
    starty = 10 
    endy = 75
    pygame.draw.rect(drawing,(112,112,112),(0,0,WINX,100))
    a = 0
    #K_LSHIFT
    for _a in range(len(colors)):
        pygame.draw.rect(drawing,colors[_a],(startx,starty,BUTTONWIDTH,BUTTONWIDTH))
        startx = endx + 10 
        endx = startx + BUTTONWIDTH
    circlex = startx + RADIUS
    pygame.draw.circle(drawing,(255,255,255),(circlex,45),(32))
    circlex = circlex + RADIUS + 10 + RADIUS
    pygame.draw.circle(drawing,(0,0,0000),(circlex,42),(32))
    startx = endx + 10
    endx = startx + BUTTONWIDTH
    startx = endx + 10 
    endx = startx + BUTTONWIDTH
    drawcross(startx, endx)
    pygame.draw.circle(drawing,(brushcolor),WIDTHCIRCLEPOS,width*0.5)

    startx = 10
    endx = 75
    starty = 10
    endy = 75

# рисует песочные часы лол    pygame.draw.polygon(win,(255,255,255), [(mx,my),(mx10,my10),(mx,my10),(mx10,my)])
    if my == SCREENEDGEYDOWN:
        ismousepressed = False 
    if my == SCREENEDGEYUP:
        ismousepressed = False 
    if mx == SCREENEDGEXLEFT:
        ismousepressed = False 
    if mx == SCREENEDGEXRIGHT:
        ismousepressed = False 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            ismousepressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            ismousepressed = False
        if event.type == pygame.MOUSEWHEEL:
            if width == 50:
                width = 1
                pygame.draw.circle(win,(112,112,112),(1190,50),(25))
            else:
                width = width + 1

  
#цвета
    if my <= 100:
        if ismousepressed == True:
            ismousepressed = False
            for _a in range(len(colors)):
                if mx <=endx and mx >= startx :
                    brushcolor = colors[_a]
                    pygame.draw.rect(alpha,(0,0,0,100),(startx,starty,BUTTONWIDTH,BUTTONWIDTH))
                    win.blit(alpha,(0,0))
                startx = endx + BUTTONSPACING
                endx = startx + BUTTONWIDTH      
            
            circlex = startx + RADIUS
            
            if mx >= startx and mx >= startx :
                pygame.draw.circle(alpha,(0,0,0,25),(circlex,45),(32))
                brushcolor = (255,255,255)
                win.blit(alpha,(0,0))
            startx = endx + BUTTONSPACING
            endx = startx + BUTTONWIDTH
            circlex = startx + RADIUS
            if mx <= endx and mx >= startx :
                brushcolor = (0,0,0)
            startx = endx + BUTTONSPACING
            endx = startx + BUTTONWIDTH
            circlex = startx + RADIUS
            if mx <= endx and mx >= startx :
                cleared = True
                drawcross(startx,endx)
                win.blit(alpha,(0,0))
        startx = endx + BUTTONSPACING
        endx = startx + BUTTONWIDTH    
        if brushcolor == colors[(5)]:
            if currentukraine == neededukraine:
                neededukraine = neededukraine + 1
                сurrentukraine = currentukraine + 1
                yellowallowed = True
            elif currentukraine == maxukraine:
                neededukraine = 0
                currentukraine = 0
        else:
            ClearUkraine()
    if brushcolor == colors[2]:
        if yellowallowed:
            if currentukraine == neededukraine:
                neededukraine = neededukraine + 1
                currentukraine = currentukraine + 1
                bgallowed = True
            elif currentukraine == maxukraine:
                neededukraine = 0
                currentukraine = 0
    else:
        ClearUkraine()

    if mx > WINX-30 and my > WINY-30 and ismousepressed:
        if pressedkey[K_u]:
            if currentukraine >= neededukraine:
                neededukraine = neededukraine + 1
                currentukraine = currentukraine + 1
            elif currentukraine == maxukraine:
                neededukraine = 0
                currentukraine = 0
        else:
            ClearUkraine()
        nextbgcolor = nextbgcolor + 1
        BGCLRIndex = BGCLRIndex + 1
        nextbgcolor = nextbgcolor % bgcolorlistlen
        BGCLRIndex = BGCLRIndex % bgcolorlistlen
        ismousepressed = False 
    pygame.draw.circle(drawing,BGCOLORLIST[nextbgcolor],(WINX-15,WINY-15),10)
    pygame.draw.rect(win,(BGCOLORLIST[BGCLRIndex]),(0,0,WINX,WINY))

    if ismousepressed:
        if prevx != None:
            pygame.draw.line(drawing,(brushcolor),(mx,my),(prevx,prevy),width)
        prevx = mx
        prevy = my
    elif not pressedkey[K_LSHIFT]:
        prevx = None

    if currentukraine == 3:
        OHYEAUKRAINE = True
    if OHYEAUKRAINE:
        mixer.music.load("secret.ogg")
        mixer.music.play(-1)
        pygame.draw.rect(win,(75,75,255),(0,0,WINX,400))
        pygame.draw.rect(win,(255,255,0),(0,400,WINX,WINY))

    win.blit(drawing,(0,0))
    alpha.fill(empty)
    pygame.time.delay(0)
    pygame.display.update()