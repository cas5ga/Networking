# Start createBoard
def createBoard():
    # Creates th initial board which is a matrix of 0's
    board = [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
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
            
    uBoard[saveRow][column] = turn
    
    # Prints the updated board
    print(' 0  1  2  3  4  5  6')
    for row in uBoard:
        print(row)
# End updateBoard

# Start playerOne
def playerOne(board):
    turn = 1 # Needed to tell board it's player one's move
    move = c.recv(1024)
    move = int(move)
    while board[0][move] is not 0:# Checks if a column is full 
        c.send('error')
        c.recv(1024)
    c.send('no error')
    updateBoard(board, move, turn)# Sends move to the baord to be updated
# End playerOne

# Start playerTwo
def playerTwo(board):
    turn = 2 # Need to tell server it's player two's turn
    move = c.recv(1024)
    move = int(move)
    while board[0][move] is not 0:# Checks if a column is full 
        c.send('error')
        c.recv(1024)
    c.send('no error')
    updateBoard(board, move, turn)# Sends move to the baord to be updated

#Main
import socket
import platform
import time

#establish a connection on port 61001
s = socket.socket()
port = 61001
s.bind(('', port))
s.listen(5)
c, addr = s.accept()

print('connection established')

myBoard = createBoard()

# Labels for columns
print(' 0  1  2  3  4  5  6')

# Prints the initial board
for row in myBoard:
    print(row)

win = False
count = 0
while(not win):
	num = count%2
	if(num == 0):
		c.send('player 1')
		playerOne(myBoard) # Calls for player one's turn
	elif(num == 1):
		c.send('player 2')
		playerTwo(myBoard) # Calls for player two's turn
		
	count += 1
