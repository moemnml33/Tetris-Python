import pygame
from pygame.locals import *

pygame.init()
# create window
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Tetris")

# main game loop
game_over = False
clock = pygame.time.Clock()
while not game_over:
    # help limit the runtime speed of the game 
    # the program will never run at more than 50 frames per second. 
    dt = clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.fill((0, 0, 0))
    # update display after each iteration
    pygame.display.update()

# exit
pygame.quit()