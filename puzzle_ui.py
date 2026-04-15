# puzzle_ui.py

# DaylanDStoica
# handle the user interface of puzzle solving
# input and output
# take user input and change cell value within puzzle

from create_puzzles import EMPTY_CELL

from create_puzzles import is_puzzle_valid

def take_input( puzzle, xcoor=0, ycoor=0, new_value=EMPTY_CELL):
    temp_puzzle = puzzle.copy()
    temp_puzzle[xcoor][ycoor] = new_value 
    # add check for after handling input, that if the potential puzzle is valid for now, update the puzzle
    # if the input was invalid, reject input 
    if is_puzzle_valid(temp_puzzle): # if the new temp_puzzle is valid, update the greater puzzle 
        puzzle = temp_puzzle
        return 1
    else:
        # reject input 
        return 0

