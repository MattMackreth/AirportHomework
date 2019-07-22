class People:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return self.first_name + ' ' + self.last_name


class Passenger(People):
    def __init__(self, first_name, last_name, passport_num):
        super().__init__(first_name, last_name)
        self.passport_num = passport_num

