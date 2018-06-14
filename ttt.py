import pygame
from pygame.locals import *
winning_combo = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("TTT")
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

def drawX(x,y):
    pygame.draw.line(screen, red, (x,y), (x+200,y+200), 5)
    pygame.draw.line(screen, red, (x+200, y), (x, y+200),5)

while True:
    pygame.display.update()
    for i in range(0, 600, 200):
        for j in range(0, 600, 200):
            pygame.draw.rect(screen, green, (i, j, 200, 200), 5)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            spot = x//200 +(y//200*3)
            print(x, y)
            print(spot)
            drawX(x//200*200, y//200*200)
