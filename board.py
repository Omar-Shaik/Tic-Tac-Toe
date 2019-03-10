from tree import Tree
from tkinter import Tk, Button, font, StringVar
import tkinter as tk


class Board:
    def __init__(self):
        self.game_tree = Tree()
        self.window = Tk()
        self.window.resizable(width=False, height=False)
        self.window.title('Tic Tac Toe')
        self.current_board = self.game_tree.root
        self.mark = "X"
        self.empty = ["","","","","","","","",""] #HOW TO LINK THIS ARRAY TO THE CURRENT BOARD STATE?
        
        self.b0 = tk.StringVar()
        self.b1 = tk.StringVar()
        self.b2 = tk.StringVar()
        self.b3 = tk.StringVar()
        self.b4 = tk.StringVar()
        self.b5 = tk.StringVar()
        self.b6 = tk.StringVar()
        self.b7 = tk.StringVar()
        self.b8 = tk.StringVar()

        self.button0 = tk.Button(self.window, font='Arial 25 bold', bg='black', fg='white', height=5, width=10, command=self.update_b0)
        self.button1 = tk.Button(self.window, text='', font='Arial 25 bold', bg='black', fg='white', height=5, width=10, command=self.update_b1)
        self.button2 = tk.Button(self.window, text='', font='Arial 25 bold', bg='black', fg='white', height=5, width=10, command=self.update_b2)
        self.button3 = tk.Button(self.window, text='', font='Arial 25 bold', bg='black', fg='white', height=5, width=10, command=self.update_b3)
        self.button4 = tk.Button(self.window, text='', font='Arial 25 bold', bg='black', fg='white', height=5, width=10, command=self.update_b4)
        self.button5 = tk.Button(self.window, text='', font='Arial 25 bold', bg='black', fg='white', height=5, width=10, command=self.update_b5)
        self.button6 = tk.Button(self.window, text='', font='Arial 25 bold', bg='black', fg='white', height=5, width=10, command=self.update_b6)
        self.button7 = tk.Button(self.window, text='', font='Arial 25 bold', bg='black', fg='white', height=5, width=10, command=self.update_b7)
        self.button8 = tk.Button(self.window, text='', font='Arial 25 bold', bg='black', fg='white', height=5, width=10, command=self.update_b8)

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

    '''def switch_mark(self):
        if self.mark == "X":
            self.mark = "O"
        else:
            self.mark = "X"'''

    def update_b0(self):
        self.button0["text"] = self.mark
        #self.switch_mark()

    def update_b1(self):
        self.button1["text"] = self.mark
        #self.switch_mark()

    def update_b2(self):
        self.button2["text"] = self.mark
        #self.switch_mark()

    def update_b3(self):
        self.button3["text"] = self.mark
        #self.switch_mark()

    def update_b4(self):
        self.button4["text"] = self.mark
        #self.switch_mark()

    def update_b5(self):
        self.button5["text"] = self.mark
        #self.switch_mark()

    def update_b6(self):
        self.button6["text"] = self.mark
        #self.switch_mark()

    def update_b7(self):
        self.button7["text"] = self.mark
        #self.switch_mark()

    def update_b8(self):
        self.button8["text"] = self.mark
        #self.switch_mark()

    def mainloop(self):
        self.window.mainloop()

    #THIS DOESNT SEEM TO BE DOING ANYTHING AS LONG AS THE BOARD IS NOT LINKED TO THE 
    #ARRAY AT ALL. 
    def winner(self):
        if (Tree().set_score == True):
            Tree().winx

if __name__ == '__main__':
    Board().mainloop()
