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

# defining the blocks
# each shape is contained within a 3x3 matrix
# each list contains the coordinates that this particular shape occupies in that matrix
blocks = [
    [[1, 4, 7], [3, 4, 5]],  # 0: straight shape
    [[1, 3, 4, 5, 7]],  # 1: cross shape
    [[0, 1, 4, 5], [1, 3, 4, 6]],  # 2: two on two 1 shape
    [[1, 2, 3, 4], [0, 3, 4, 7]],  # 3: two on two 2 shape
    [[0, 1, 3, 6], [0, 1, 2, 5], [2, 5, 7, 8], [3, 6, 7, 8]],  # 4: L 1 shape
    [[1, 2, 5, 8], [5, 6, 7, 8], [0, 3, 6, 7], [0, 1, 2, 3]],  # 5: L 2 shape
    [[4, 6, 7, 8], [0, 3, 4, 6], [0, 1, 2, 4], [2, 4, 5, 8]]  # 6: one on three
]
# block class
class Block:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = 1   # select the shape from the blocks list
        self.rotation = 0   # select the variation of the shape (ex: straight vs. rotated) from the blocks list
    
    # pick the shape from the list based on the values in the constructor above
    def shape(self):
        return blocks[self.type][self.rotation]

# draw block function
def draw_block():
    # 3x3 matrix
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                pygame.draw.rect(screen, (255, 255, 255), 
                                 # x: location of block in its 3x3 matrix
                                 # block.x: location that we want on the grid
                                 # + 1 and - 2: so the block does not overlap with grid
                                 [(x + block.x) * grid_size + x_gap + 1, 
                                 (y + block.y) * grid_size + y_gap + 1,
                                 grid_size - 2, 
                                 grid_size - 2])

# grid size, cols, rows, x and y gaps variables to draw grid
grid_size = 30
cols = screen.get_width() // grid_size
rows = screen.get_height() // grid_size
x_gap = (screen.get_width() - cols * grid_size) // 2
y_gap = (screen.get_height() - rows * grid_size) // 2

# main game loop
game_over = False
clock = pygame.time.Clock()
# block object to test
block = Block(5, 6)
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
    # draw block to test
    draw_block()
    # update display after each iteration
    pygame.display.update()

# exit
pygame.quit()