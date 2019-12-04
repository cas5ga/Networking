# Start playerOne
def playerOne():
	try:
		turn = 1 # Needed to tell board it's player one's move
		#gets user input and converts it to integer
		move = int(input("Player one, please select a column to play in.\n"))
		while move < 0 or move > 6:# Checks that user has selected an existing column
			move = int(input("Column not allowed, please select an appropriate column.\n"))
		move = str(move)
		move = updateMessage(move)
		#sends the new move location to the server
		s.send(move.encode())
		#receives a message of whether or not the location is valid
		message = recvData()
		#loops until new move location is valid
		while message == "error":# Checks if a column is full 
			move = int(input("That column is full, please select a different column.\n"))
			move = str(move)
			move = updateMessage(move)
			#sends the new move location to the server
			s.send(move.encode())
			#receives a message of whether or not the location is valid
			message = recvData()
	#recursively calls this function if the user enters invalid input
	except:
		print("Sorry, but that input is not valid.  Please try again.\n")
		playerOne()
# End playerOne

# Start playerTwo
def playerTwo():
	try:
		turn = 2 # Need to tell server it's player two's turn
		#gets user input and converts it to an integer
		move = int(input("Player two, please select a column to play in.\n"))
		while move < 0 or move > 6:# Checks that user has selected an existing column
			move = int(input("Column not allowed, please select an appropriate column.\n"))
		move = str(move)
		move = updateMessage(move)
		#sends the new move location to the server
		s.send(move.encode())
		#receives a message of whether or not the location is valid
		message = recvData()
		#loops until new move location is valid
		while message == "error":# Checks if a column is full 
			move = int(input("That column is full, please select a different column.\n"))
			move = str(move)
			move = updateMessage(move)
			#sends the new move location to the server
			s.send(move.encode())
			#receives a message of whether or not the location is valid
			message = recvData()
	#recursively calls this function if the user enters invalid input
	except:
		print("Sorry, but that input is not valid.  Please try again.\n")
		playerTwo()
# End playerTwo

#receives data from the server
def recvData():
	#The message contains the length of the message followed by a '#'
	#The actual message follows the '#'
	dataSize = ""
	#loops reading only one byte until the '#' is found
	found = False
	while not found:
		data = s.recv(1).decode()
		#determines the length of the message
		if(data != "#"):
			dataSize = dataSize + data
		else:
			found = True
			
	dataSize = int(dataSize)
	#reads the appropriate number of bytes based on the information gathered above
	message = s.recv(dataSize).decode()
			
	return message

#receives the board from the server
def recvBoard():
	#The message contains the length of the message followed by a '#'
	#The actual message follows the '#'
	dataSize = ""
	#loops reading only one byte until the '#' is found
	found = False
	while not found:
		data = s.recv(1).decode()
		#determines the length of the message
		if(data != "#"):
			dataSize = dataSize + data
		else:
			found = True
			
	dataSize = int(dataSize)
	#reads the appropriate number of bytes based on the information gathered above
	board = s.recv(dataSize)
	board = pickle.loads(board)
	
	return board
	
#updates the outgoing messages to include the message length and a '#'	
def updateMessage(message):
	encodedMsg = message.encode()
	dataSize = len(encodedMsg)
	dataSize = str(dataSize)
	message = dataSize + "#" + message
	return message
	
# Main
import socket
import platform
import pickle

playerNumber = 0

#creates a socket and connects to listed ip address on the listed port
s = socket.socket()
port = 61001
#ip address for the medusa server at The University of Virginia's College at Wise
ip = "143.60.76.32"
s.connect(('', port))

#receives which player this client is
player = recvData()

#prints the appropriate message based on which player this client is
if(player == "player 1"):
	print("You are player 1")
	print("Waiting on player 2 to connect\n")
elif(player == "player 2"):
	print("You are player 2\n")
	
#main loop of the game
win = False
tie = 0
while win is False:
	#receives the baord from the server
	board = recvBoard()

	#prints labels for the columns
	print("\n 0  1  2  3  4  5  6")
	#prints the game board
	for row in board:
		print(row)
	print("")

	turn = recvData()	#receives a message stating which player's turn it is
	#prints the appropriate message based on whose turn it is
	if(player == "player 1" and turn == "player one's turn"):
		playerOne()
	elif(player == "player 2" and turn == "player two's turn"):
		playerTwo()
	elif(player == "player 1"):
		print("Waiting on player 2\n")
	elif(player == "player 2"):
		print("Waiting on player 1\n")
	
	#receives a message stating if there is a winner or not
	winner = recvData()
	#stops the loop if there is a winner
	if(winner == "True"):
		win = True
	
	#increments the tie variable by one each loop to determine if there is a tie
	#once it reaches 42, there are no more moves
	tie += 1
	if(tie == 42):	
		break
		
#receives the game board
board = recvBoard()

#prints the labels for the columns
print("\n 0  1  2  3  4  5  6")
#prints the game board
for row in board:
	print(row)
print("")	

#if the game was not a tie, receive the winner or looser message
if(tie != 42):
	message = recvData()
	print(message)
#message if the game was a tie
else:
	print("Tie")
	
print("Game Over")
