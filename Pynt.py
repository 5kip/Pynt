import time as tim
import pygame

pygame.init()
from pygame import *

win = pygame.display.set_mode((1250, 726))

pygame.display.set_caption("Pynt 0.3")

prevx = None
prevy = None
mousepressed = False
width = 1
brushcolor = (255,255,255) 
RADIUS = 32


pygame.draw.polygon(win,(112,112,112),[(0,100),(1250,100),(1250,0),(0,0)])
colors = [(255,0,0),(255,132,0),(255,255,0),(0,255,0),(0,255,255),(31,79,255),(95,0,184),(255,0,255)]




run = True
while run:
    mx, my = pygame.mouse.get_pos()

    startx = 10
    endx = 75
    starty = 10 
    endy = 75
   
    a = 0
    for _a in range(len(colors)):
        pygame.draw.polygon(win,colors[_a],[(startx,endy),(endx,endy),(endx,starty),(startx,starty)])
        startx = endx + 10 
        endx = startx + 65
    startx= endx + 74
    pygame.draw.circle(win,(255,255,255),(midx,45),(32))
    startx= endx + 74
    pygame.draw.circle(win,(0,0,0000),(,42),(32))
    pygame.draw.line(win,(255,0,0),(760,75),(825,10),10)
    pygame.draw.line(win,(255,0,0),(760,10),(825,75),10) 
    pygame.draw.circle(win,(255,255,255),(1190,50),(width*0.5))

# рисует песочные часы лол    pygame.draw.polygon(win,(255,255,255), [(mx,my),(mx10,my10),(mx,my10),(mx10,my)])

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousepressed = False
        if event.type == pygame.MOUSEWHEEL:
            if width == 50:
                width = 1
                pygame.draw.circle(win,(112,112,112),(1190,50),(25))
            else:
                width = width + 1
        #цвета
        if my <= 100:
            if mousepressed == True:
                if mx <= 75:
                    brushcolor = (255,0,0)
                    pygame.draw.polygon(win,(200,0,0),[(10,75),(75,75),(75,10),(10,10)])
                if mx <= 150:
                    if mx >= 85:
                        brushcolor = (255,132,0)
                if mx <= 225:
                    if mx >= 160:
                        brushcolor = (255,255,0)
                if mx <= 300:
                    if mx >= 235:
                        brushcolor =(0,255,0)
                if mx <= 375:
                    if mx >= 310:
                        brushcolor = (0,255,255)
                if mx <= 450:
                    if mx >= 385:
                        brushcolor = (31,79,255)
                if mx <= 525:
                    if mx >= 460:
                        brushcolor = (95,0,184)
                if mx <= 600:
                    if mx >= 535:
                        brushcolor = (255,0,255)
                if mx <= 675:
                    if mx >= 610:
                        brushcolor = (255,255,255)
                if mx <= 750:
                    if mx >= 685:
                        brushcolor = (0,0,0)
                if mx <= 825:
                    if mx >= 760:
                        pygame.draw.polygon(win,(0,0,0),[(0,101),(0,726),(1250,726),(1250,101),(0,101)])
                if my >= 100:
                    break

    if prevx != None:
        if mousepressed == True:
            if pygame.mouse.get_pos()[1] >= 150:
                pygame.draw.line(win,(col),(mx,my),(prevx,prevy),width)

    prevx = mx
    prevy = my
    pygame.time.delay(0)
    pygame.display.update()