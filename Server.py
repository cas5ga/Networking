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
    
	"""
	c.send(saveRow)
	time.sleep(.25)
	c.send(column)
    
	c2.send(saveRow)
	time.sleep(.25)
	c2.send(column)
	"""
    
	# Prints the updated board
	print(' 0  1  2  3  4  5  6')
	for row in uBoard:
		print(row)
	print('')
		
# End updateBoard

# Start playerOne
def playerOne(board):
    turn = 1 # Needed to tell board it's player one's move
    move = player1.recv(1024)
    move = int(move)
    while board[0][move] is not 0:# Checks if a column is full 
        player1.send('error')
        player1.recv(1024)
    player1.send('no error')
    updateBoard(board, move, turn)# Sends move to the baord to be updated
# End playerOne

# Start playerTwo
def playerTwo(board):
    turn = 2 # Need to tell server it's player two's turn
    move = player2.recv(1024)
    print("move for player 2")
    move = int(move)
    while board[0][move] is not 0:# Checks if a column is full 
        player2.send('error')
        player2.recv(1024)
    player2.send('no error')
    updateBoard(board, move, turn)# Sends move to the baord to be updated

#Main
import socket
import platform
import time
import pickle

#establish a connection on port 61001

s = socket.socket()
port = 61001
s.bind(('', port))
s.listen(2)
player1, addr1 = s.accept()
player1.send('player 1')

player2, addr2 = s.accept()
player2.send('player 2')

print('connection established')

myBoard = createBoard()

# Labels for columns
print(' 0  1  2  3  4  5  6')

# Prints the initial board
for row in myBoard:
    print(row)
print('')

win = False
count = 0
while(not win):
	
	gameBoard = pickle.dumps(myBoard)
	player1.send(gameBoard)
	time.sleep(.1)
	player2.send(gameBoard)
	time.sleep(.1)
	
	num = count%2
	if(num == 0):
		player1.send("player one's turn")
		player2.send("player one's turn")
		playerOne(myBoard) # Calls for player one's turn
		
	elif(num == 1):
		player1.send("player two's turn")
		player2.send("player two's turn")
		playerTwo(myBoard) # Calls for player two's turn
	
	count += 1
