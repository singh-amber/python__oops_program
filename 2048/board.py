class boardGame:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]

    @staticmethod
    def applying_gravity_to_left(lst):
        if len(lst) == 0:
            return []
        elif len(lst) == 1:
            return lst
        elif len(lst) == 2:
            if lst[0] == lst[1]:
                return [lst[0] + lst[1]]
            else:
                return lst
        elif len(lst) == 3:
            if lst[0] == lst[1]:
                return [lst[0] + lst[1], lst[2]]
            elif lst[1] == lst[2]:
                return [lst[0], lst[1] + lst[2]]
            else:
                return lst
        elif len(lst) == 4:
            if lst[0] == lst[1] and lst[2] == lst[3]:
                return [lst[0] + lst[1], lst[2] + lst[3]]
            elif lst[0] == lst[1] and lst[2] != lst[3]:
                return [lst[0] + lst[1], lst[2], lst[3]]
            elif lst[1] == lst[2]:
                return [lst[0], lst[1] + lst[2], lst[3]]
            elif lst[0] != lst[1] and lst[2] == lst[3]:
                return [lst[0], lst[1], lst[2] + lst[3]]
            else:
                return lst

    def handling_top_move(self):
        for j in range(4):
            lst = []
            for i in range(4):
                if self.board[i][j] != 0:
                    lst.append(self.board[i][j])
                    self.board[i][j] = 0
            lst = boardGame.applying_gravity_to_left(lst)
            for i in range(len(lst)):
                if lst[i] == 2048:
                    return True
                self.board[i][j] = lst[i]

        return False

    def handling_bottom_move(self):
        for j in range(4):
            lst = []
            for i in range(3, -1, -1):
                if self.board[i][j] != 0:
                    lst.append(self.board[i][j])
                    self.board[i][j] = 0
            lst = boardGame.applying_gravity_to_left(lst)
            for i in range(0, len(lst), 1):
                if lst[i] == 2048:
                    return True
                self.board[3 - i][j] = lst[i]
        return False

    def handling_left_move(self):
        for i in range(4):
            lst = []
            for j in range(4):
                if self.board[i][j] != 0:
                    lst.append(self.board[i][j])
                    self.board[i][j] = 0

            lst = boardGame.applying_gravity_to_left(lst)
            for j in range(len(lst)):
                if lst[j] == 2048:
                    return True
                self.board[i][j] = lst[j]
        return False

    def handling_right_move(self):
        for i in range(4):
            lst = []
            for j in range(3, -1, -1):
                if self.board[i][j] != 0:
                    lst.append(self.board[i][j])
                    self.board[i][j] = 0
            lst = boardGame.applying_gravity_to_left(lst)
            for j in range(len(lst)):
                if lst[j] == 2048:
                    return True
                self.board[i][3 - j] = lst[j]
        return False
