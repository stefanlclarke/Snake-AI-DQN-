import pygame
import numpy as np
from Game import GameEnvironment

gridsize = 13
framerate = 10
block_size = 20

board = GameEnvironment(gridsize)
windowwidth = gridsize*block_size
windowheight = gridsize*block_size

pygame.init()
win = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption("snake")
font = pygame.font.SysFont('Comic Sans MS', 10)
clock = pygame.time.Clock()

def drawboard(snake, apple):
    win.fill((0,0,0))
    for pos in snake.prevpos:
        pygame.draw.rect(win, (0,255,0), (pos[0]*block_size, pos[1]*block_size, block_size, block_size))
    pygame.draw.rect(win, (255, 0, 0), (apple.pos[0]*block_size, apple.pos[1]*block_size, block_size, block_size))

run = True
move=0
while run:
    clock.tick(framerate)
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        move = 0
    if keys[pygame.K_d]:
        move = 1
    if keys[pygame.K_w]:
        move = 2
    if keys[pygame.K_s]:
        move = 3
    board.update_boardstate(move)
    drawboard(board.snake, board.apple)
    pygame.display.update()
    
    if board.game_over == True:
        board.resetgame()
        
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    