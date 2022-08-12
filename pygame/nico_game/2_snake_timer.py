import pygame
import time
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

directions={"RIGHT":"incX()",
            "LEFT" :"decX()",
            "UP"   :"decY()",
            "DOWN" :"incY()"
            }

keys={ K_LEFT :"LEFT",
       K_RIGHT:"RIGHT",
       K_UP   :"UP",
       K_DOWN :"DOWN"
       }

if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((ARENA_SIZE,ARENA_SIZE))
    x=0
    y=0

    actualDir="DOWN"
    while True:
        surface.fill(ARENA_COLOR)
        drawSnakeHead(x,y)
        drawGrid()
        pygame.display.flip()

        changed=False
        for i in range(10):
            if changed==False:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        actualDir=keys[event.key]
                        changed=True
            time.sleep(0.01)

        eval(directions[actualDir])
