class Aircraft:
    def __init__(self, flights=True):
        self.flights = flights


class Helicopter(Aircraft):
    def __init__(self, amount_of_blades,flights):
        super().__init__(flights)
        self.amount_of_blades = amount_of_blades


class Airplane(Aircraft):
    def __init__(self, plane_number, company, flights):
        super().__init__(flights)
        self.plane_number = plane_number
        self.company = company
