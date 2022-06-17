import pygame
import time
from pygame.locals import *


if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((800, 800))
    surface.fill((255, 255, 255))
    block = pygame.image.load("resources/block.jpg").convert()
    block_x, block_y = 0, 0
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

    running = True
    while running:

        for contador in range(800-40):
            surface.fill((255, 255,255))
            surface.blit(block, (block_y, block_x))
            pygame.display.flip()
            block_x += 1
            time.sleep(0.01)

        for contador in range(800-40):
            block_x -= 1
            surface.fill((255, 255,255))
            surface.blit(block, (block_y, block_x))
            pygame.display.flip()
            time.sleep(0.01)
#
#        for event in pygame.event.get():
#            if event.type == KEYDOWN:
#                if event.key == K_ESCAPE:
#                    running = False
#
#                if event.key == K_LEFT:
#                    block_x -= 10
#                    surface.fill((255, 255,255))
#                    surface.blit(block, (block_x, block_y))
#                    pygame.display.flip()
#
#                if event.key == K_RIGHT:
#                    pygame.display.flip()
#
#            elif event.type == QUIT:
#                event
#                running = False
#
