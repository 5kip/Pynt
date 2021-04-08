import pygame

pygame.init()
from pygame import *

WINX = 1250
WINY = 726

empty = (0,0,0,0)
win = pygame.display.set_mode((WINX, WINY))
alpha = pygame.Surface((WINX, WINY),pygame.SRCALPHA)

pygame.display.set_caption("Pynt 0.5")

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

colors = [(255,0,0),(255,132,0),(255,255,0),(0,255,0),(0,255,255),(31,79,255),(95,0,184),(255,0,255)]

run = True
while run:
    mx, my = pygame.mouse.get_pos()
    startx = 10
    endx = 75
    starty = 10 
    endy = 75
    pygame.draw.rect(win,(112,112,112),(0,0,1250,100))
    a = 0
    for _a in range(len(colors)):
        pygame.draw.rect(win,colors[_a],(startx,starty,BUTTONWIDTH,BUTTONWIDTH))
        startx = endx + 10 
        endx = startx + BUTTONWIDTH
    circlex = startx + RADIUS
    pygame.draw.circle(win,(255,255,255),(circlex,45),(32))
    circlex = circlex + RADIUS + 10 + RADIUS
    pygame.draw.circle(win,(0,0,0000),(circlex,42),(32))
    pygame.draw.line(win,(255,0,0),(760,75),(825,10),10)
    pygame.draw.line(win,(255,0,0),(760,10),(825,75),10) 
    pygame.draw.circle(win,(255,255,255),(1190,50),(width*0.5))

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
    if mx ==SCREENEDGEXRIGHT:
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
                pygame.draw.rect(win,(0,0,0),(0,100,WINX,WINY))
                pygame.draw.line(alpha,(0,0,0,30),(startx,endy),(endx,starty),10)
                pygame.draw.line(alpha,(0,0,0,30),(startx,starty),(endx,endy),10)
                win.blit(alpha,(0,0))

    if prevx != None:
        if ismousepressed == True:
                pygame.draw.line(win,(brushcolor),(mx,my),(prevx,prevy),width)

    alpha.fill(empty)
    prevx = mx
    prevy = my
    pygame.time.delay(0)
    pygame.display.update()