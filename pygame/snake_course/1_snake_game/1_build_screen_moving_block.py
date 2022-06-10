import pygame
from pygame.locals import *

def draw_block():
    global red
    surface.fill((red, 0,0))
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
                    block_x -= 10
                if event.key == K_RIGHT:
                    block_x += 10
                if event.key == K_UP:
                    block_y -= 10
                if event.key == K_DOWN:
                    block_y += 10

                draw_block()

            elif event.type == QUIT:
                event
                running = False

