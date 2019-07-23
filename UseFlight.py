from Aircraft import Airplane
from People import Passenger
from Flight import Flight
from Airport import Airport

passenger1 = Passenger('Matt', 'Mackreth','PN123456')
passenger2 = Passenger('Filipe', 'Paiva', '10308408108')
passenger3 = Passenger('Markson', 'Aigbodi', '2004910940')

my_plane1 = Airplane(1, 'Big Airline', True)
my_plane2 = Airplane(2, 'Medium Jet', True)

my_airport1 = Airport('Markson International', 'England')
my_airport2 = Airport('Hamza Airport', 'Italy')
my_airport3 = Airport('Adam Local', 'Ireland', False)

my_flight1 = Flight(my_plane1, my_airport1, my_airport2)
my_flight2 = Flight(my_plane2, my_airport2, my_airport3)

my_flight1.add_passengers(passenger1)
my_flight2.add_passengers(passenger2, passenger3)

for flight in (my_flight1, my_flight2):
    print(flight.flight_details())

print(my_flight2.get_passports())