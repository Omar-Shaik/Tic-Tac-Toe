import Node

class Tree:
    def __init__(self):
        self.board = ["","","","","","","","",""]
        self.root = Node(node.board,0)


    def set_score(node):
        if node.height == 9:
            if(node.board[0] == "X" and node.board[1] == "X" and node.board[2] == "X" or
                node.board[3] == "X" and node.board[4] == "X" and node.board[5] == "X" or
                node.board[6] == "X" and node.board[7] == "X" and node.board[8] == "X" or
                node.board[0] == "X" and node.board[3] == "X" and node.board[6] == "X" or
                node.board[1] == "X" and node.board[4] == "X" and node.board[7] == "X" or
                node.board[2] == "X" and node.board[5] == "X" and node.board[8] == "X" or
                node.board[0] == "X" and node.board[4] == "X" and node.board[8] == "X" or
                node.board[2] == "X" and node.board[4] == "X" and node.board[6] == "X"):
                node.weight = 1
            elif(node.board[0] == "O" and node.board[1] == "O" and node.board[2] == "O" or
              node.board[3] == "O" and node.board[4] == "O" and node.board[5] == "O" or
              node.board[6] == "O" and node.board[7] == "O" and node.board[8] == "O" or
              node.board[0] == "O" and node.board[3] == "O" and node.board[6] == "O" or
              node.board[1] == "O" and node.board[4] == "O" and node.board[7] == "O" or
              node.board[2] == "O" and node.board[5] == "O" and node.board[8] == "O" or
              node.board[0] == "O" and node.board[4] == "O" and node.board[8] == "O" or
              node.board[2] == "O" and node.board[4] == "O" and node.board[6] == "O"):
              node.weight = -1
            else:
              node.weight = 0
        elif node.height < 9:
            if node.mark == "X":
                node.score = max(map(set_score,node.children))
            elif node.mark == "O":
                node.score = min(map(set_score,node.children))
        return node.score
