class User:
    User_DB = {}
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.rides_taken = 0
        self.rides_offered = 0
        self.User_DB[name] = self