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
            
	uBoard[saveRow][column] = turn

	# Prints the updated board
	print(' 0  1  2  3  4  5  6')
	for row in uBoard:
		print(row)
	print('')
	
	win = winCheck(uBoard, turn, win)
	return win
		
# End updateBoard

# Start playerOne
def playerOne(board, isWin):
	turn = 1 # Needed to tell board it's player one's move
	move = player1.recv(1024)
	move = int(move)
	while board[0][move] is not 0:# Checks if a column is full 
		player1.send('error')
		move = player1.recv(1024)
		move = int(move)
	player1.send('no error')
	isWin = updateBoard(board, move, turn, isWin)# Sends move to the baord to be updated
		
	return isWin
# End playerOne

# Start playerTwo
def playerTwo(board, isWin):
    turn = 2 # Need to tell server it's player two's turn
    move = player2.recv(1024)
    move = int(move)
    while board[0][move] is not 0:# Checks if a column is full 
        player2.send('error')
        move = player2.recv(1024)
        move = int(move)
    player2.send('no error')
    isWin = updateBoard(board, move, turn, isWin)# Sends move to the baord to be updated
		
    return isWin
    
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
player1.send('player 1'.encode())

player2, addr2 = s.accept()
player2.send('player 2')

myBoard = createBoard()

# Labels for columns
print(' 0  1  2  3  4  5  6')

# Prints the initial board
for row in myBoard:
    print(row)
print('')

win = False
count = 0
winner = ''
while win is False:
	
	gameBoard = pickle.dumps(myBoard)
	player1.send(gameBoard)
	time.sleep(.1)
	player2.send(gameBoard)
	time.sleep(.1)
	
	num = count%2
	if(num == 0):
		player1.send("player one's turn")
		player2.send("player one's turn")
		win = playerOne(myBoard, win) # Calls for player one's turn
		if win is True:
			winner = 'player 1'
		
	elif(num == 1):
		player1.send("player two's turn")
		player2.send("player two's turn")
		win = playerTwo(myBoard, win) # Calls for player two's turn
		if win is True:
			winner = 'player 2'
			
	if win is True:
		player1.send('True')
		player2.send('True')
	else:
		player1.send('False')
		player2.send('False')
	
	count += 1


gameBoard = pickle.dumps(myBoard)
player1.send(gameBoard)
time.sleep(.1)
player2.send(gameBoard)
time.sleep(.1)

if(winner == 'player 1'):
	player1.send('Congratulations!  You are the winner!')
	player2.send('Sorry, but player 1 won the game.')
elif(winner == 'player 2'):
	player1.send('Sorry, but player 2 won the game.')
	player2.send('Congratulations!  You are the winner!')
