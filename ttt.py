import pygame
from pygame.locals import *
winning_combo = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("TTT")
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
turn = "x"
board_dict = {}
winner = False
for i in range(1,10,1):
    board_dict[i] = ""
def drawX(x,y):
    pygame.draw.line(screen, red, (x,y), (x+200,y+200), 5)
    pygame.draw.line(screen, red, (x+200, y), (x, y+200),5)
def drawO(x, y):
    pygame.draw.circle(screen, blue, (x+100, y+ 100), 100, 5)
def checkWinner(board, turn):
    for combo in winning_combo:
        print(board[combo[0]], board[combo[1]], board[combo[2]])
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == turn:
            print("Winner is", turn)
            
while True:
    pygame.display.update()
    for i in range(0, 600, 200):
        for j in range(0, 600, 200):
            pygame.draw.rect(screen, green, (i, j, 200, 200), 5)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            spot = x//200 +(y//200*3) + 1
            board_dict[spot] = turn
            
            if turn == "x":
                drawX(x//200*200, y//200*200)
                checkWinner(board_dict, turn)
                turn = "o"
            elif turn == "o":
                drawO(x//200*200, y//200*200)
                checkWinner(board_dict, turn)
                turn = "x"
