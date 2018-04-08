import pygame
class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius;
        self.color = color;


    def changeXY(self, xchange, ychange):
        self.x = self.x + xchange
        self.y = self.y + ychange

    def drawBall(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        
