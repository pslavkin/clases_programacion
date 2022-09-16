import pygame
import random
import time
import threads
from pygame.locals import *

GRID_COUNT = 10
ARENA_SIZE = 600
BLOCK_SIZE = ARENA_SIZE // GRID_COUNT
SNAKE_COLOR = (200 ,0   ,0)
TAIL_COLOR  = (0   ,0   ,255)
GRID_COLOR  = (200 ,200 ,200)
FOOD_COLOR  = (0 ,200   ,0)
ARENA_COLOR = (255 ,255 ,255)

def drawSnakeHead(x,y):
    pygame.draw.rect(surface,SNAKE_COLOR , pygame.Rect(BLOCK_SIZE*x,BLOCK_SIZE*y,BLOCK_SIZE, BLOCK_SIZE))
def drawSnakeTail(x,y):
    pygame.draw.rect(surface,TAIL_COLOR , pygame.Rect(BLOCK_SIZE*x,BLOCK_SIZE*y,BLOCK_SIZE, BLOCK_SIZE))

def drawHLine(y):
    pygame.draw.line(surface,GRID_COLOR,(0 , BLOCK_SIZE*y),(ARENA_SIZE-1,BLOCK_SIZE*y),1)

def drawVLine(x):
    pygame.draw.line(surface,GRID_COLOR,(BLOCK_SIZE*x,0),(BLOCK_SIZE*x,ARENA_SIZE-1),1)

def compareLimit(x,y):
    if x >= GRID_COUNT or x < 0 or y >= GRID_COUNT or y<0:
       ans=False
    else:
       ans=True
    return ans

def drawGrid():
    for i in range(GRID_COUNT):
        drawHLine(i)
        drawVLine(i)

def generateFood():
    x=int(random.uniform(0,GRID_COUNT))
    y=int(random.uniform(0,GRID_COUNT))
    return x,y

def drawFood(x,y):
    pygame.draw.rect(surface,FOOD_COLOR , pygame.Rect(BLOCK_SIZE*x,BLOCK_SIZE*y,BLOCK_SIZE, BLOCK_SIZE))

def eat(snakeX,snakeY,foodX,foodY):
    return snakeX==foodX and snakeY==foodY


def incX():
    global x
    x = x + 1
def decX():
    global x
    x = x - 1
def incY():
    global y
    y = y + 1
def decY():
    global y
    y = y - 1

keys={ K_LEFT :"decX()",
       K_RIGHT:"incX()",
       K_UP   :"decY()",
       K_DOWN :"incY()",
       }


event=[]
move_history=[]

if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((ARENA_SIZE,ARENA_SIZE))
    x=0
    y=0
    foodX=0
    foodY=0
    tailLenght=0
    actualDir=K_DOWN
    foodX,foodY=generateFood()

    while True:
        
        # lectura y parseo de teclas
        event += pygame.event.get()
        while len(event)>0:
            e=event[0]
            event.pop(0)
            if e.type == KEYDOWN:
                #print(actualDir,e.key)
                if e.key in keys:
                    actualDir=e.key
                    break;

        eval(keys[actualDir])

        surface.fill(ARENA_COLOR)
        if compareLimit(x,y)==False:
            print('game over')
            exit()
        drawFood(foodX,foodY)
        drawSnakeHead(x,y)
        # enganche de la cola de serpiente

        for i in range(-tailLenght,0):
            drawSnakeTail(move_history[i][0],move_history[i][1])

        if eat(x,y,foodX,foodY) == True:
            foodX,foodY=generateFood()
            tailLenght+=1
            print('comio')

        move_history.append([x,y])

        if len(move_history)>tailLenght:
            move_history.pop(0)
        #print(move_history)

        drawGrid()
        pygame.display.flip()
        time.sleep(.5/(tailLenght+1))


