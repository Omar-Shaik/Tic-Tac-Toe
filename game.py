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
