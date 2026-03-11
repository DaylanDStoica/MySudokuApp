
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

def create_puzzle_random():
    # through row creation, fill up a board
    # then check the board for rule compliance, and if it is not compliant, start over
    # this is a brute-force method, and it may not be the most efficient way to

    board = EMPTY_BOARD