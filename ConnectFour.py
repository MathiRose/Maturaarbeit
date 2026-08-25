import pygame
import sys
import keyboard
from enum import Enum


BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
YELLOW = (255,255,0)
RED = (255,0,0)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 700
colour = YELLOW
board = [[BLACK] * 6 for _ in range(7)]
x = 3
y = 0

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    global colour
    global board
    global x 
    global y 
    
    while True:
        SCREEN.fill(BLACK)
        drawGrid()
        drawBoard()
        drawCircle(x,y,colour)

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
                    placeChip(x)
                    
        
        pygame.display.update()
   
    
def drawGrid():
    blockSize = 100 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)


def drawCircle(x,y,colour):
    pygame.draw.circle(SCREEN, colour, (x*100+50,y*100+50), 40)


def drawBoard():
    for i in range(7):
        for j in range(6):
            drawCircle(i,7-j,board[i][j])


def placeChip(x):
    global colour
    global board
    
    for i in range(6):
        if board[x][i] == BLACK:
            board[x][i] = colour

            if checkWin() == True:
                Win()
                return
            
            if checkDraw() == True:
                print('draw')
                return

            if colour == YELLOW:
                colour=RED
            else:
                colour=YELLOW
            break


def checkWin():

    #check columns
    for column in board:
        for i in range(3):
            if column[i] != BLACK and column[i:i+4].count(column[i]) == 4:
                return True
            
    #check rows
    for i in range(4):
        for j in range(6):
            if board[i][j] != BLACK and [board[i+k][j] for k in range(4)].count(board[i][j]) == 4:
                return True
            
    #check diagonals
    #up-right
    for i in range(4):
        for j in range(3):
            if board[i][j] != BLACK and [board[i+k][j+k] for k in range(4)].count(board[i][j]) == 4:
                return True
            
    #up-left
    for i in range(4):
        for j in range(3):
            if board[i+3][j] != BLACK and [board[i-k+3][j+k] for k in range(4)].count(board[i+3][j]) == 4:
                return True


def Win():
    if colour == YELLOW:
        print('Yellow won')
    else:
        print('Red won')
    reset()
    

def checkDraw():
    for col in board:
        if BLACK in col:
            return
        
    return True
        

def reset():
    global colour
    global board
    global x
    global y
    colour = YELLOW
    board = [[BLACK] * 6 for _ in range(7)]
    x = 3
    y = 0


main()