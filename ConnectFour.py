# Start createBoard
def createBoard():
    # Creates th initial board which is a matrix of 0's
    board = [[0,0,2,0,0,0,0],
             [0,0,1,0,0,0,0],
             [0,0,2,0,0,0,0],
             [0,0,1,0,0,0,0],
             [0,0,2,0,0,0,0],
             [0,0,1,1,1,0,0]]
    return board
# End createBoard

# Start updateBoard
def updateBoard(uBoard, column, turn):
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
    
    # Prints the updated board
    print(' 0  1  2  3  4  5  6')
    for row in uBoard:
        print(row)
# End updateBoard
            
# Start playerOne
def playerOne(board):
    turn = 1 # Needed to tell board it's player one's move
    # Gets user input and converts it to integer
    move = int(input("Player one, please select a column to play in.\n"))
    while move < 0 or move > 6:# Checks that user has selected an existing column
        move = int(input('Column not allowed, please select an appropriate column.\n'))
    while board[0][move] is not 0:# Checks if a column is full 
        move = int(input('That column is full, please select a different column.\n'))
        move = int(move)
    updateBoard(board, move, turn)# Sends move to the baord to be updated
# End playerOne

# Start playerTwo
def playerTwo(board):
    turn = 2 # Need to tell server it's player two's turn
    # Gets user input and converts it to integer
    move = int(input("Player two, please select a column to play in.\n"))
    while move < 0 or move > 6: # Checks that user has selected an existing column
        move = int(input('Column not allowed, please select an appropriate column.\n'))
    while board[0][move] is not 0: # Checks if a column is full 
        move = int(input('That column is full, please select a different column.\n'))
    updateBoard(board, move, turn)# Sends move to the baord to be updated

# Main
# Function call to get the baord
myBoard = createBoard()

win = False

# Labels for columns
print(' 0  1  2  3  4  5  6')

# Prints the initial board
for row in myBoard:
    print(row)

# Continues playing the game until a winner is found
#while win is False:
playerOne(myBoard) # Calls for player one's turn
playerTwo(myBoard) # Calls for player two's turn