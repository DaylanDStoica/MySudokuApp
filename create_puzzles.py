
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

from math import ceil
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


# create a filled puzzle 

# Method 1: random generation, which is very inefficient, as it generates completely random boards that are likely to be invalid, and then checks for validity afterwards, which can take a long time to generate a valid puzzle.
def create_puzzle_random():
    # through row creation, fill up a board
    # then check the board for rule compliance, and if it is not compliant, start over
    # this is a brute-force method, and it may not be the most efficient way to

    board = EMPTY_BOARD.copy()
    for row in range(9):
        board[row] = create_row_random()

    return board


# generated notes:
# this is a brute-force method, and it may take a long time to generate a valid puzzle, especially if the random generation is not efficient.  
# It may be more efficient to use a backtracking algorithm to generate puzzles, which can ensure that the generated puzzle is valid from the start, 
# rather than generating random puzzles and checking for validity afterwards.



def track_time_threading():
    # track the time during puzzle generation, and print it every second, using threading to avoid blocking the main thread during generation, which can take a long time, especially if the random generation is not efficient.
    import time
    # import threading

    start_time = time.time()
    current_time = ceil(time.time() - start_time) # round to the upper second, to avoid printing too many decimals

    while True:
        new_time = ceil(time.time() - start_time)
        if new_time > current_time: # only print the time if it has changed by at least 1 second, to avoid printing too many times
            current_time = new_time
            print("Current time: (seconds)", current_time)
        time.sleep(0.1) # sleep for a short amount of time to avoid busy-waiting

# Method 2: random generation, but with a more efficient method than the previous one, by filling in the board row by row, and checking for validity after each row is filled in, which should be more likely to generate a valid puzzle in a shorter amount of time, but it is still a brute-force method, and it may still take a long time to generate a valid puzzle, especially if the random generation is not efficient.
def create_puzzle_random2():
    # create a random puzzle, but with a more efficient method than the previous one, by filling in the board row by row, and checking for validity after each row is filled in
    # this is still a brute-force method, but it should be more efficient than the previous one, as it will not generate completely random boards that are likely to be invalid, but rather will fill in the board in a way that is more likely to be valid

    board = EMPTY_BOARD.copy()

    row = 0
        # test the time it takes to generate a random puzzle, and check if it is valid
    import time
    start_time = time.time()
    current_time = ceil(time.time() - start_time) # round to the upper second, to avoid printing too many decimals

    # for row in range(0, 9):
    while row < 9:
        # print ("Filling in row ", row)
        row_is_valid = False
        while not row_is_valid:
            board[row] = create_row_random()
            row_is_valid = is_row_valid(board, row)

            new_time = ceil(time.time() - start_time)
            if new_time > current_time: # only print the time if it has changed by at least 1 second, to avoid printing too many times
                current_time = new_time
                print("Current time: (seconds)", current_time)

        # once the row is valid, check if the board is still valid, and if not, start over
        if not is_puzzle_valid(board):
            board = EMPTY_BOARD.copy()
            row = -1 # reset the row index to start over from the first row
        row += 1
    return board

# print(create_puzzle_random())
#print_board(create_puzzle_random())


def is_row_valid (board, row):  
    # check if the given row is valid (no duplicates)
    # print("checking row ", row)
    # print( type(row))
    # print(board[row])
    temp_row = board[row]
    invalid_values = []
    for cell in temp_row:
        if cell in invalid_values: # duplicates
            return False
        elif cell != EMPTY_CELL:
            invalid_values.append(cell)
    return True

def is_col_valid (board, col):
    # check if the given column is valid (no duplicates)
    temp_col = [board[row][col] for row in range(9)]
    invalid_values = []
    for cell in temp_col:
        if cell in invalid_values: # duplicates
            return False
        elif cell != EMPTY_CELL:
            invalid_values.append(cell)
    return True

def is_box_valid (board, box_row, box_col):
    # check if the 3x3 box at the given row and column is valid (no duplicates)
        # box_row and box_col are the indices of the box, not the cell

    # create a temporary array to hold the values of the box, for checking for duplicates
    temp_box = [ [EMPTY_CELL] * 3 for _ in range(3) ] # 3x3 array of empty cells
    # print("printing temp_box:")
    # print_board(temp_box)
    temp_row = 0
    for row in range(box_row * 3, box_row * 3 + 3):
        temp_col = 0
        for col in range(box_col * 3, box_col * 3 + 3):
            # temp_box.append(board[row][col])
            temp_box[temp_row][temp_col] = board[row][col]
            temp_col += 1
        temp_row += 1
    
    invalid_values = []
    for row in temp_box:
        for cell in row:
            if cell in invalid_values: # duplicates
                return False
            elif cell != EMPTY_CELL:
                invalid_values.append(cell)
    return True

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


# testing the validity_checking functions, by getting an outside puzzle for checking
test_puzzle1 = [ list('391286574'),
               list('487359126'),
               list('652714839'),
               list('875431692'),
               list('213967485'),
               list('964528713'),
               list('149673258'),
               list('538142967'),
               list('726895341')]

# test_puzzle = test_puzzle1.copy()
# print_board(test_puzzle)
# print(is_puzzle_valid(test_puzzle)) # should return True, as this is a valid puzzle


