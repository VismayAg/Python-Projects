# Python-Projects
**SUDOKU SOLVER**

Using the following code, any sudoku puzzle can be solved provided they have a valid solution.
The project is coded in python language and is using recursion as well as backtracking to reach the end result.

To find a solution, I have defined multiple function to perform specific task in order to reach the end goal.

find_next_empty(puzzle) : The work of this function is to iterate over the entire puzzle and find the next empty space which we need to fill. The empty space in the given code being -1.
The function returns the index of row and column if an empty space is found else returns None,None signifying the sudoku puzzle has been solved.

is_valid(puzzle, guess, row, column) : The work of this function is to find what value between 1-9 i.e., the guess value we pass in parameter is the correct value that can be put in the empty space that follows the rules of sudoku.
If the value (guess) is not valid, the function returns False i.e., it is already in either the row or the column of the empty space.
If it is not present in the current row and column, now we check if it is in the current 3x3 square of the sudoku block.
If the guess is not present, the value (guess) is entered in puzzle[r][c].  If it is already in the 3x3 block, it returns False.
If the value is entered in the empty space i.e., puzzle[r][c], the function as a whole returns True.

solve_sudoku(puzzle) : This function is the main function that calls all the above stated functions.
First it calls find_next_empty(puzzle) to get the row and column index of the empty space.
We check that the row is not None, if it is none, the puzzle is solved else,
We call function is_valid by passing all numbers from 1 through 9 to check which number best fits the empty space first.
If the number fits, its entered in puzzle[r][c] else we revert back to the inital value ie., -1 by back tracking.
The function calls itself until solve_sudoku returns True. If it returns False, the puzzle is not solvable as we have iterated over all possible values.

sample input:

        [3, 9, -1,  -1, 5, -1,  -1, -1, -1],
        [-1, -1, -1,  2, -1, -1,  -1, -1, 5],
        [-1, -1, -1,  7, 1, 9,  -1, 8, -1],

        [-1, 5, -1,  -1, 6, 8,  -1, -1, -1],
        [2, -1, 6,  -1, -1, 3, -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, 4],

        [5, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [6, 7, -1,  1, -1, 5,  -1, 4, -1],
        [1, -1, 9,  -1, -1, -1,  2, -1, -1]
        
Output: 

        [3, 9, 1,  8, 5, 6,  4, 2, 7],
        [8, 6, 7,  2, 3, 4,  9, 1, 5],
        [4, 2, 5,  7, 1, 9,  6, 8, 3],

        [7, 5, 4,  9, 6, 8,  1, 3, 2],
        [2, 1, 6,  4, 7, 3,  5, 9, 8],
        [9, 3, 8,  5, 2, 1,  7, 6, 4],

        [5, 4, 3,  6, 9, 2,  8, 7, 1],
        [6, 7, 2,  1, 8, 5,  3, 4, 9],
        [1, 8, 9,  3, 4, 7,  2, 5, 6]
