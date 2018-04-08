import pygame
from pygame.locals import *
from ahmad_ballClass import Ball
import random
pygame.init()
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255,255,255)
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Pong")

#Player1 variables
player1_score = 0
paddle_1x = 20
paddle_1y = 250
#Player2 Variables
player2_score = 0
paddle_2x = 580
paddle_2y = 250

#Paddle Variables
pad_width = 10
pad_height = 100

#Calling Ball Class
firstBall = Ball(300, 300, 10, white)

#Xchange YChange
xchange = 1
ychange = random.randint(1,5)

def show_text(msg, x, y, color):
    fontobj = pygame.font.SysFont("freesans", 32)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (x,y))


while True:
    screen.fill(black)
    show_text("Score: " + str(player1_score), 10, 10, blue)
    show_text("Score: " + str(player2_score), 450, 10, blue)
    pygame.draw.rect(screen, red, (paddle_1x, paddle_1y, pad_width, pad_height))
    pygame.draw.rect(screen, red, (paddle_2x, paddle_2y, pad_width, pad_height))
    firstBall.drawBall(screen)
    firstBall.changeXY(xchange, ychange)
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
    pygame.display.update()
    
    if keys[K_UP]:
        paddle_2y = paddle_2y - 3
    if keys[K_DOWN]:
        paddle_2y = paddle_2y + 3
    if keys[K_w]:
        paddle_1y = paddle_1y - 3
    if keys[K_s]:
        paddle_1y = paddle_1y +3
        
    if firstBall.y <= 0 + firstBall.radius or firstBall.y >= 600 - firstBall.radius:
        ychange = -ychange
    if firstBall.x <= 0 + firstBall.radius:
        xchange = 1
        ychange = random.randint(1, 5)
        player2_score += 1
    if firstBall.x >= 600 - firstBall.radius:
        xchange = -1
        ychange = random.randint(1, 5)
        player1_score += 1
    if firstBall.x - firstBall.radius == paddle_1x and firstBall.y - firstBall.radius >= paddle_1y and firstBall.y - firstBall.radius <= paddle_1y + pad_height and xchange <= 0:
        xchange = -(xchange - 1)

    if firstBall.x + firstBall.radius == paddle_2x and firstBall.y + firstBall.radius >= paddle_2y and firstBall.y + firstBall.radius <= paddle_2y + pad_height and xchange >= 0:
        xchange = -(xchange + 1)
