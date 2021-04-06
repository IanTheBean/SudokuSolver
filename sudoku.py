import time
start_time = time.time()
 
template_puzzle_9x9 = [
    [6, 0, 0,   0, 0, 5,   0, 3, 0], 
    [0, 1, 0,   4, 2, 0,   0, 0, 6], 
    [0, 0, 4,   0, 0, 0,   0, 0, 0], 
 
    [0, 0, 5,   0, 7, 0,   0, 9, 0], 
    [0, 2, 0,   0, 0, 9,   0, 8, 0], 
    [0, 0, 1,   0, 0, 6,   0, 0, 0], 
 
    [4, 7, 0,   0, 0, 0,   0, 0, 0], 
    [0, 3, 0,   0, 0, 0,   9, 0, 1], 
    [0, 0, 0,   0, 0, 8,   0, 0, 3]
]
 
 
 
template_puzzle_25x25 = [
    [0, 13, 22, 0, 0,   0, 0, 0, 0, 25,  0, 24, 0, 0, 0,  11, 0, 0, 0, 18,  0, 0, 20, 0, 1], 
    [0, 21, 0, 0, 0,    0, 13, 0, 16, 8,    0, 12, 0, 2, 25,    0, 0, 0, 3, 0,  11, 0, 0, 0, 0], 
    [18, 11, 0, 0, 0,   0, 0, 7, 0, 15,  4, 13, 0, 0, 0,  9, 12, 14, 0, 25,   0, 0, 23, 0, 0], 
    [0, 0, 24, 23, 0,   16, 11, 6, 17, 0,   0, 0, 7, 0, 15,  0, 13, 0, 0, 8,  0, 0, 14, 2, 25],
    [25, 9, 0, 0, 0,    0, 5, 0, 23, 3,  18, 11, 6, 17, 10,  0, 0, 7, 20, 15,   0, 13, 22, 16, 8], 
 
    [8, 0, 13, 0, 0,    25, 9, 0, 0, 2,  0, 5, 0, 0, 3, 18, 11, 6, 17, 10,  0, 0, 7, 20, 15], 
    [15, 1, 0, 7, 0,    8, 0, 0, 22, 0,  25, 0, 0, 0, 2,  19, 5, 0, 0, 3,  0, 0, 0, 17, 10], 
    [10, 18, 0, 6, 17,  0, 0, 21, 0, 20,    0, 4, 13, 0, 0,  25, 9, 0, 0, 0,  0, 5, 24, 0, 3], 
    [3, 19, 5, 24, 0,   0, 18, 0, 6, 17,    15, 0, 0, 0, 20,    8, 4, 13, 22, 16,   0, 9, 0, 0, 0],
    [2, 0, 9, 0, 0,  3, 0, 5, 0, 0, 0, 18, 11, 6, 17,   15, 0, 0, 7, 20, 0, 0, 0, 22, 0], 
 
    [16, 8, 0, 0, 22,   0, 25, 9, 0, 14,    0, 19, 5, 0, 23,    10, 18, 11, 0, 0,   0, 0, 21, 7, 20], 
    [0, 0, 0, 21, 0,    0, 8, 0, 13, 22,    0, 0, 9, 12, 14,    3, 0, 0, 0, 23,  10, 18, 11, 6, 0], 
    [0, 0, 18, 11, 0,   0, 15, 0, 21, 0,    0, 8, 0, 0, 0,  2, 25, 9, 12, 14,   3, 19, 0, 0, 0], 
    [23, 3, 19, 0, 24,  0, 0, 0, 11, 6,  0, 15, 1, 0, 7,  0, 8, 0, 0, 0,    0, 25, 9, 12, 14],
    [14, 2, 25, 0, 0,   0, 3, 0, 0, 0,  17, 10, 18, 0, 0,   0, 15, 1, 21, 0,  16, 0, 4, 0, 0], 
 
    [0, 16, 8, 4, 13,   0, 2, 25, 0, 12,    0, 0, 19, 0, 0,  0, 10, 0, 0, 6,  0, 0, 0, 0, 7], 
    [7, 20, 0, 0, 0,    0, 16, 8, 4, 13,    0, 0, 0, 0, 12,  23, 0, 0, 0, 24,   0, 0, 18, 11, 0], 
    [6, 17, 0, 0, 0,    0, 20, 15, 0, 21,   0, 0, 0, 4, 13,  0, 0, 0, 9, 0, 0, 3, 19, 5, 0], 
    [24, 0, 3, 0, 0,    0, 17, 0, 0, 11,    0, 20, 15, 0, 21,   22, 16, 0, 4, 0,    14, 0, 0, 0, 0],
    [12, 0, 2, 0, 9,    24, 23, 3, 0, 5,    6, 17, 0, 0, 0,  7, 0, 0, 0, 21,  22, 0, 0, 4, 0], 
 
    [0, 0, 16, 8, 4,    12, 0, 0, 25, 9,    0, 23, 3, 0, 5,  6, 0, 10, 0, 0,  0, 20, 0, 0, 21], 
    [0, 0, 0, 15, 1,    0, 0, 16, 0, 4,  12, 0, 2, 0, 9,  0, 0, 3, 19, 0,  0, 0, 10, 18, 11], 
    [0, 0, 17, 10, 0,   0, 7, 20, 0, 1,  0, 22, 0, 8, 0,  0, 0, 0, 25, 9,  0, 23, 0, 19, 0], 
    [5, 0, 23, 3, 19,   0, 0, 17, 10, 0,    21, 0, 20, 15, 0,   13, 22, 16, 0, 4,   12, 14, 2, 0, 9],
    [9, 0, 0, 0, 0,  0, 0, 23, 0, 0,  0, 6, 17, 0, 0,  21, 7, 0, 15, 1, 0, 22, 16, 0, 4], 
]
 