def create_puzzle_random3():
    # this is a more efficient random generation method, which fills in the board row by row, and checks for validity after each row is filled in, which should be more likely to generate a valid puzzle in a shorter amount of time, but it is still a brute-force method, and it may still take a long time to generate a valid puzzle, especially if the random generation is not efficient.
    # this method is similar to the previous one, but it also checks for validity after each row is filled in, and if the row is not valid, it will try to fill in the row again, rather than starting over from the first row, which should be more efficient than the previous method, as it will not have to start over from the first row every time a row is not valid.

    board = EMPTY_BOARD.copy()

    # print_board(board)
    import time
    start_time = time.time()

    current_time = start_time
    row = 0
    # for row in range(0, 9):
    while row < 9:
        row_is_valid = False
        while not row_is_valid:
            board[row] = create_row_random()
            row_is_valid = is_row_valid(board, row)

            # print the time change
            new_time = ceil(time.time() - start_time)
            if new_time > current_time: # only print the time if it has changed by at least 1 second, to avoid printing too many times
                current_time = new_time
                print("Current time: (seconds)", current_time)

        # once the row is valid, check if the board is still valid, and if not, start over from the current row, rather than starting over from the first row, 
        # which should be more efficient than the previous method, as it will not have to start over from the first row every time a row is not valid
        if not is_puzzle_valid(board):
            board[row] = EMPTY_ROW.copy() 
            # reset the current row to empty, to start over from the current row, rather than starting over from the first row, 
            # which should be more efficient than the previous method, as it will not have to start over from the first row every time a row is not valid
            row -= 1 # decrement the row index to start over from the current row, rather than starting over from the first row,
        row += 1
    return board

# test the puzzle generation 
def testing_time_of_random_gen_puzzle():
    # test the time it takes to generate a random puzzle, and check if it is valid
    import time
    start_time = time.time()
    current_time = ceil(time.time() - start_time) # round to the upper second, to avoid printing too many decimals

    # TODO: implement threading for printing the time during generation, to avoid printing too many times, and to avoid blocking the main thread during generation, which can take a long time, especially if the random generation is not efficient.
    puzzle_is_valid = False

    # def create_and_test_puzzle():
    #     nonlocal puzzle_is_valid
    #     puzzle = EMPTY_BOARD.copy()
    #     while ( not puzzle_is_valid):
    #         # puzzle = create_puzzle_random() # this is the original random generation method, which is very inefficient, as it generates completely random boards that are likely to be invalid, and then checks for validity afterwards, which can take a long time to generate a valid puzzle.
            
    #         puzzle = create_puzzle_random2() # this is a more efficient random generation method, which fills in the board row by row, and checks for validity after each row is filled in, which should be more likely to generate a valid puzzle in a shorter amount of time, but it is still a brute-force method, and it may still take a long time to generate a valid puzzle, especially if the random generation is not efficient.
    #         puzzle_is_valid = is_puzzle_valid(puzzle)

    #     return puzzle

    # import threading
    
    # time_thread = threading.Thread(target=track_time_threading)
    # time_thread.start()

    # puzzle_thread = threading.Thread(target=create_and_test_puzzle)
    # puzzle_thread.start()
        
    while ( not puzzle_is_valid):
        # print("Current time: ", time.time() - start_time)
        # printing time during generation
        #  
        
        # puzzle = create_puzzle_random() # this is the original random generation method, which is very inefficient, as it generates completely random boards that are likely to be invalid, and then checks for validity afterwards, which can take a long time to generate a valid puzzle.
        
        # puzzle = create_puzzle_random2() # this is a more efficient random generation method, which fills in the board row by row, and checks for validity after each row is filled in, which should be more likely to generate a valid puzzle in a shorter amount of time, but it is still a brute-force method, and it may still take a long time to generate a valid puzzle, especially if the random generation is not efficient.
        puzzle = create_puzzle_random3() # this is a more efficient random generation method, which fills in the board row by row, and checks for validity after each row is filled in, which should be more likely to generate a valid puzzle in a shorter amount of time, but it is still a brute-force method, and it may still take a long time to generate a valid puzzle, especially if the random generation is not efficient.
        new_time = ceil(time.time() - start_time)
        if new_time > current_time: # only print the time if it has changed by at least 1 second, to avoid printing too many times
            current_time = new_time
            print("Current time: (seconds)", current_time)

        puzzle_is_valid = is_puzzle_valid(puzzle)
        
    # time_thread.close() # close the time tracking thread, which should stop it from printing the time during generation, as the puzzle is now generated and is valid
    # time_thread.join() # wait for the time tracking thread to finish, which should happen when the puzzle is generated and is valid
    
    # puzzle_thread.join() # wait for the puzzle generation thread to finish, which should happen when the puzzle is generated and is valid
    end_time = time.time() # get the end time after the puzzle is generated and is valid
    # puzzle = puzzle_thread._target() # get the generated puzzle from the puzzle generation thread, which should be valid
    print_board(puzzle)
    print("Time taken to generate puzzle: ", end_time - start_time)
    print("Is the puzzle valid? ", is_puzzle_valid(puzzle))

    # with open('test_results.txt', 'a') as f:
    #     f.write("Testing time of create_random_puzzle() function, random puzzle generation method 3 (row by row, with validity checking after each row): \n" )
    #     f.write("Time taken to generate valid puzzle (randomly): " + str(end_time - start_time) + "\n")
    #     f.write("\n")
    # f.close()

# testing_time_of_random_gen_puzzle()

# testing_time_of_random_gen_puzzle() # testing stopped after 5 minutes, as it was taking too long to generate a valid puzzle.
# TODO: implement a more efficient puzzle generation method, such as backtracking, to ensure that the generated puzzle is valid from the start, 
# rather than generating random puzzles and checking for validity afterwards.

# generated notes:
# this is a brute-force method, and it may take a long time to generate a valid puzzle, especially if the random generation is not efficient.  
# It may be more efficient to use a backtracking algorithm to generate puzzles, which can ensure that the generated puzzle is valid from the start, 
# rather than generating random puzzles and checking for validity afterwards.

testing_time_of_random_gen_puzzle()

