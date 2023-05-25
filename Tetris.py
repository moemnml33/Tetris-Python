import pygame
from pygame.locals import *
pygame.init()
# create window
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Tetris")

# draw grid function
def draw_grid(cols, rows, grid_size, x_gap, y_gap):
    for y in range(rows): # rows
        for x in range(cols): # columns
            # draw rect onto screen, colour grey, rectangle parameters, draw border only
            pygame.draw.rect(screen, (100, 100, 100), 
                             [x * grid_size + x_gap, y * grid_size + y_gap, grid_size, grid_size], 1)

# grid size, cols, rows, x and y gaps variables to draw grid
grid_size = 30
cols = screen.get_width() // grid_size
rows = screen.get_height() // grid_size
x_gap = (screen.get_width() - cols * grid_size) // 2
y_gap = (screen.get_height() - rows * grid_size) // 2

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
    
    # draw grid
    draw_grid(cols, rows, grid_size, x_gap, y_gap)
    
    # update display after each iteration
    pygame.display.update()

# exit
pygame.quit()