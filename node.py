class Node:
    def __init__(self, new_board, height):
        self.board = new_board
        self.height = height
        self.score = None
        self.children = []
        self.mark = "X"
        self.set_mark()

    def set_mark(self):
        if self.height % 2 == 1:
            self.mark = "O"
    
    def create_children(node):
        if node.height < 9:
            i = 0
            while i < len(node.board):
                local_board = node.board
                if node.board[i] == "":
                    local_board[i] = node.mark
                n = Node(local_board, node.height+1)
                node.children.append(n)
                i += 1

