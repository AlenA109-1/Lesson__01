class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def userName(self):
        print(f'Имя: {self.first_name}')

    def userSurname(self):
        print(f'Фамилия: {self.last_name}')

    def userFullName(self):
        print(f'Имя, Фамилия: {self.first_name}, {self.last_name}')