import pygame
from pygame.locals import *

def draw_block():
    surface.fill((255, 255,255))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((800, 800))
    surface.fill((255, 255, 255))
    block = pygame.image.load("resources/block.jpg").convert()
    block_x, block_y = 350, 300
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_LEFT:
                    if((block_x-100)>0):
                        block_x -= 100
                    else:
                        block_x=0

                if event.key == K_RIGHT:
                    if (block_x+100)>=760:
                        block_x = 759
                    else:
                        block_x +=100

                if event.key == K_UP:
                    block_y -= 100

                if event.key == K_DOWN:
                    block_y += 100


                draw_block()

            elif event.type == QUIT:
                event
                running = False

