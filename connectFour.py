# Start createBoard
def createBoard():
    # Creates the initial board which is a matrix of 0's
    board = [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
    return board
# End createBoard

#start billy pygame stuff 1

import pygame
pygame.init()
win = pygame.display.set_mode((4200, 4200))
pygame.display.set_caption("Connect Four")  

#end billy pygame stuff 1

# Start winCheck
def winCheck(myBoard, t, checkWin):
    # Checks for vertical win
    for row in range(3):
        for column in range(7):
            if myBoard[row][column] == t and myBoard[row+1][column] == t:
                if myBoard[row+2][column] == t and myBoard[row+3][column] == t:
                    checkWin = True
                    break
                
    # Check for horizontal win                
    for row in range(6):
        for column in range(4):
            if myBoard[row][column] == t and myBoard[row][column+1] == t:
                if myBoard[row][column+2] == t and myBoard[row][column+3] == t:
                    checkWin = True
                    break
                
    # Check for up-right diagonal win
    for row in range(3, 6):
        for column in range(3):
            if myBoard[row][column] == t and myBoard[row-1][column+1] == t:
                if myBoard[row-2][column+2] == t and myBoard[row-3][column+3] == t:
                    checkWin = True
                    break
                
    # Check fpr down-right diagonal win
    for row in range(3):
        for column in range(4):
            if myBoard[row][column] == t and myBoard[row+1][column+1] == t:
                if myBoard[row+2][column+2] == t and myBoard[row+3][column+3] == t:
                    checkWin = True
                    break
                
    return checkWin
    
# Start updateBoard
def updateBoard(uBoard, column, turn, win):
    # Takes the user's move and updates the board
    saveRow = 0
    for row in range(6):
        if uBoard[row][column] is not 0:
            saveRow = row - 1
            break
        elif row is 5:# If a column is empty, sets saveRow to row 
            saveRow = row
            break
    
    if(turn is 1):
        uBoard[saveRow][column] = turn
    
    if(turn is 2):
        uBoard[saveRow][column] = turn
    
    win = winCheck(uBoard, turn, win)
    
    # Prints the updated board
    print(' 0  1  2  3  4  5  6')
    for row in uBoard:
        print(row)
    
    return win
# End updateBoard
            
# Start playerOne
def playerOne(board, isWin):
    turn = 1 # Needed to tell board it's player one's move
    # Gets user input and converts it to integer
    move = int(input("Player one, please select a column to play in.\n"))
    while move < 0 or move > 6:# Checks that user has selected an existing column
        move = int(input('Column not allowed, please select an appropriate column.\n'))
    while board[0][move] is not 0:# Checks if a column is full 
        move = int(input('That column is full, please select a different column.\n'))
        move = int(move)
    isWin = updateBoard(board, move, turn, isWin)# Sends move to the baord to be updated
    if isWin is True:
        print("Player One wins!")
    return isWin
# End playerOne

# Start playerTwo
def playerTwo(board, isWin):
    turn = 2 # Need to tell server it's player two's turn
    # Gets user input and converts it to integer
    move = int(input("Player two, please select a column to play in.\n"))
    while move < 0 or move > 6: # Checks that user has selected an existing column
        move = int(input('Column not allowed, please select an appropriate column.\n'))
    while board[0][move] is not 0: # Checks if a column is full 
        move = int(input('That column is full, please select a different column.\n'))
    isWin = updateBoard(board, move, turn, isWin)# Sends move to the baord to be updated
    if isWin is True:
        print("Player Two wins!")
    return isWin

# Main
# Function call to get the baord
myBoard = createBoard()

#start billy pygame stuff 2

#values of constants
x = 50
y = 50
radius = 60
vel = 5
locationspace = 1

run = true
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #window should close once user presses red X at top
            run = False
    running = 1
    while running <= 7
        sprinting = 1
        while sprinting <= 6
            pygame.draw.circle(win, (128, 128, 128) (running * x, sprinting  * y, radius) ) #draw a gray circle in the window at 
            sprinting = sprinting + 1
        running = running + 1
    pygame.display.update()
            
pygame.quit


#end billy pygame stuff 2

win = False
# Labels for columns
print(' 0  1  2  3  4  5  6')

# Prints the initial board
for row in myBoard:
    print(row)

# Continues playing the game until a winner is found
while win is False:
    win = playerOne(myBoard, win) # Calls for player one's turn
    if win is False: 
        win = playerTwo(myBoard, win) # Calls for player two's turn

