# Start playerOne
def playerOne():
	turn = 1 # Needed to tell board it's player one's move
	# Gets user input and converts it to integer
	move = int(input("Player one, please select a column to play in.\n"))
	while move < 0 or move > 6:# Checks that user has selected an existing column
		move = int(input('Column not allowed, please select an appropriate column.\n'))
	s.send(str(move))
	message = s.recv(1024)
	while message == 'error':# Checks if a column is full 
		move = int(input('That column is full, please select a different column.\n'))
		s.send(str(move))
		message = s.recv(1024)
# End playerOne

# Start playerTwo
def playerTwo():
	turn = 2 # Need to tell server it's player two's turn
	move = int(input("Player two, please select a column to play in.\n"))
	while move < 0 or move > 6:# Checks that user has selected an existing column
		move = int(input('Column not allowed, please select an appropriate column.\n'))
	s.send(str(move))
	message = s.recv(1024)
	while message == 'error':# Checks if a column is full 
		move = int(input('That column is full, please select a different column.\n'))
		s.send(str(move))
		message = s.recv(1024)
		
# End playerTwo

# Main
# Function call to get the baord
import socket
import time
import platform
import pickle

playerNumber = 0

s = socket.socket()
port = 61001
s.connect(('143.60.76.32', port))

player = s.recv(1024).decode()

if(player == 'player 1'):
	print('You are player 1')
	print('Waiting on player 2 to connect\n')
elif(player == 'player 2'):
	print('You are player 2\n')

win = False
while win is False:
		board = s.recv(4096)
		board = pickle.loads(board)
	
		print(' 0  1  2  3  4  5  6')
		for row in board:
			print(row)
		print('')
	
		turn = s.recv(1024)
	
		if(player == 'player 1' and turn == "player one's turn"):
			playerOne()
		elif(player == 'player 2' and turn == "player two's turn"):
			playerTwo()
		elif(player == 'player 1'):
			print("Waiting on player 2\n")
		elif(player == 'player 2'):
			print("Waiting on player 1\n")
			
		winner = s.recv(1024)
		
		if(winner == 'True'):
			win = True
			
board = s.recv(4096)
board = pickle.loads(board)	

print(' 0  1  2  3  4  5  6')
for row in board:
	print(row)
print('')	

message = s.recv(1024)
print(message)

print('Game Over')
