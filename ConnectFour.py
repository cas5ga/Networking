def createBoard():
    # Creates th initial board which is a matrix of 0's
    board = [[0,0,1,0,2,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
    return board

def updateBoard(uBoard, column):
    # Takes the user's move and updates the board
    for row in range(1):
        rowCheck = row - 1
        while uBoard[rowCheck+1][column] is 0 and rowCheck+1 is not 6:
            rowCheck += 1
    
    # Prints the updated board
    for row in uBoard:
        print(row)
                
# Player one's turn
def playerOne(board):
    # Gets user input and converts it to integer
    move = int(input("Player one, please select a column to play in.\n"))
    while move < 0 or move > 6:# Checks that user has selected an existing column
        move = int(input('Column not allowed, please select an appropriate column.\n'))
    while board[0][move] is not 0:# Checks if a column is full 
        move = int(input('That column is full, please select a different column.\n'))
        move = int(move)
    updateBoard(board, move)# Sends move to the baord to be updated

# Player tow's turn
def playerTwo(board):
    # Gets user input and converts it to integer
    move = int(input("Player two, please select a column to play in.\n"))
    while move < 0 or move > 6: # Checks that user has selected an existing column
        move = int(input('Column not allowed, please select an appropriate column.\n'))
    while board[0][move] is not 0: # Checks if a column is full 
        move = int(input('That column is full, please select a different column.\n'))
    updateBoard(board, move)# Sends move to the baord to be updated

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