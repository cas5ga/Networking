board = [['a1','a2','a3','a4','a5','a6','a7',],
         ['b1','b2','b3','b4','b5','b6','b7',],
         ['c1','c2','c3','c4','c5','c6','c7',],
         ['d1','d2','d3','d4','d5','d6','d7',],
         ['e1','e2','e3','e4','e5','e6','e7',],
         ['f1','f2','f3','f4','f5','f6','f7',]]

count = 0
win = False
pos = 'position'

while win is False:
    
    for row in board:
        print('\n')
        for i in range(7):
            print('   ',row[i], end = ' ')
    
    turn = 1
    if turn is 1:
        pos = input('\nPlayer 1, select a position play\n')
        for i in range(6):
            for j in range(7):
                if(board[i][j] == pos):
                    board[i][j] = 'R'
                    break
        count += 1
    print('\n\n')
    for row in board:
        print('\n')
        for i in range(7):
            print('   ',row[i], end = ' ')
    
    turn = 2
    if turn is 2:
        pos = input('\nPlayer 2, select a position play\n')
        for i in range(6):
            for j in range(7):
                if(board[i][j] == pos):
                    board[i][j] = 'B'
                    break
                if(board[i][j] == 'B' or board[i][j] == 'R'):
                    pos = input('Please select an appropriate position\n')
        count += 1
        
    print('\n\n')
    
    if count is 6:
        win = True
                