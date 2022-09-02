import pygame
import time
import threads
from pygame.locals import *

GRID_COUNT = 10
ARENA_SIZE = 600
BLOCK_SIZE = ARENA_SIZE // GRID_COUNT
SNAKE_COLOR = (200,0,0)
GRID_COLOR  = (200,200,200)
ARENA_COLOR = (255,255,255)

def drawSnakeHead(x,y):
    pygame.draw.rect(surface,SNAKE_COLOR , pygame.Rect(BLOCK_SIZE*x,BLOCK_SIZE*y,BLOCK_SIZE, BLOCK_SIZE))

def drawHLine(y):
    pygame.draw.line(surface,GRID_COLOR,(0 , BLOCK_SIZE*y),(ARENA_SIZE-1,BLOCK_SIZE*y),1)

def drawVLine(x):
    pygame.draw.line(surface,GRID_COLOR,(BLOCK_SIZE*x,0),(BLOCK_SIZE*x,ARENA_SIZE-1),1)

def drawGrid():
    for i in range(GRID_COUNT):
        drawHLine(i)
        drawVLine(i)

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

c = pygame.time.Clock()
print(c.tick(10),type(c))

event=[]

if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((ARENA_SIZE,ARENA_SIZE))
    x=0
    y=0
    actualDir=K_DOWN
    while True:
        
        event += pygame.event.get()
        while len(event)>0:
            e=event[0]
            event.pop(0)
            if e.type == KEYDOWN:
                print(actualDir,e.key)
                if e.key in keys:
                    actualDir=e.key
                    break;

        eval(keys[actualDir])

        surface.fill(ARENA_COLOR)
        drawSnakeHead(x,y)
        drawGrid()
        pygame.display.flip()

        time.sleep(.5)


