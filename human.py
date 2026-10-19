import pygame
import sys
import keyboard
from enum import Enum
import environement


BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
YELLOW = (255,255,0)
RED = (255,0,0)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 700


def humanStr(board, player):
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    x = 3
    y = 0
    
    while True:
        SCREEN.fill(BLACK)
        drawGrid()
        drawBoard(board)
        if player == 1:
            drawCircle(x,y,YELLOW)
        else:
            drawCircle(x,y,RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x > 0:
                        x -= 1
                if event.key == pygame.K_RIGHT:
                    if x < 6:
                        x += 1
                if event.key == pygame.K_SPACE:
                    if x in environement.LegalMoves(board):
                        return environement.placeChip(x, board, player)

        pygame.display.update()
   
    
def drawGrid():
    blockSize = 100 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)


def drawCircle(x,y,colour):
    pygame.draw.circle(SCREEN, colour, (x*100+50,y*100+50), 40)


def drawBoard(board):
    for i in range(7):
        for j in range(6):
            if board[i][j] == 1:
                drawCircle(i,7-j,YELLOW)
            elif board[i][j] == 2:
                drawCircle(i,7-j,RED)


