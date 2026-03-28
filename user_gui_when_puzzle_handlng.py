
# created by DaylanDStoica on 28/03/2026

def read_puzzle_from_file(file_path = "./playable_puzzles.txt"):
    # read a puzzle from a file, and return it as a 2D list, to be used in the GUI for displaying the puzzle to the user, and allowing them to interact with it.
    with open(file_path, 'r') as file:
        lines = file.readlines()
        puzzle = []
        for line in lines:
            if line.startswith("Difficulty:") or line.startswith("Playable Puzzle:"):
                continue  # skip the difficulty line and the "Playable Puzzle:" line
            # if line.strip() == "":
            #     continue  # skip empty lines
            row = [int(num) for num in line.strip().split(',')]
            puzzle.append(row)
        file.close()
    return puzzle

from create_puzzles import VALID_CELL_VALUES
print("Testing the read_puzzle_from_file function:")
test_puzzle = read_puzzle_from_file()
print(test_puzzle)