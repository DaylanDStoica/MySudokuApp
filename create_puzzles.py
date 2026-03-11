
# DaylanDStoica
# create_puzzles.py

# handle the creation of puzzles, including generating new puzzles and loading puzzles into files
EMPTY_CELL = '_'
EMPTY_ROW = [EMPTY_CELL] * 9
EMPTY_BOARD = [EMPTY_ROW] * 9 # array of arrarys

VALID_CELL_VALUES = [ '1', '2', '3', '4', '5', '6', '7', '8', '9']
def print_board(board): # prints the board in a readable format, with spaces between the cells and without the list brackets and commas
    for row in board:
        print(' '.join(row))

# print_board(EMPTY_BOARD)

import random
def create_row_random():
    # create a row with random values from the valid cell values, ensuring that there are no duplicates
    # for use in random puzzle generation
    row = EMPTY_ROW.copy()
    remaining_values = VALID_CELL_VALUES.copy()
    for i in range(9):
        cell_value = random.choice(remaining_values)
        row[i] = cell_value
        remaining_values.remove(cell_value)


    return row
def create_puzzle_random():
    # through row creation, fill up a board
    # then check the board for rule compliance, and if it is not compliant, start over
    # this is a brute-force method, and it may not be the most efficient way to

    board = EMPTY_BOARD.copy()
    for row in range(9):
        board[row] = create_row_random()

    return board


# print(create_puzzle_random())
print_board(create_puzzle_random())

def is_box_valid (board, box_row, box_col):
    # check if the 3x3 box at the given row and column is valid (no duplicates)
    pass

def is_row_valid (board, row):  

    # check if the given row is valid (no duplicates)
    pass

def is_col_valid (board, col):
    # check if the given column is valid (no duplicates)
    pass    

def is_puzzle_valid (board):
    # run through the rules of the game and check if the board is valid
    # check for duplicates in rows, columns, and 3x3 boxes

    # check rows
    for row in range(9):
        if not is_row_valid(board, row):
            return False
    # check columns
    for col in range(9):
        if not is_col_valid(board, col):
            return False
    # check boxes
    for box_row in range(3):
        for box_col in range(3):
            if not is_box_valid(board, box_row, box_col):
                return False
    return True
