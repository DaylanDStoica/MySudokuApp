
# DaylanDStoica
# create_puzzles.py

# handle the creation of puzzles, including generating new puzzles and loading puzzles into files
EMPTY_CELL = '_'
EMPTY_ROW = [EMPTY_CELL] * 9
EMPTY_BOARD = [EMPTY_ROW] * 9 # array of arrarys

def print_board(board): # prints the board in a readable format, with spaces between the cells and without the list brackets and commas
    for row in board:
        print(' '.join(row))

# print_board(EMPTY_BOARD)

