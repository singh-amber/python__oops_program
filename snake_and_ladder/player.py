from snake import snake
from dice import dice


class player:
    def __init__(self, name, current_position):
        self.name = name
        self.current_position = current_position

    def get_current_position(self):
        return self.current_position

    def get_final_position(self, score, board):
        final_position = min(self.get_current_position()+score, 100)
        if final_position == 100:
            return final_position

        while board[final_position] is not None:
            if isinstance(board[final_position], snake):
                final_position = board[final_position].tail
            else:
                final_position = board[final_position].top

        final_position = min(final_position, 100)
        return final_position

    def make_a_move(self):
        return dice.roll_dice()
