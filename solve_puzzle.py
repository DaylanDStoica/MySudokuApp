
# solve_puzzle.py
# given an unsolved sudoku puzzle, output a solved version

# DaylanDStoica


from create_puzzles import is_box_valid, is_col_valid, is_row_valid, is_puzzle_valid
from create_puzzles import EMPTY_CELL
ACCEPTABLE_CELL_VALUES = [1,2,3,4,5,6,7,8,9]

# puzzle format of 2D array, puzzle[9][9]
def findTheNextEmptyCell ( unsolved_puzzle):
    # return the coordinates of the next empty cell within the puzzle, moving left-right top-down
    for x in range(0,9):
        for y in range(0,9):
            if ( unsolved_puzzle[x][y] == EMPTY_CELL):
                return x, y 
    return -1, -1 # no more empty cells

def solvePuzzleV1( unsolved_puzzle):
    puzzle_copy = unsolved_puzzle.copy()
    # first version of the process, will use brute force to solve
    # 1. enter an empty cell, going from left-to-right and top-to-bottom
    # 2. select the first/next value in acceptable values_list for the cell
    # 3. check that the puzzle remains valid
    # 4a. if puzzle is valid after cell input, move to next empty cell
    # 4b. if puzzle is not valid after cell input, try the next value in acceptable values_list
    # 4ba. if no acceptable values exist for the cell, the puzzle as is is unsolvable, and
    # and will need to retrace steps to a prior cell of attempted value, and try the next value in acceptable values list for the older cell
    # this may require mulitple retraces to find a cell with another valid number with change
    # 5. repeat until reach the end of puzzle and puzzle is valid with all cells filled.

    while ( True):
        # Step 1: find the empty cell 
        empty_cell_coords = findTheNextEmptyCell(puzzle_copy)
        # if the empty cell coords put it outside the puzzle, check that the puzzle is valid, 
        # if both are True, exit the loop
        if empty_cell_coords == (-1,-1):
            if is_puzzle_valid(puzzle_copy):
                return True
            else: # reached the end and the puzzle is NOT valid, error
                print("ERROR: reached end of puzzle, puzzle is invalid")

        # Step 2: loop through the list of viable numbers to insert into the empty cell
        temp_puzzle = puzzle_copy.copy() # create a puzzle copy for verifying new values
        for new_num in ACCEPTABLE_CELL_VALUES:
            # check if the puzzle is still valid after new number
            temp_puzzle[empty_cell_coords[0] ] [ empty_cell_coords[1] ] = new_num 
            # if is_puzzle_valid(temp_puzzle):
        
        # if after going through all numbers for the cell, and still no valid numbers
        # the empty cell will remain empty
        # then, retrace to a prior attempted cell, skipping over the cells hard-written upon puzzle reception
        
