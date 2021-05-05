class Snake_Ladder:
    board = [None] * 101

    def __init__(self):
        self.players = []
        self.number_of_snakes = None
        self.number_of_ladders = None
        self.number_of_players = None

    @staticmethod
    def playGame(player_obj, score):
        initial_position = player_obj.get_current_position()
        final_position = player_obj.get_final_position(
            score, Snake_Ladder.board)

        player_obj.current_position = final_position
        if final_position == 100:
            print(player_obj.name, " Won")
            return True
        else:
            print(player_obj.name, " rolls a dice ", score, " moves from ",
                  initial_position, " to ", final_position)
            return False
