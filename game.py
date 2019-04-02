from tkinter import messagebox

#Function a boolean that's True if a game is finished.
def finished(a):
    done = True
    for x in a:
        if x == ' ':
            done = False
    if ((a[0] == 'X' and a[1] == 'X' and a[2] =='X') or
    (a[3] == 'X' and a[4] == 'X' and a[5] =='X') or
    (a[6] == 'X' and a[7] == 'X' and a[8] =='X') or
    (a[0] == 'X' and a[3] == 'X' and a[6] =='X') or
    (a[1] == 'X' and a[4] == 'X' and a[7] =='X') or
    (a[2] == 'X' and a[5] == 'X' and a[8] =='X') or
    (a[0] == 'X' and a[4] == 'X' and a[8] =='X') or
    (a[2] == 'X' and a[4] == 'X' and a[6] =='X')):
        done = True
    if ((a[0] == 'O' and a[1] == 'O' and a[2] =='O') or
    (a[3] == 'O' and a[4] == 'O' and a[5] =='O') or
    (a[6] == 'O' and a[7] == 'O' and a[8] =='O') or
    (a[0] == 'O' and a[3] == 'O' and a[6] =='O') or
    (a[1] == 'O' and a[4] == 'O' and a[7] =='O') or
    (a[2] == 'O' and a[5] == 'O' and a[8] =='O') or
    (a[0] == 'O' and a[4] == 'O' and a[8] =='O') or
    (a[2] == 'O' and a[4] == 'O' and a[6] =='O')):
        done = True
    return done

#Function that returns the value of a finished game.
def win(a):
    if ((a[0] == 'X' and a[1] == 'X' and a[2] =='X') or
    (a[3] == 'X' and a[4] == 'X' and a[5] =='X') or
    (a[6] == 'X' and a[7] == 'X' and a[8] =='X') or
    (a[0] == 'X' and a[3] == 'X' and a[6] =='X') or
    (a[1] == 'X' and a[4] == 'X' and a[7] =='X') or
    (a[2] == 'X' and a[5] == 'X' and a[8] =='X') or
    (a[0] == 'X' and a[4] == 'X' and a[8] =='X') or
    (a[2] == 'X' and a[4] == 'X' and a[6] =='X')):
        return 1
    elif ((a[0] == 'O' and a[1] == 'O' and a[2] =='O') or
    (a[3] == 'O' and a[4] == 'O' and a[5] =='O') or
    (a[6] == 'O' and a[7] == 'O' and a[8] =='O') or
    (a[0] == 'O' and a[3] == 'O' and a[6] =='O') or
    (a[1] == 'O' and a[4] == 'O' and a[7] =='O') or
    (a[2] == 'O' and a[5] == 'O' and a[8] =='O') or
    (a[0] == 'O' and a[4] == 'O' and a[8] =='O') or
    (a[2] == 'O' and a[4] == 'O' and a[6] =='O')):
        return -1
    else:
        return 0

#Function that returns the depth of an array, a.
def find_depth(a):
    depth = 0
    for x in a:
        if x != ' ':
            depth += 1
    return depth

#Function that returns a list of next possible moves.
def find_next_moves(a, mark):
    moves = []
    i = 0
    while i < len(a):
        if a[i] == ' ':
            copy = [] + a
            copy[i] = mark
            moves.append(copy)
        i += 1
    return moves

#Function that returns the best result for the player whose turn it is if they
#make the move that results in array, a.
def minimax(a):
    #If game is finished, return winning state
    if finished(a):
        return win(a)
    else:
        #Get depth of game
        depth = find_depth(a)
        #Mark of current player
        mark = None
        #If it's X's turn
        if depth%2 == 0:
            mark = 'X'
            next_moves = find_next_moves(a, mark)
            next_values = list(map(minimax, next_moves))
            return max(next_values)
        #If it's O's turn
        else:
            mark = 'O'
            next_moves = find_next_moves(a, mark)
            next_values = list(map(minimax, next_moves))
            return min(next_values)

#Function that returns the next best move for player whose turn it is
def get_next_move(a):
    depth = find_depth(a)
    if depth % 2 == 0:
        mark = 'X'
        next_moves = find_next_moves(a, mark)
        next_move_values = list(map(minimax, next_moves))
        best_index = 0
        best_move_value = next_move_values[0]
        i = 1
        while i < len(next_move_values):
            if next_move_values[i] > best_move_value:
                best_move_value = next_move_values[i]
                best_index = i
            i += 1
        return next_moves[best_index]
    else:
        mark = 'O'
        next_moves = find_next_moves(a, mark)
        next_move_values = list(map(minimax, next_moves))
        best_index = 0
        best_move_value = next_move_values[0]
        i = 1
        while i < len(next_move_values):
            if next_move_values[i] < best_move_value:
                best_move_value = next_move_values[i]
                best_index = i
            i += 1
        return next_moves[best_index]
 
#Function that starts a new game.
def start():
    board = [' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ']
    complete = finished(board)
    while not complete:
        i = int(input())
        if board[i] == ' ':
            board[i] = 'X'
            complete = finished(board)
            if not complete:
                board = get_next_move(board)
                complete = finished(board)
                print(board)
        else:
            print("You can't do that.")
            print(board)
    winner = win(board)
    if winner == 1:
        print("Player Wins")
    elif winner == -1:
        print("Computer Wins")
    elif winner == 0:
        print("Draw")
#start()