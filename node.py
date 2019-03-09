class Node:
    def __init__(self, new_board, height, count):
        self.board = [] + new_board
        self.height = height + 1
        self.count = count
        self.count[0] += 1
        print(count)
        print("Hi, I am " + str(self.height) + " nodes deep")
        print(self.board)
        self.score = None
        self.children = []
        self.mark = "X"
        self.set_mark()

    def set_mark(self):
        if self.height % 2 == 1:
            self.mark = "O"

    def create_children(self):
        if self.height < 9:
            i = 0
            while i < len(self.board):
                local_board = [] + self.board
                if self.board[i] == "":
                    local_board[i] = self.mark
                    n = Node(local_board, 0+self.height, self.count)
                    n.create_children()
                    self.children.append(n)
                i += 1

