class app:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * (n + 1) for _ in range(n + 1)]

    def handle_input(self, users, input_lst):
        # print(input_lst)
        if len(input_lst) == 1 and input_lst[0] == "SHOW":
            self.handle_show_all()
            return
        paying_user_id = int(input_lst[1][1])
        # print(paying_user_id)
        if len(input_lst) == 2 and input_lst[0] == "SHOW":
            users[paying_user_id].handle_show_user(self.board)
            return

        number_of_users = int(input_lst[3])
        if input_lst[0] == "EXPENSE":
            if input_lst[-1] == "EQUAL":
                users[paying_user_id].handle_equal(input_lst, self.board)
            elif input_lst[3 + number_of_users + 1] == "EXACT":
                users[paying_user_id].handle_exact(input_lst, self.board)
            elif input_lst[3 + number_of_users + 1] == "PERCENT":
                users[paying_user_id].handle_percent(input_lst, self.board)

    def handle_show_all(self):
        flag = 0
        for i in range(1, self.n + 1, 1):
            for j in range(1, self.n + 1, 1):
                if self.board[i][j] > 0:
                    flag = 1
                    print("u", i, "owes", "u", j, " ", self.board[i][j])

        if flag == 0:
            print("No balances")
