from board import Snake_Ladder
from snake import snake
from ladder import ladder
from player import player

if __name__ == "__main__":
    snake_ladder_obj = Snake_Ladder()

    try:
        f = open('input.txt', 'r')
        snake_ladder_obj.number_of_snakes = int(f.readline()[:-1])

        for i in range(snake_ladder_obj.number_of_snakes):
            temp = list(map(int, f.readline()[:-1].split()))
            head, tail = temp[0], temp[1]
            snake_ladder_obj.board[head] = snake(head, tail)

        snake_ladder_obj.number_of_ladders = int(f.readline()[:-1])
        for i in range(snake_ladder_obj.number_of_ladders):
            temp = list(map(int, f.readline()[:-1].split()))
            bottom, top = temp[0], temp[1]
            snake_ladder_obj.board[bottom] = ladder(top, bottom)

        snake_ladder_obj.number_of_players = int(f.readline()[:-1])
        for i in range(snake_ladder_obj.number_of_players):
            name = f.readline()[:-1]
            snake_ladder_obj.players.append(player(name, 0))

        turn = 0
        while True:
            turn = turn % snake_ladder_obj.number_of_players
            score = snake_ladder_obj.players[turn].make_a_move()
            dec = Snake_Ladder.playGame(snake_ladder_obj.players[turn], score)
            if dec:
                break
            turn += 1

        f.close()
    except Exception as e:
        print("Exception is ", e)
    finally:
        print("Done with the program")