template_puzzle_3x3 = [
    [1, 0, 0], 
    [0, 0, 0], 
    [2, 0, 3]
]
template_3x3_answer = [
    [1, 3, 2], 
    [3, 2, 3], 
    [2, 1, 3]
]
 
#debug_puzzle_2 = [
#   [0, 0, 3, 0, 1, 0],
#   [5, 6, 0, 3, 2, 0],
#   [0, 5, 4, 2, 0, 3],
#   [2, 0, 6, 4, 5, 0],
#   [0, 1, 2, 0, 4, 5],
#   [0, 4, 0, 1, 0, 0]
#]
 
PUZZLE_SIZE = 9
BOX_SIZE = 3

puzzle_to_solve = template_puzzle_9x9
template_puzzle = [
    [5, 0, 2,   0, 0, 0,   4, 0, 0], 
    [0, 8, 0,   0, 7, 5,   0, 1, 0], 
    [1, 6, 0,   9, 4, 0,   7, 0, 8], 
 
    [2, 0, 8,   7, 6, 0,   3, 0, 9], 
    [0, 3, 7,   0, 0, 0,   8, 0, 1], 
    [6, 0, 9,   0, 0, 0,   5, 2, 7], 
 
    [7, 0, 5,   0, 9, 8,   1, 0, 2], 
    [0, 2, 0,   0, 1, 7,   0, 0, 0], 
    [8, 9, 0,   0, 5, 0,   0, 0, 4]
]

 
def iteration_search(puzzle):
    last_filled_in = 0
    filled_in = 0
    while filled_in < pow(PUZZLE_SIZE, 2):
        rowNumber = 0
        filled_in = 0
        for row in puzzle:
            cellNumber = 0
            for cell in row:
                if cell == 0:
                    possibleNumbers = []
                    for number in range(1, PUZZLE_SIZE + 1):
                        if checkForAllowed(puzzle, rowNumber, cellNumber, number) == True:
                            possibleNumbers.append(number)     
                    if len(possibleNumbers) == 0:
                        print ("The puzzle is not solvable.")
                        quit()
                    elif len(possibleNumbers) == 1:
                        puzzle[rowNumber][cellNumber] = possibleNumbers[0]
                    else:
                        pass
                else:
                    filled_in += 1
                cellNumber += 1
            rowNumber += 1
        print("There are", filled_in, "filled-in cells")

    print_puzzle(puzzle)
    print("puzzle completed in", time.time() - start_time, " seconds")
    quit()

def brute_force():
    TEMP_PUZZLE = [
    [5, 0, 2,   0, 0, 0,   4, 0, 0], 
    [0, 8, 0,   0, 7, 5,   0, 1, 0], 
    [1, 6, 0,   9, 4, 0,   7, 0, 8], 
 
    [2, 0, 8,   7, 6, 0,   3, 0, 9], 
    [0, 3, 7,   0, 0, 0,   8, 0, 1], 
    [6, 0, 9,   0, 0, 0,   5, 2, 7], 
 
    [7, 0, 5,   0, 9, 8,   1, 0, 2], 
    [0, 2, 0,   0, 1, 7,   0, 0, 0], 
    [8, 9, 0,   0, 5, 0,   0, 0, 4]
]
    ROW_NUMBER = 0
    CELL_NUMBER = 0
    shouldMoveForward = True
    fillInSquare(puzzle_to_solve, 0, 0)
    while True:
        if shouldMoveForward == True:
            TEMP_PUZZLE, ROW_NUMBER, CELL_NUMBER, shouldMoveForward = fillInSquare(TEMP_PUZZLE, ROW_NUMBER, CELL_NUMBER)
        else:
            TEMP_PUZZLE, ROW_NUMBER, CELL_NUMBER, shouldMoveForward = fillInSquareBack(TEMP_PUZZLE, ROW_NUMBER, CELL_NUMBER)
 
