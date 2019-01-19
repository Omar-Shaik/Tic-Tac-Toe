class Node:
    def __init__(self, new_board, prev_mark):
        self.board = new_board
        self.weight = None
        self.mark = not prev_mark
        self.children = []
        self.set_weight()
        self.create_children()
        self.sum_weight()

    def set_weight(self):
        if (self.board[0] == "X" and self.board[1] == "X" and self.board[2] == "X" or
                self.board[3] == "X" and self.board[4] == "X" and self.board[5] == "X" or
                self.board[6] == "X" and self.board[7] == "X" and self.board[8] == "X" or
                self.board[0] == "X" and self.board[3] == "X" and self.board[6] == "X" or
                self.board[1] == "X" and self.board[4] == "X" and self.board[7] == "X" or
                self.board[2] == "X" and self.board[5] == "X" and self.board[8] == "X" or
                self.board[0] == "X" and self.board[4] == "X" and self.board[8] == "X" or
                self.board[2] == "X" and self.board[4] == "X" and self.board[6] == "X"):
            self.weight = 1
        elif (self.board[0] == "O" and self.board[1] == "O" and self.board[2] == "O" or
              self.board[3] == "O" and self.board[4] == "O" and self.board[5] == "O" or
              self.board[6] == "O" and self.board[7] == "O" and self.board[8] == "O" or
              self.board[0] == "O" and self.board[3] == "O" and self.board[6] == "O" or
              self.board[1] == "O" and self.board[4] == "O" and self.board[7] == "O" or
              self.board[2] == "O" and self.board[5] == "O" and self.board[8] == "O" or
              self.board[0] == "O" and self.board[4] == "O" and self.board[8] == "O" or
              self.board[2] == "O" and self.board[4] == "O" and self.board[6] == "O"):
            self.weight = -1
        elif self.board[0] != "" and self.board[1] != "" and self.board[2] != "" and self.board[3] != "" and self.board[4] != "" and self.board[5] != "" and self.board[6] != "" and self.board[7] != "" and self.board[8] == "":
            self.weight = 0

    def create_children(self):
        i = 0
        while i < len(self.board):
            if self.board[i] == "":
                x = self.board
                if self.mark:
                    x[i] = "X"
                else:
                    x[i] = "O"
                n = Node(x, self.mark)
                self.children.append(n)
            i += 1

    def sum_weight(self):
        self.weight = 0
        for x in self.children:
            self.weight += x.weight
