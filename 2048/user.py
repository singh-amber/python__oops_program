from random_generator import randomCellGenerator
from board import boardGame


class User:
    def __init__(self):
        self.board_obj = boardGame()

    def make_a_move(self, i):
        move = int(input())
        dec = False
        if move == 2:
            dec = self.board_obj.handling_top_move()
        elif move == 3:
            dec = self.board_obj.handling_bottom_move()
        elif move == 0:
            dec = self.board_obj.handling_left_move()
        elif move == 1:
            dec = self.board_obj.handling_right_move()

        # print(self.board_obj.board)
        if dec:
            for j in range(4):
                print(self.board_obj.board[j])
            print(i+1, " Won")
            return True

        x, y = randomCellGenerator.get_random_cell(self.board_obj.board)
        if x == -1 and y == -1:
            print(i+1, " lost")
            return True
        self.board_obj.board[x][y] = 2
        for j in range(4):
            print(self.board_obj.board[j])
        return False
