class player:
    def __init__(self, name, piece):
        self.piece = piece
        self.name = name

    def make_a_move(self, board, x, y):
        board[x][y] = self.piece




