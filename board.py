import os
import sys
from tkinter import Tk, Button, font, StringVar, messagebox
import tkinter as tk
from game import *
import game as g

class Board:
    def __init__(self):
        self.index = None
        self.window = Tk()
        self.window.resizable(width=False, height=False)
        self.window.title('Tic Tac Toe')
        self.board = [' ',' ',' ',' ',' ',' ',' ',' ',' '] 

        self.b0 = tk.StringVar()
        self.b1 = tk.StringVar()
        self.b2 = tk.StringVar()
        self.b3 = tk.StringVar()
        self.b4 = tk.StringVar()
        self.b5 = tk.StringVar()
        self.b6 = tk.StringVar()
        self.b7 = tk.StringVar()
        self.b8 = tk.StringVar()

        self.button0 = tk.Button(self.window, text='', font='Arial 25 bold', bg='#cdc9c9', fg='black', height=3, width=5, command=self.update_b0)
        self.button1 = tk.Button(self.window, text='', font='Arial 25 bold', bg='#cdc9c9', fg='black', height=3, width=5, command=self.update_b1)
        self.button2 = tk.Button(self.window, text='', font='Arial 25 bold', bg='#cdc9c9', fg='black', height=3, width=5, command=self.update_b2)
        self.button3 = tk.Button(self.window, text='', font='Arial 25 bold', bg='#cdc9c9', fg='black', height=3, width=5, command=self.update_b3)
        self.button4 = tk.Button(self.window, text='', font='Arial 25 bold', bg='#cdc9c9', fg='black', height=3, width=5, command=self.update_b4)
        self.button5 = tk.Button(self.window, text='', font='Arial 25 bold', bg='#cdc9c9', fg='black', height=3, width=5, command=self.update_b5)
        self.button6 = tk.Button(self.window, text='', font='Arial 25 bold', bg='#cdc9c9', fg='black', height=3, width=5, command=self.update_b6)
        self.button7 = tk.Button(self.window, text='', font='Arial 25 bold', bg='#cdc9c9', fg='black', height=3, width=5, command=self.update_b7)
        self.button8 = tk.Button(self.window, text='', font='Arial 25 bold', bg='#cdc9c9', fg='black', height=3, width=5, command=self.update_b8)

        self.button0["text"] = ""
        self.button1["text"] = ""
        self.button2["text"] = ""
        self.button3["text"] = ""
        self.button4["text"] = ""
        self.button5["text"] = ""
        self.button6["text"] = ""
        self.button7["text"] = ""
        self.button8["text"] = ""

        self.button0.grid(row=1, column=0)
        self.button1.grid(row=1, column=1)
        self.button2.grid(row=1, column=2)
        self.button3.grid(row=2, column=0)
        self.button4.grid(row=2, column=1)
        self.button5.grid(row=2, column=2)
        self.button6.grid(row=3, column=0)
        self.button7.grid(row=3, column=1)
        self.button8.grid(row=3, column=2)

    def update(self):
        self.button0["text"] = self.board[0]
        self.button1["text"] = self.board[1]
        self.button2["text"] = self.board[2]
        self.button3["text"] = self.board[3]
        self.button4["text"] = self.board[4]
        self.button5["text"] = self.board[5]
        self.button6["text"] = self.board[6]
        self.button7["text"] = self.board[7]
        self.button8["text"] = self.board[8]

    def update_b0(self):
        #self.button0["text"] = self.mark
        index = 0
        complete = g.finished(self.board)
        if self.board[index] == ' ' and not complete:
            self.board[index] = 'X'
            self.update()
            complete = g.finished(self.board)
            if not complete:
                self.board = g.get_next_move(self.board)
                self.update()
                complete = g.finished(self.board)
        if complete:
            winner = g.win(self.board)
            if winner == 1:
                #print("Player Wins")
                tk.messagebox.askretrycancel("Player Wins", "The Winner is Player!" + "\n" + "Would you like to play again?")
            elif winner == -1:
                #print("Computer Wins")
                ask = tk.messagebox.askretrycancel("Computer Wins", "The Winner is Computer!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)
            elif winner == 0:
                ask = tk.messagebox.askretrycancel("Draw", "The Match was a DRAW!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)


    def update_b1(self):
        #self.button1["text"] = self.mark
        index = 1
        complete = g.finished(self.board)
        if self.board[index] == ' ' and not complete:
            self.board[index] = 'X'
            self.update()
            complete = g.finished(self.board)
            if not complete:
                self.board = g.get_next_move(self.board)
                self.update()
                complete = g.finished(self.board)
        if complete:
            winner = g.win(self.board)
            if winner == 1:
                #print("Player Wins")
                ask = tk.messagebox.askretrycancel("Player Wins", "The Winner is Player!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)
            elif winner == -1:
                #print("Computer Wins")
                ask = tk.messagebox.askretrycancel("Computer Wins", "The Winner is Computer!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)
            elif winner == 0:
                ask = tk.messagebox.askretrycancel("Draw", "The Match was a DRAW!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)

    def update_b2(self):
        #self.button2["text"] = self.mark

        index = 2
        complete = g.finished(self.board)
        if self.board[index] == ' ' and not complete:
            self.board[index] = 'X'
            self.update()
            complete = g.finished(self.board)
            if not complete:
                self.board = g.get_next_move(self.board)
                self.update()
                complete = g.finished(self.board)
        if complete:
            winner = g.win(self.board)
            if winner == 1:
                #print("Player Wins")
                ask = tk.messagebox.askretrycancel("Player Wins", "The Winner is Player!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)
            elif winner == -1:
                #print("Computer Wins")
                ask = tk.messagebox.askretrycancel("Computer Wins", "The Winner is Computer!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)
            elif winner == 0:
                ask = tk.messagebox.askretrycancel("Draw", "The Match was a DRAW!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)


    def update_b3(self):
        #self.button3["text"] = self.mark

        index = 3
        complete = g.finished(self.board)
        if self.board[index] == ' ' and not complete:
            self.board[index] = 'X'
            self.update()
            complete = g.finished(self.board)
            if not complete:
                self.board = g.get_next_move(self.board)
                self.update()
                complete = g.finished(self.board)
        if complete:
            winner = g.win(self.board)
            if winner == 1:
                #print("Player Wins")
                ask = tk.messagebox.askretrycancel("Player Wins", "The Winner is Player!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)
            elif winner == -1:
                #print("Computer Wins")
                ask = tk.messagebox.askretrycancel("Computer Wins", "The Winner is Computer!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)
            elif winner == 0:
                ask = tk.messagebox.askretrycancel("Draw", "The Match was a DRAW!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)

    def update_b4(self):
        #self.button4["text"] = self.mark

        index = 4
        complete = g.finished(self.board)
        if self.board[index] == ' ' and not complete:
            self.board[index] = 'X'
            self.update()
            complete = g.finished(self.board)
            if not complete:
                self.board = g.get_next_move(self.board)
                self.update()
                complete = g.finished(self.board)
        if complete:
            winner = g.win(self.board)
            if winner == 1:
                #print("Player Wins")
                ask = tk.messagebox.askretrycancel("Player Wins", "The Winner is Player!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)
            elif winner == -1:
                #print("Computer Wins")
                ask = tk.messagebox.askretrycancel("Computer Wins", "The Winner is Computer!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)
            elif winner == 0:
                ask = tk.messagebox.askretrycancel("Draw", "The Match was a DRAW!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)


    def update_b5(self):
        #self.button5["text"] = self.mark

        index = 5
        complete = g.finished(self.board)
        if self.board[index] == ' ' and not complete:
            self.board[index] = 'X'
            self.update()
            complete = g.finished(self.board)
            if not complete:
                self.board = g.get_next_move(self.board)
                self.update()
                complete = g.finished(self.board)
        if complete:
            winner = g.win(self.board)
            if winner == 1:
                #print("Player Wins")
                ask = tk.messagebox.askretrycancel("Player Wins", "The Winner is Player!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)
            elif winner == -1:
                #print("Computer Wins")
                ask = tk.messagebox.askretrycancel("Computer Wins", "The Winner is Computer!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)
            elif winner == 0:
                ask = tk.messagebox.askretrycancel("Draw", "The Match was a DRAW!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)


    def update_b6(self):
        #self.button6["text"] = self.mark

        index = 6
        complete = g.finished(self.board)
        if self.board[index] == ' ' and not complete:
            self.board[index] = 'X'
            self.update()
            complete = g.finished(self.board)
            if not complete:
                self.board = g.get_next_move(self.board)
                self.update()
                complete = g.finished(self.board)
        if complete:
            winner = g.win(self.board)
            if winner == 1:
                #print("Player Wins")
                ask = tk.messagebox.askretrycancel("Player Wins", "The Winner is Player!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)
            elif winner == -1:
                #print("Computer Wins")
                ask = tk.messagebox.askretrycancel("Computer Wins", "The Winner is Computer!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)
            elif winner == 0:
                ask = tk.messagebox.askretrycancel("Draw", "The Match was a DRAW!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)

    def update_b7(self):
        #self.button7["text"] = self.mark

        index = 7
        complete = g.finished(self.board)
        if self.board[index] == ' ' and not complete:
            self.board[index] = 'X'
            self.update()
            complete = g.finished(self.board)
            if not complete:
                self.board = g.get_next_move(self.board)
                self.update()
                complete = g.finished(self.board)
        if complete:
            winner = g.win(self.board)
            if winner == 1:
                #print("Player Wins")
                ask = tk.messagebox.askretrycancel("Player Wins", "The Winner is Player!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)
            elif winner == -1:
                #print("Computer Wins")
                ask = tk.messagebox.askretrycancel("Computer Wins", "The Winner is Computer!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)
            elif winner == 0:
                ask = tk.messagebox.askretrycancel("Draw", "The Match was a DRAW!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)


    def update_b8(self):
        #self.button8["text"] = self.mark

        index = 8
        complete = g.finished(self.board)
        if self.board[index] == ' ' and not complete:
            self.board[index] = 'X'
            self.update()
            complete = g.finished(self.board)
            if not complete:
                self.board = g.get_next_move(self.board)
                self.update()
                complete = g.finished(self.board)
        if complete:
            winner = g.win(self.board)
            if winner == 1:
                #print("Player Wins")
                ask = tk.messagebox.askretrycancel("Player Wins", "The Winner is Player!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)
            elif winner == -1:
                #print("Computer Wins")
                ask = tk.messagebox.askretrycancel("Computer Wins", "The Winner is Computer!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)
            elif winner == 0:
                ask = tk.messagebox.askretrycancel("Draw", "The Match was a DRAW!" + "\n" + "Would you like to play again?")
                if ask == True:
                    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                else:
                    sys.exit(0)


    def mainloop(self):
        self.window.mainloop()

if __name__ == '__main__':
    Board().mainloop()
