import board as b
import node as n
#import tkMessageBox as mb

empty_board = ["", "", "", "", "", "", "", "", ""]
start = n.Node(empty_board, False)
pointer = start
mark = raw_input("Do you want to be X's or O's?")
turn = ""
if mark == "X":
    turn = "Player"

while pointer.children:
    if turn == "Player":
        print "This part still has to be implemented"
    else:
        next_move = pointer.children[0]
        for x in pointer.children:
            if x.weight > next_move.weight:
                next_move = x
        pointer = next_move

board = b.Board()
board.window.mainloop()

#mb.showinfo("You Won!")
