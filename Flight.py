class Flight:
    def __init__(self, plane, destination, origin):
        self.plane = plane
        self.__destination = destination
        self.__origin = origin
        self.passengers_list = []

    def add_passengers(self, *passengers):
        for passenger in passengers:
            self.passengers_list.append(passenger)

    def get_destination(self):
        return self.__destination

    def get_origin(self):
        return self.__origin

    def get_passengers(self):
        return self.passengers_list

    def flight_details(self):
        pass_list = []
        for passenger in self.passengers_list:
            pass_list.append(passenger.get_name())
        return f'{self.plane.plane_number} is going to {self.get_destination().AirportName} from {self.get_origin().AirportName},' \
            f' passengers are: {pass_list}'

    def get_passports(self):
        pass_list = []
        for passenger in self.passengers_list:
            pass_list.append(passenger.passport_num)
        return pass_list

