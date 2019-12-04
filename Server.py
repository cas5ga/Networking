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

# Start updateBoard
def updateBoard(uBoard, column, turn, win):
	# Takes the user's move and updates the board with the new move location
	saveRow = 0
	for row in range(6):
		if uBoard[row][column] is not 0:
			saveRow = row - 1
			break
		elif row is 5:# If a column is empty, sets saveRow to row 
			saveRow = row
			break
            
	uBoard[saveRow][column] = turn

	# Prints the updated board and labels
	print(" 0  1  2  3  4  5  6")
	for row in uBoard:
		print(row)
	print("")
	
	#Checks for a win
	win = winCheck(uBoard, turn, win)
	return win
		
# End updateBoard

# Start playerOne
def playerOne(board, isWin):
	turn = 1 # Needed to tell board it's player one's move
	move = player1recv()
	move = int(move)
	while board[0][move] is not 0:# Checks if a column is full 
		#sends error message to the client
		message = "error"
		message = updateMessage(message)
		player1.send(message.encode())
		move = player1recv()
		move = int(move)
	#sends message that there was no error to the client
	message = "no error"
	message = updateMessage(message)
	player1.send(message.encode())
	isWin = updateBoard(board, move, turn, isWin)# Sends move to the baord to be updated
		
	return isWin
# End playerOne

# Start playerTwo
def playerTwo(board, isWin):
	turn = 2 # Need to tell server it's player two's turn
	move = player2recv()
	move = int(move)
	while board[0][move] is not 0:# Checks if a column is full 
		#sends error message to the client
		message = "error"
		message = updateMessage(message)
		player2.send(message.encode())
		move = player2recv()
		move = int(move)
	#sends message that there was no error to the client
	message = "no error"
	message = updateMessage(message)
	player2.send(message.encode())
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
    
#receive data from the player 1 client
def player1recv():
	#The message contains the length of the message followed by a '#'
	#The actual message follows the '#'
	dataSize = ""
	#loops reading only one byte until the '#' is found
	found = False
	while not found:
		data = player1.recv(1).decode()
		#determines the length of the message
		if(data != "#"):
			dataSize = dataSize + data
		else:
			found = True
		
	dataSize = int(dataSize)
	#reads the appropriate number of bytes based on the information gathered above
	message = player1.recv(dataSize)
			
	return message
	
#recerive data from the player 2 client
def player2recv():
	#The message contains the length of the message followed by a '#'
	#The actual message follows the '#'
	dataSize = ""
	#loops reading only one byte until the '#' is found
	found = False
	while not found:
		data = player2.recv(1).decode()
		#determines the length of the message
		if(data != "#"):
			dataSize = dataSize + data
		else:
			found = True
			
	dataSize = int(dataSize)
	#reads the appropriate number of bytes based on the information gathered above
	message = player2.recv(dataSize)
			
	return message
	
#update outgoing messages to include the message length and a "#"
def updateMessage(message):
	encodedMsg = message.encode()
	dataSize = len(encodedMsg)
	dataSize = str(dataSize)
	message = dataSize + "#" + message
	return message

#Main
import socket
import platform
import pickle

#creates a socket and listens on listed port
s = socket.socket()
port = 61001
s.bind(('', port))
s.listen(2)

#create a connection for player 1
player1, addr1 = s.accept()
message = "player 1"
message = updateMessage(message)
player1.send(message.encode())

#create a connection for player 2
player2, addr2 = s.accept()
message = "player 2"
message = updateMessage(message)
player2.send(message.encode())

myBoard = createBoard()

#prints labels for the columns
print(" 0  1  2  3  4  5  6")

#prints the initial board
for row in myBoard:
    print(row)
print('')

#main loop of the game
win = False
count = 0
tie = 0
winner = ''
while win is False:

	#counter to determine if there is a tie
	tie += 1
	
	#pickles the game board to send it to the clients
	gameBoard = pickle.dumps(myBoard)
	#adds the length of the board and a '#' to the message
	dataSize = len(gameBoard)
	dataSize = str(dataSize) + "#"
	
	#sends the baord to player 1 and player 2
	player1.send(dataSize.encode())
	player1.send(gameBoard)
	player2.send(dataSize.encode())
	player2.send(gameBoard)
	
	#determines if it is player 1's turn or player 2's turn
	num = count%2
	#player 1
	if(num == 0):
		message  = "player one's turn"
		message = updateMessage(message)
		player1.send(message.encode())
		player2.send(message.encode())
		win = playerOne(myBoard, win) # Calls for player one's turn
		if win is True:
			winner = "player 1"
	#player 2
	elif(num == 1):
		message = "player two's turn"
		message = updateMessage(message)
		player1.send(message.encode())
		player2.send(message.encode())
		win = playerTwo(myBoard, win) # Calls for player two's turn
		if win is True:
			winner = "player 2"
	#sends a message to the clients informing them if there has been a win	
	if win is True:
		message = "True"
		message = updateMessage(message)
		player1.send(message.encode())
		player2.send(message.encode())
	else:
		message = "False"
		message = updateMessage(message)
		player1.send(message.encode())
		player2.send(message.encode())
	
	#increases the count to determine if it is player 1's turn or player 2's turn
	count += 1
	
	#breaks out of the loop if there is a tie
	if(tie == 42):
		break


#pickles the board and adds the message length and a '#'
gameBoard = pickle.dumps(myBoard)
dataSize = len(gameBoard)
dataSize = str(dataSize) + "#"

#sends the board to player 1 and player 2
player1.send(dataSize.encode())
player1.send(gameBoard)
player2.send(dataSize.encode())
player2.send(gameBoard)

#checks if winner was player 1
#sends the appropriate message to each client
if(winner == "player 1"):
	message = "Congratulations!  You are the winner!"
	message = updateMessage(message)
	player1.send(message.encode())
	message = "Sorry, but player 1 won the game."
	message = updateMessage(message)
	player2.send(message.encode())
#checks if winner was player 2
#sends the appropriate message to each client
elif(winner == "player 2"):
	message = "Sorry, but player 2 won the game."
	message = updateMessage(message)
	player1.send(message.encode())
	message = "Congratulations!  You are the winner!"
	message = updateMessage(message)
	player2.send(message.encode())
