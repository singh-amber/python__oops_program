class user:
    def __init__(self, user_id, name, email, mobile_number):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.mobile_number = mobile_number

    def handle_equal(self, input_lst, mat):
        # paying_user_id = input_lst[1]
        paying_amount = int(input_lst[2])
        number_of_users = int(input_lst[3])
        # print(input_lst)
        # print(paying_amount)
        # print(number_of_users)

        other_users = input_lst[4:-1]
        # print(other_users)
        for a_user in other_users:
            user_id = int(a_user[1:])
            if user_id == self.user_id:
                continue
            # print(user_id, self.user_id)
            mat[user_id][self.user_id] = mat[user_id][self.user_id] + paying_amount / number_of_users
            mat[self.user_id][user_id] = mat[self.user_id][user_id] - paying_amount / number_of_users
            # print(mat[user_id][self.user_id], mat[self.user_id][user_id])

    def handle_percent(self, input_lst, mat):
        paying_amount = int(input_lst[2])
        number_of_users = int(input_lst[3])

        other_users = input_lst[4:4 + number_of_users]
        percent_of_users = input_lst[-number_of_users:]
        for index, a_user in enumerate(other_users):
            user_id = int(a_user[1:])
            mat[user_id][self.user_id] = mat[user_id][self.user_id] + ((int(percent_of_users[index]) / 100) * paying_amount)
            mat[self.user_id][user_id] = mat[self.user_id][user_id] - ((int(percent_of_users[index]) / 100) * paying_amount)

    def handle_exact(self, input_lst, mat):
        paying_amount = int(input_lst[2])
        number_of_users = int(input_lst[3])

        other_users = input_lst[4:4 + number_of_users]
        amount_of_users = input_lst[-number_of_users:]
        for index, a_user in enumerate(other_users):
            user_id = int(a_user[1:])
            mat[user_id][self.user_id] = mat[user_id][self.user_id] + int(amount_of_users[index])
            mat[self.user_id][user_id] = mat[self.user_id][user_id] - int(amount_of_users[index])

    def handle_show_user(self, mat):
        print(self.user_id)
        print(mat[self.user_id])
        flag = 0
        for j in range(1, len(mat[0]), 1):
            if mat[self.user_id][j] == 0:
                continue

            flag = 1
            if mat[self.user_id][j] < 0:
                print("u", j, "owes", "u", self.user_id, " ", -1*mat[self.user_id][j])
            else:
                print("u", self.user_id, "owes", "u", j, " ", mat[self.user_id][j])
        if flag == 0:
            print("No balances")



