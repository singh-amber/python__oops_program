class board:
    def __init__(self):
        self.board = [[''] * 3 for _ in range(3)]

    def check_validity(self, x, y):
        if self.board[x][y] == '' and 0 <= x <= 2 and 0 <= y <= 2:
            return True
        return False

    def check_row(self):
        for i in range(3):
            if self.board[i][0] != '' and self.board[i][1] != '' and self.board[i][2] != '' and self.board[i][0] == \
                    self.board[i][1] == self.board[i][2]:
                return True
        return False

    def check_columns(self):
        for j in range(3):
            if self.board[0][j] != '' and self.board[1][j] != '' and self.board[2][j] != '' and self.board[0][j] == \
                    self.board[1][j] == self.board[2][j]:
                return True
        return False

    def check_diagonals(self):
        if self.board[0][0] != '' and self.board[1][1] != '' and self.board[2][2] != '' and self.board[0][0] == \
                self.board[1][1] == self.board[2][2]:
            return True
        if self.board[0][2] != '' and self.board[1][1] != '' and self.board[2][0] != '' and self.board[0][2] == \
                self.board[1][1] == self.board[2][0]:
            return True

        return False

    def has_won(self):
        if self.check_row() or self.check_columns() or self.check_diagonals():
            return True
        return False
