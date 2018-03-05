from game import Game
import sys
import pygame
import time

SECONDS_PER_FRAME = 0.1


game = Game()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key = None
    start_time = time.time()
    while time.time() - start_time < SECONDS_PER_FRAME:
        if key not in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]: 
            key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        game.move('left')
    elif key[pygame.K_RIGHT]:
        game.move('right')
    elif key[pygame.K_DOWN]:
        game.move('down')
    elif key[pygame.K_UP]:
        game.move('up')
    else:
        game.move('continue')

    game.draw()
