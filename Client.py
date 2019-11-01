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
        s.send(move)
        s.recv(1024)
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
        s.send(move)
        s.recv(1024)
# End playerTwo

# Main
# Function call to get the baord
import socket
import time
import platform

s = socket.socket()
port = 61001
s.connect(('', port))

print('connection established')

win = False
while(not win):
	player = s.recv(1024)
	if(player == 'player 1'):
		playerOne()
	elif(player == 'player 2'):
		playerTwo()


