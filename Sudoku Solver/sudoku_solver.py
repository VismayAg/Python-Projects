def find_next_empty(puzzle):
    #finds the next empty row & column i.e., -1
    #returns row, column tuple or (None,None) if there's no empty spaces left
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c

    return None,None #if no spaces left

def is_valid(puzzle, guess, row, col):
    #finds if the guess is valid, returns True else returns false
    #for row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    #for column:
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
        #col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    #Now we need to find starting index of 3x3 matrix of the puzzle
    row_start = (row//3) * 3  #1//3 = 0 or 5//3 = 1
    col_start = (col//3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    #if our guess is coreect, we pass True
    return True


def solve_sudoku(puzzle):
    #solve sudoku using backtracking
    #returns whether a solution for the combination exists
    #mutates puzzle to be the solution if it exists

    # Step 1:
    row, col = find_next_empty(puzzle)

    if row is None:
        return True #If Solved
    
    # Step 2:
    for guess in range(1,10):  #values to enter in puzzle
        # Step 3:
        if is_valid(puzzle, guess, row, col):
            # Step 3.1: if the guess is valid, place in the puzzle
            puzzle[row][col] = guess
            #Now repeat using recursion until we reach the last empty space
            # Step 4: recursively call the function
            if solve_sudoku(puzzle):
                return True
            
        # Step 5: If not valid or if the guess didn't solve the puzzle:
        # We need to backtrack to try a new number:
        puzzle[row][col] = -1 #reset the value of the empty space

    # Step 6: If no number works, then the puzzle is unsolvable, return False:
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,  -1, 5, -1,  -1, -1, -1],
        [-1, -1, -1,  2, -1, -1,  -1, -1, 5],
        [-1, -1, -1,  7, 1, 9,  -1, 8, -1],

        [-1, 5, -1,  -1, 6, 8,  -1, -1, -1],
        [2, -1, 6,  -1, -1, 3, -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, 4],

        [5, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [6, 7, -1,  1, -1, 5,  -1, 4, -1],
        [1, -1, 9,  -1, -1, -1,  2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)