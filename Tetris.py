import pygame
from pygame.locals import *
import random
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
            # if not black, then draw gameboard
            if game_board[x][y] != (0, 0, 0):
                pygame.draw.rect(screen, game_board[x][y], 
                             [x * grid_size + x_gap + 1, y * grid_size + y_gap + 1, grid_size - 2, grid_size - 2])

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
        self.type = random.randint(0, 6)   # select the shape from the blocks list
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
                                 # x: location of each specific block in its 3x3 matrix
                                 # block.x: location that we want on the grid
                                 # + 1 and - 2: so the block does not overlap with grid
                                 [(x + block.x) * grid_size + x_gap + 1, 
                                 (y + block.y) * grid_size + y_gap + 1,
                                 grid_size - 2, 
                                 grid_size - 2])

# collides function
def collides(next_x, next_y):
    collision = False
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                # if collides with the left or right of the screen
                if x + block.x + next_x < 0 or x + block.x + next_x > cols - 1:
                    collision = True
                    break
                # if collides with the top or bottom of the screen
                if y + block.y + next_y < 0 or y + block.y + next_y > rows - 1:
                    collision = True
                    break
                # if collides with the next element of the game board
                if game_board[block.x + x + next_x][block.y + y + next_y] != (0, 0, 0):
                    collision = True
                    break
    return collision

# drop block function
def drop_block():
    can_drop = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                # if block collides with another block or hits the bottom of the screen
                if collides(0, 1):
                    can_drop = False
    if can_drop:
        block.y += 1
    # if block reaches the bottom, set its colour to green and set it to None
    else:
        for y in range(3):
            for x in range(3):
                if y * 3 + x in block.shape():
                    game_board[block.x + x][block.y + y] = (0, 255, 0)
    return can_drop

# side move function
def side_move(dx):
    can_move = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                # if block collides with right or left edge
                if collides(dx, 0):
                    can_move = False

    if can_move:
        block.x += dx
    # if shape reaches left or right edge drop instead of holding
    else:
        drop_block()

# rotate function
def rotate():
    # save initial value, then check if rotation is possible
    last_rotation = block.rotation
    block.rotation = (block.rotation + 1) % len(blocks[block.type])
    can_rotate = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                # if block collides with the bottom, right and left edge
                if collides(0, 0):
                        can_rotate = False
    if not can_rotate:
        block.rotation = last_rotation 
    

# grid size, cols, rows, x and y gaps variables to draw grid
grid_size = 30
cols = screen.get_width() // grid_size
rows = screen.get_height() // grid_size
x_gap = (screen.get_width() - cols * grid_size) // 2
y_gap = (screen.get_height() - rows * grid_size) // 2

# game board
# initialize as a list containing blocks of colour black
game_board = []
for i in range(cols):
    new_col = []
    for j in range(rows):
        new_col.append((0, 0, 0))
    game_board.append(new_col)

# main game loop
game_over = False
clock = pygame.time.Clock()
fps = 8
# block object to test
block = Block((cols - 1)// 2, 0)
while not game_over:
    screen.fill((0, 0, 0))
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            continue
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rotate()
    # move left and right
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            side_move(-1)
        elif event.key == pygame.K_RIGHT:
            side_move(1)

    # draw grid
    draw_grid(cols, rows, grid_size, x_gap, y_gap)
    # if block is not none then draw it
    if block is not None:
        # draw block to test
        draw_block()
        # allow block to slide sideways
        if event.type != pygame.KEYDOWN:
            # draw block
            # if the shape reaches the bottom then we don't need it anymore
            # instead it's gonna be set to none and added to the gameboard
            # then create a new block at a random spot
            if not drop_block():
                block = None
                block = Block(random.randint(3 , cols - 3), 0)

    # update display after each iteration
    pygame.display.update()

# exit
pygame.quit()