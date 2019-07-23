from Flight import Flight
from Aircraft import Airplane
from Airport import Airport
from People import Passenger

plane1 = Airplane('12414', 'Virgin', True)
plane2 = Airplane(12345, 'British Airways', True)

airport1 = Airport('Heathrow', 'England', True)
airport2 = Airport('LAX', 'USA', True)

flight1 = Flight(plane1, airport1, airport2)
flight2 = Flight(plane2, airport2, airport2)

passenger1 = Passenger('Matt', 'Mackreth', 30940239402)
passenger2 = Passenger('Person', 'Test Name', '30932091039')


def test_flight_details():
    assert flight1.flight_details() == '12414 is going to Heathrow from LAX, passengers are: []'


def test_get_passengers():
    assert flight1.get_passengers() == []


def test_get_passengers2():
    flight1.add_passengers(passenger1)
    assert flight1.get_passengers() == [passenger1]


def test_get_passports():
    assert flight1.get_passports() == [30940239402]


def test_get_destination():
    assert flight1.get_destination() == airport1


def test_get_origin():
    assert flight1.get_origin() == airport2


def test_flight_details2():
    assert flight1.flight_details() is not None


def test_get_passports2():
    flight1.add_passengers(passenger2, passenger1)
    assert flight1.get_passports() == [30940239402, '30932091039', 30940239402]
