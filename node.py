class Node:
    def __init__(self, new_board, height):
        self.board = new_board
        self.height = height
        self.score = None
        self.children = []
        self.mark = "X"
        self.set_mark()
        self.create_children()

    def set_mark(self):
        if self.height % 2 == 1:
            self.mark = "O"

    def create_children(self):
        if self.height < 9:
            i = 0
            while i < len(self.board):
                local_board = self.board
                if self.board[i] == "":
                    local_board[i] = self.mark
                n = Node(local_board, self.height+1)
                self.children.append(n)
                i += 1

