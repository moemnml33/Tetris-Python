# Tetris game 

The following is the recreation of the classic Tetris game with python using pygame, and the following is the game walkthrough.

# About the commits, building the game step-by-step:

## First commit - the game's infrastructure:

In the first step, we're just laying the infrastructure of the game; creating an empty window in which the game will be run.

![](images/first_commit.png)

## Second commit - the base grid:

In the second step, we're creating the base grid; using a draw_grid function, we iterate over the x's and y's of the window (columns and rows) and draw our grid where each block is made of a grey square. With the parameters the function takes, the grid dynamically adapts to any changes we make to the window size, number of rows and columns, and the grid size.

![](images/second_commit.png)

## Third commit - defining the blocks and displaying shapes:

In the thrid step, we define each shape to be contained in a 3x3 matrix. For example, a straight shape can be represented as the matrix:
[0 1 0 0 1 0 0 1 0]
where the 1's are the valid blocks, which can be represented as the list [1, 4, 7]. The same logic follows for the shape's rotation, and for all other shapes.
Then we created a Block class, in which the contructor takes the coordinates as parameters, and specifies the shape and the shape variation that we want to pick. The shape function returns the shape from the list of blocks based on the values chosen in the constructor above.
Lastly, we created a draw block function that loops in the 3x3 matrix and draws the desired shape on the screen.

### Type 0 rotation 0 (line 34 in the code):
![](images/third_commit_drawing_shape_1.png)

### Type 1 rotation 0 (line 34 in the code):
![](images/third_commit_drawing_shape_2.png)

## Fourth commit - dropping and moving the blocks:

In the fourth step we are moving the blocks on the grid. First we are dropping the block from top to bottom, we do that by changing the y coordinates of the block relative to the screen frame rate in the move_block() function. We also set the block to stop moving when it reaches the bottom of the window. Next, we are moving the block to the left or right depending on the user key input. The block stops moving when reaching either edges.

### Pressing left arrow and reaching left edge:
![](images/fourth_commit_left_edge.png)

### Pressing right arrow and reaching right edge:
![](images/fourth_commit_right_edge.png)

### Shape reaching the end of the screen:
![](images/fourth_commit_bottom.png)

## Fifth commit - creating a game board:

In the fifth step we are creating a board for the game. The board is a list contaning colour values. At first, we initialize it containing all black colours. Then, as an example, when a block reaches the bottom of the screen, we're not going to need it anymore; so we set the block to None, we set its coordinates in the game board to hold the green value, and we draw the game board on the grid as long as the colour is different than black.

### Before hitting the bottom of the screen:
![](images/fifth_commit_game_board_1.png)

### After hitting the bottom of the screen:
![](images/fifth_commit_game_board_2.png)

