import pygame
from pygame.locals import *
import time
import random
screen = pygame.display.set_mode((600,600))
class ship:
    def __init__(self, x, y, width, height, health, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.health = health
        self.bullets = 5

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x\
                                              ,self.y, self.width, self.height))

    def moveShip(self, move):
        self.x += move
        if self.x >= 600:
            self.x = 600 - self.width
        if self.x <= 0:
            self.x = 0
    def moveToSpot(self, newlocation):
        if self.x < newlocation:
            self.x +=1
        elif self.x > newlocation:
            self.x -= 1
        else:
            return True
        return False


class bullets:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 5, 5))

    def move(self, move):
        self.y += move
    def checkCollision(self, enemy, bullet_list):
        if self.x >= enemy.x and\
            self.y >= enemy.y and\
            self.x <= enemy.x + int(enemy.width) and\
            self.y <= enemy.y + int(enemy.height):
                print("enemy_hit")
                enemy.health -= 1
                bullet_list.remove(self)
        if self.y < 0 or self.y > 600:
            if self in bullet_list:
                bullet_list.remove(self)

blue = (0,0,255)
colored = (1,125,250)
green = (0,255,0)
player = ship(300, 550, 50, 50, 5, green)

computerMove = False
playerShot = False
enemyShot = False
moveLeft = False
moveRight = False
reloadStart = False
playerBullets = []
enemyBullets = []
reloadTime = 2
enemy = ship(300, 0, 50, 50, 5,blue)
enemylist = []
new_location = 0
reach_location = True
for i in range(10):
    tex = random.randint(0, 580)
    tey = random.randint(70, 540) 
    tinyenemy = ship(tex, tey, 20, 10, 1,colored)
    enemylist.append(tinyenemy)
while True:
    currentTime = time.time()
    pygame.display.update()
    screen.fill((0,0,0))
    player.draw()
    if enemy.health > 0:
        enemy.draw()
    for te in enemylist:
        if te.health == 0:
            enemylist.remove(te)
        te.draw()
    if computerMove == True:
        if currentTime - moveTime >= 1 and enemy.health > 0:
            if reach_location == True:
                new_location = random.randint(50, 550)//5 * 5
                reach_location = False
            bullet = bullets(enemy.x + int(enemy.width/2), enemy.y + enemy.height)
            enemyBullets.append(bullet)
            computerMove = False
        reach_location = enemy.moveToSpot(new_location)
    if computerMove == False:
        moveTime = time.time()
        computerMove = True
    if moveLeft:
        player.moveShip(-1)
    if moveRight:
        player.moveShip(1)
    if playerShot == True:
        for i in playerBullets:
            i.draw()
            i.move(-1)
            for te in enemylist:
                i.checkCollision(te, playerBullets)
            i.checkCollision(enemy, playerBullets)
            
    for i in enemyBullets:
        i.draw()
        i.move(1)
        i.checkCollision(player, enemyBullets)
    for i in range(player.bullets):
        pygame.draw.rect(screen, (255,0,0), (5 + i * 4, 570, 3, 5))
    if reloadStart == True:
        if currentTime - startTime >= reloadTime:
            player.bullets = 5
            reloadStart = False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                moveLeft = True
            if event.key == K_d:
                moveRight = True
            if event.key == K_w:
                if reloadStart == False and player.bullets > 0:
                    player.bullets -= 1
                    playerBullets.append(bullets(player.x + int(player.width/2), player.y))
                    playerShot = True
            if event.key == K_r:
                if reloadStart == False and player.bullets != 5:
                    print("Reloading")
                    reloadStart = True
                    startTime = time.time()
        if event.type == pygame.KEYUP:
            moveLeft= False
            moveRight = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos
            if reloadStart == False and player.bullets > 0:
                player.bullets -= 1
                playerBullets.append(bullets(player.x + int(player.width/2), player.y))
                playerShot = True
                
