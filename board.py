import Tkinter as t


class Board:
    def __init__(self):
        self.window = t.Tk()
        self.window.title("Tic Tac Toe")
        self.mark = "X"
        self.b0 = t.StringVar()
        self.b1 = t.StringVar()
        self.b2 = t.StringVar()
        self.b3 = t.StringVar()
        self.b4 = t.StringVar()
        self.b5 = t.StringVar()
        self.b6 = t.StringVar()
        self.b7 = t.StringVar()
        self.b8 = t.StringVar()
        self.button0 = t.Button(self.window, textvariable=self.b0, font='Times 20 bold', bg='black', fg='white',
                                height=5, width=10, command=self.update_b0)
        self.button0.grid(row=1, column=0)
        self.button1 = t.Button(self.window, textvariable=self.b1, font='Times 20 bold', bg='black', fg='white',
                                height=5, width=10, command=self.update_b1)
        self.button1.grid(row=1, column=1)
        self.button2 = t.Button(self.window, textvariable=self.b2, font='Times 20 bold', bg='black', fg='white',
                                height=5, width=10, command=self.update_b2)
        self.button2.grid(row=1, column=2)
        self.button3 = t.Button(self.window, textvariable=self.b3, font='Times 20 bold', bg='black', fg='white',
                                height=5, width=10, command=self.update_b3)
        self.button3.grid(row=2, column=0)
        self.button4 = t.Button(self.window, textvariable=self.b4, font='Times 20 bold', bg='black', fg='white',
                                height=5, width=10, command=self.update_b4)
        self.button4.grid(row=2, column=1)
        self.button5 = t.Button(self.window, textvariable=self.b5, font='Times 20 bold', bg='black', fg='white',
                                height=5, width=10, command=self.update_b5)
        self.button5.grid(row=2, column=2)
        self.button6 = t.Button(self.window, textvariable=self.b6, font='Times 20 bold', bg='black', fg='white',
                                height=5, width=10, command=self.update_b6)
        self.button6.grid(row=3, column=0)
        self.button7 = t.Button(self.window, textvariable=self.b7, font='Times 20 bold', bg='black', fg='white',
                                height=5, width=10, command=self.update_b7)
        self.button7.grid(row=3, column=1)
        self.button8 = t.Button(self.window, textvariable=self.b8, font='Times 20 bold', bg='black', fg='white',
                                height=5, width=10, command=self.update_b8)
        self.button8.grid(row=3, column=2)

    def switch_mark(self):
        if self.mark == "X":
            self.mark = "O"
        else:
            self.mark = "X"

    def update_b0(self):
        self.b0.set(self.mark)
        self.switch_mark()

    def update_b1(self):
        self.b1.set(self.mark)
        self.switch_mark()

    def update_b2(self):
        self.b2.set(self.mark)
        self.switch_mark()

    def update_b3(self):
        self.b3.set(self.mark)
        self.switch_mark()

    def update_b4(self):
        self.b4.set(self.mark)
        self.switch_mark()

    def update_b5(self):
        self.b5.set(self.mark)
        self.switch_mark()

    def update_b6(self):
        self.b6.set(self.mark)
        self.switch_mark()

    def update_b7(self):
        self.b7.set(self.mark)
        self.switch_mark()

    def update_b8(self):
        self.b8.set(self.mark)
        self.switch_mark()
