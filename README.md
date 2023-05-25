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
[0 1 0  
 0 1 0
 0 1 0]
where the 1's are the valid blocks, which can be represented as the list [1, 4, 7]. The same logic follows for the shape's rotation, and for all other shapes.
Then we created a Block class, in which the contructor takes the coordinates as parameters, and specifies the shape and the shape variation that we want to pick. The shape function returns the shape from the list of blocks based on the values chosen in the constructor above.
Lastly, we created a draw block function that loops in the 3x3 matrix and draws the desired shape on the screen.

![](images/third_commit_drawing_shape_1.png)

![](images/third_commit_drawing_shape_2.png)






