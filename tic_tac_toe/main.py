from player import player
from board import board

if __name__ == "__main__":

    board_obj = board()
    for lst in board_obj.board:
        print(lst)
    # player1 = player(input(), "X")
    # player2 = player(input(), "O")

    player1 = player("Gaurav", "X")
    player2 = player("Sagar", "O")

    print(player1.piece, player1.name)
    print(player2.piece, player2.name)

    i = 0
    while True:
        temp = list(map(int, input().split()))
        x, y = temp[0]-1, temp[1]-1
        isValid = board_obj.check_validity(x, y)
        if not isValid:
            print("Invalid Move")
            continue

        i = i % 2
        if i == 0:
            player1.make_a_move(board_obj.board, x, y)
        elif i == 1:
            player2.make_a_move(board_obj.board, x, y)

        for j in range(3):
            print(board_obj.board[j])
        dec = board_obj.has_won()
        if dec:
            print(i+1, "won")
            temp = ''
            while temp != "exit":
                temp = input()
            if temp == 'exit':
                print(temp)
                break
        i += 1




