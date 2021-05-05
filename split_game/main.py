from user import user
from app import app

if __name__ == "__main__":
    users = [None]
    users.append(user(1, "Vimal", "vimal@email.com", 1234567890))
    users.append(user(2, "Kesari", "kesari@email.com", 1234567891))
    users.append(user(3, "Ranjeet", "ranjeet@email.com", 1234567892))
    users.append(user(4, "Biswa", "biswa@email.com", 1234567893))


    app_obj = app(len(users))
    while True:
        input_lst = list(input().split())
        app_obj.handle_input(users, input_lst)




