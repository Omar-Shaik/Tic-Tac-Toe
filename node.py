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


