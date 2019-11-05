"""
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
def updateBoard(board, row, column, turn):
	board[row][column] = turn
# End updateBoard
"""

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

playerNumber = 0

try:
	s = socket.socket()
	port = 61001
	s.connect(('', port))
	playerNumber = 1
except:
	s2 = socket.socket()
	port = 61002
	s2.connect(('',port))
	playerNumber = 2

print('connection established')

#board = createBoard()

win = False
while(not win):
	player = s.recv(1024)
	if(player == 'player 1' and playerNumber == 1):
		playerOne()
	elif(player == 'player 2' and playerNumber == 2):
		playerTwo()
	
	player1Board = s.recv(4096)
	player2Board = s2.recv(4096)
	
	print(' 0  1  2  3  4  5  6')
	for row in player1Board:
		print(row)
	
	print(' 0  1  2  3  4  5  6')
	for row in player2Board:
		print(row)
	