##forward track
def fillInSquare(puzzle, rowNumber, cellNumber):
    
    if cellNumber == -1:
        if rowNumber == 0:
            print("The puzzle is not possible")
            quit()
        cellNumber = PUZZLE_SIZE - 1
        rowNumber = rowNumber - 1
    elif cellNumber == PUZZLE_SIZE:
        if(rowNumber == PUZZLE_SIZE - 1):
            print_puzzle(puzzle) 
            print("puzzle completed in", time.time() - start_time, "seconds")
            quit()
        rowNumber += 1
        cellNumber = 0
    print("filling in the cell (", cellNumber, ", ", rowNumber, ")")
 
 
    if template_puzzle[rowNumber][cellNumber] == 0:
        i = puzzle[rowNumber][cellNumber]
        while i <= PUZZLE_SIZE + 1:
            if i >= PUZZLE_SIZE + 1:
                puzzle[rowNumber][cellNumber] = 0
                print("there is no viable option, backtracking")
                return puzzle, rowNumber, cellNumber - 1, False
            elif checkForAllowed(puzzle, rowNumber, cellNumber, i) == True:
                puzzle[rowNumber][cellNumber] = i
                print("cell filled in with a ",i,", moving on to the next cell")
                return puzzle, rowNumber, cellNumber + 1, True
                
                return
            elif checkForAllowed(puzzle, rowNumber, cellNumber, i) == False:
                pass
            else: 
                print("overflow error: i is greater than we can handle")
                quit()
            i = i + 1
    else:
        print("cell is pre-filled with a ", template_puzzle[rowNumber][cellNumber], ", moving on to the next")
        return puzzle, rowNumber, cellNumber + 1, True
        return
 
##backtrack
def fillInSquareBack(puzzle, rowNumber, cellNumber):
    if cellNumber == -1:
        if rowNumber == 0:
            print("The puzzle is not possible")
            quit()
        cellNumber = PUZZLE_SIZE - 1
        rowNumber = rowNumber - 1
    elif cellNumber == PUZZLE_SIZE:
        if(rowNumber == PUZZLE_SIZE - 1):
            print_puzzle(puzzle) 
            print("puzzle completed")
            print("puzzle completed in", time.time() - start_time, "seconds")
            quit()
        rowNumber += 1
        cellNumber = 0
    print("backtracked to the square (", cellNumber, ", ", rowNumber, ")")
        
 
    if template_puzzle[rowNumber][cellNumber] == 0:
        i = puzzle[rowNumber][cellNumber]
        while i <= PUZZLE_SIZE + 1:
            if i >= PUZZLE_SIZE + 1:
                puzzle[rowNumber][cellNumber] = 0
                print("there is no viable option, backtracking")
                return puzzle, rowNumber, cellNumber - 1, False
            elif checkForAllowed(puzzle, rowNumber, cellNumber, i) == True:
                puzzle[rowNumber][cellNumber] = i
                print("cell filled in with a ", i, ", moving on to the next cell")
                return puzzle, rowNumber, cellNumber + 1, True
            elif checkForAllowed(puzzle, rowNumber, cellNumber, i) == False:
                pass
            else: 
                print("overflow error: i is greater than we can handle")
                quit()
            i = i + 1   
    else:
        print("cell is pre-filled with a ", template_puzzle[rowNumber][cellNumber], ", moving backwards")
        return puzzle, rowNumber, cellNumber - 1, False
 
##check for allowerd option
def checkForAllowed(puzzle, rowNumber, cellNumber, number):
    for cell in puzzle[rowNumber]:
        if cell == number:
            return False
 
    for row in puzzle:
        if row[cellNumber] == number:
            return False
 
    xBoxNum = 0
    yBoxNum = 0
 
    while rowNumber >= BOX_SIZE:
        rowNumber -= BOX_SIZE
        yBoxNum += 1
 
    while cellNumber >= BOX_SIZE:
        cellNumber -= BOX_SIZE
        xBoxNum += 1
 
    for y in range(yBoxNum * BOX_SIZE, yBoxNum * BOX_SIZE + BOX_SIZE):
        for x in range(xBoxNum * BOX_SIZE, xBoxNum * BOX_SIZE + BOX_SIZE):
            if(puzzle[y][x] == number):
                return False
 
    return True
    
def print_puzzle(puzzle):
    for row in puzzle:
        print(row)
      
## in order to run the iteration search algorithm, make sure that the puzzle size and box size(71&72) variables are set to the correct value and pass through the puzzle
iteration_search(puzzle_to_solve)

## to tun the brute force, make sure that the puzzle and box size are correct, and set the puzzle inside the brute force function, puzzle to solve and template puzzle(~75).
#brute_force()
