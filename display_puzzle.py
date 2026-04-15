
# display_puzzle.py
# DaylanDStoica

# given a sudoku puzzle, assuming 9x9, display in a GUI friendly way 

def display_puzzle(puzzle):
    for row in puzzle: 
        print(row.join)

def read_puzzle_from_file():
    filename = "playable_puzzles.txt"
    f = open( filename, "r")
    # print(f)
    # display_puzzle(f)
    for row in f:
        print(row)
    f.close

read_puzzle_from_file() # currently reads the file contents without separators 

# TODO: build function that output just the puzzle, without extra characters    