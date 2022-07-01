import pygame
import time
from pygame.locals import *

FRAME_RATE = 0.5
BLOCK_SIZE = 123
ARENA_SIZE = 300
STEP_SIZE = 10

if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((ARENA_SIZE,ARENA_SIZE))
    surface.fill((255, 255, 255))
    block_x, block_y = 0, 0
#    block = pygame.image.load("resources/block.jpg").convert()
    #surface.blit(block, (block_x, block_y))
    pygame.draw.rect(surface, (100,45,100), pygame.Rect(block_x,block_y,BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.flip()
    running = True
    while running:

        #izq a derecha
        for contador in range(int((ARENA_SIZE-BLOCK_SIZE) / STEP_SIZE)):
            block_x += STEP_SIZE
            surface.fill((255, 255,255))
            print("x normal",block_x)
            pygame.draw.rect(surface, (100,45,100), pygame.Rect(block_x,block_y,BLOCK_SIZE, BLOCK_SIZE))
            #surface.blit(block, (block_x, block_y))
            pygame.display.flip()
            time.sleep(FRAME_RATE)

        block_x += ((ARENA_SIZE-BLOCK_SIZE) % STEP_SIZE)
        print("x resto",block_x)
        surface.fill((255, 255,255))
        pygame.draw.rect(surface, (100,45,100), pygame.Rect(block_x,block_y,BLOCK_SIZE, BLOCK_SIZE))
        #surface.blit(block, (block_x, block_y))
        pygame.display.flip()
        time.sleep(FRAME_RATE)

        for contador in range(int((ARENA_SIZE-BLOCK_SIZE)/STEP_SIZE)):
            surface.fill((255, 255,255))
            block_y += STEP_SIZE
            print("y normal",block_y)
            pygame.draw.rect(surface, (100,45,100), pygame.Rect(block_x,block_y,BLOCK_SIZE, BLOCK_SIZE))
            #surface.blit(block, (block_x, block_y))
            pygame.display.flip()
            time.sleep(FRAME_RATE)

        block_y += ((ARENA_SIZE-BLOCK_SIZE) % STEP_SIZE)
        print("y resto",block_y)
        surface.fill((255, 255,255))
        pygame.draw.rect(surface, (100,45,100), pygame.Rect(block_x,block_y,BLOCK_SIZE, BLOCK_SIZE))
        #surface.blit(block, (block_x, block_y))
        pygame.display.flip()
        time.sleep(FRAME_RATE)

        for contador in range(int((ARENA_SIZE-BLOCK_SIZE) / STEP_SIZE)):
            block_x -= STEP_SIZE
            surface.fill((255, 255,255))
            print("x normal",block_x)
            pygame.draw.rect(surface, (100,45,100), pygame.Rect(block_x,block_y,BLOCK_SIZE, BLOCK_SIZE))
            #surface.blit(block, (block_x, block_y))
            pygame.display.flip()
            time.sleep(FRAME_RATE)

        block_x -= ((ARENA_SIZE-BLOCK_SIZE) % STEP_SIZE)
        print("x resto",block_x)
        surface.fill((255, 255,255))
        pygame.draw.rect(surface, (100,45,100), pygame.Rect(block_x,block_y,BLOCK_SIZE, BLOCK_SIZE))
        #surface.blit(block, (block_x, block_y))
        pygame.display.flip()
        time.sleep(FRAME_RATE)

        for contador in range(int((ARENA_SIZE-BLOCK_SIZE)/STEP_SIZE)):
            surface.fill((255, 255,255))
            block_y -= STEP_SIZE
            print("y normal",block_y)
            pygame.draw.rect(surface, (100,45,100), pygame.Rect(block_x,block_y,BLOCK_SIZE, BLOCK_SIZE))
            #surface.blit(block, (block_x, block_y))
            pygame.display.flip()
            time.sleep(FRAME_RATE)

        block_y -= ((ARENA_SIZE-BLOCK_SIZE) % STEP_SIZE)
        print("y resto",block_y)
        surface.fill((255, 255,255))
        pygame.draw.rect(surface, (100,45,100), pygame.Rect(block_x,block_y,BLOCK_SIZE, BLOCK_SIZE))
        #surface.blit(block, (block_x, block_y))
        pygame.display.flip()
        time.sleep(FRAME_RATE)

#        for contador in range(int((ARENA_SIZE-BLOCK_SIZE)/STEP_SIZE)+1):
#            block_x -= STEP_SIZE
#            surface.fill((255, 255,255))
#            print(block_x)
#            pygame.draw.rect(surface, (100,45,100), pygame.Rect(block_x,block_y,BLOCK_SIZE, BLOCK_SIZE))
#            #surface.blit(block, (block_x, block_y))
#            pygame.display.flip()
#            time.sleep(FRAME_RATE)
#
#        block_x += STEP_SIZE
#
#        for contador in range(int((ARENA_SIZE-BLOCK_SIZE)/STEP_SIZE)+1):
#            block_y -= STEP_SIZE
#            surface.fill((255, 255,255))
#            print(block_y)
#            pygame.draw.rect(surface, (100,45,100), pygame.Rect(block_x,block_y,BLOCK_SIZE, BLOCK_SIZE))
#            #surface.blit(block, (block_x, block_y))
#            pygame.display.flip()
#            time.sleep(FRAME_RATE)
#
#        block_y += STEP_SIZE
##
##        for event in pygame.event.get():
##            if event.type == KEYDOWN:
##                if event.key == K_ESCAPE:
##                    running = False
##
##                if event.key == K_LEFT:
##                    block_x -= 10
##                    surface.fill((255, 255,255))
##                    surface.blit(block, (block_x, block_y))
##                    pygame.display.flip()
##
##                if event.key == K_RIGHT:
##                    pygame.display.flip()
##
##            elif event.type == QUIT:
##                event
##                running = False
##
