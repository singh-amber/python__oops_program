from random_generator import randomCellGenerator
from board import boardGame
from user import User

if __name__ == "__main__":
    user1 = User()
    user2 = User()
    x, y = randomCellGenerator.get_random_cell(user1.board_obj.board)
    user1.board_obj.board[x][y] = 2
    x, y = randomCellGenerator.get_random_cell(user1.board_obj.board)
    user1.board_obj.board[x][y] = 2

    x, y = randomCellGenerator.get_random_cell(user2.board_obj.board)
    user2.board_obj.board[x][y] = 2
    x, y = randomCellGenerator.get_random_cell(user2.board_obj.board)
    user2.board_obj.board[x][y] = 2

    print("User1 board is")
    for j in range(4):
        print(user1.board_obj.board[j])
    print("User2 board is", user2.board_obj.board)
    for j in range(4):
        print(user2.board_obj.board[j])
    i = 0
    while True:
        i = i % 2
        if i == 0:
            print("Player 1 Make a move:-")
            isStop = user1.make_a_move(i)
        else:
            print("Player 2 Make a move:-")
            isStop = user2.make_a_move(i)
        if isStop:
            break
        i += 1
