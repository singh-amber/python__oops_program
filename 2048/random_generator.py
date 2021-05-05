import random

class randomCellGenerator:
    def __init__(self):
        pass

    @staticmethod
    def get_random_cell(board):
        lst = []
        for i in range(4):
            for j in range(4):
                if board[i][j] != 0:
                    continue
                lst.append((i, j))

        if len(lst) == 0:
            return (-1, -1)
        index = random.randint(0, len(lst)-1)
        return lst[index]