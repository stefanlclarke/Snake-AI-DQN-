import pygame
import numpy as np
from Game import GameEnvironment
from Model import actor, get_network_input
import torch

gridsize = 13
framerate = 10
block_size = 20

model = actor(10, 20, 5)
model.load_state_dict(torch.load('./Models/DQN67150'))
epsilon = 0.0

board = GameEnvironment(gridsize, 0., -100., 100.)
windowwidth = gridsize*block_size*3
windowheight = gridsize*block_size

pygame.init()
win = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption("snake")
font = pygame.font.SysFont('arial', 10)
clock = pygame.time.Clock()

def drawboard(snake, apple):
    win.fill((0,0,0))
    for pos in snake.prevpos:
        pygame.draw.rect(win, (0,255,0), (pos[0]*block_size, pos[1]*block_size, block_size, block_size))
    pygame.draw.rect(win, (255, 0, 0), (apple.pos[0]*block_size, apple.pos[1]*block_size, block_size, block_size))

run = True
move=0
reward = 0.
while run:
    clock.tick(framerate)
    
    inp = get_network_input(board.snake, board.apple)
    out = model(inp)
    rand = np.random.uniform(0,1)
    if rand > epsilon:
        move = torch.argmax(out)
        randmove = False
    else:
        move = np.random.randint(0,5)
        randmove = True
    
    reward, done = board.update_boardstate(move)
    drawboard(board.snake, board.apple)
    
    newinp = get_network_input(board.snake, board.apple)
    inputtext = font.render('PREV INPUT: ' + str(inp), False, (255, 255, 255))
    newinputtext = font.render('NEW INPUT: ' + str(newinp), False, (255, 255, 255))
    outtext = font.render('OUTPUT ' + str(out), False, (255, 255, 255))
    epstext = font.render('MOVING RANDOMLY: ' + str(randmove), False, (255, 255, 255))
    movetext = font.render('MOVE ' + str(move), False, (255, 255, 255))
    rewardtext = font.render('REWARD: ' + str(reward), False, (255, 255, 255))
    donetext = font.render('DONE? ' + str(done), False, (255, 255, 255))
    
    win.blit(inputtext, (windowwidth//3, 0))
    win.blit(newinputtext, (windowwidth//3, 20))
    win.blit(outtext, (windowwidth//3, 40))
    win.blit(epstext, (windowwidth//3, 60))
    win.blit(movetext, (windowwidth//3, 80))
    win.blit(rewardtext, (windowwidth//3, 100))
    win.blit(donetext, (windowwidth//3, 120))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        paused = True
        while paused == True:
            clock.tick(10)
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    paused = False
    
    #reward, done = board.update_boardstate(move)
    pygame.display.update()
    
    if board.game_over == True:
        board.resetgame()
        
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    