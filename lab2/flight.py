from __future__ import annotations
from typing import Union


class Seat:
    name: str
    type: str = 'economy'

    def __init__(self, name, type) -> None:
        self.name = name
        if type in ['economy', 'business']:
            self.type = type


class Passenger:
    booking_id: Union[str, None]

    def __init__(self) -> None:
        self.booking_id = None

    # IF WE PUT BOOK IN PASSENGER
    def book(self, flight: Flight, type: str) -> bool:
        """
        A passenger books a certain type of seat (business or economy),
        returns true on success, false on failure. 
        """
        # Book the seat
        if flight.book_seat(type):
            self.booking_id = 'fasfsdafasfas'  # assign some random booking id
            return True
        return False


class Flight:
    occupied_economy: int
    occupied_business: int
    capacity_economy: int
    capacity_business: int

    def __init__(self, capacity_economy, capacity_business) -> None:
        self.capacity_economy = capacity_economy
        self.capacity_business = capacity_business
        self.occupied_economy = 0
        self.occupied_business = 0

    def get_filled_all(self) -> float:
        """
        Returns the percentage of all seats which are filled.
        """
        return (self.occupied_business + self.occupied_economy) / (self.capacity_business + self.capacity_economy)

    def get_filled_economy(self) -> float:
        """
        Returns the percentage of economy seats which are filled.
        """
        return self.occupied_economy / self.capacity_economy

    def get_filled_business(self) -> float:
        """
        Returns the percentage of business seats which are filled.
        """
        return self.occupied_business / self.capacity_business

    def book_seat(self, type: str) -> bool:
        # Check if we have space
        if type == 'economy' and self.occupied_economy < self.capacity_economy:
            self.occupied_economy += 1  # book the seat
            return True

        if type == 'business' and self.occupied_business < self.capacity_business:
            self.occupied_business += 1  # book the seat
            return True

        return False

    # IF WE PUT BOOK IN FLIGHT
    def book(self, passenger: Passenger, type: str) -> bool:
        """
        A passenger books a certain type of seat (business or economy),
        returns true on success, false on failure. 
        """
        # Book the seat
        if self.book_seat(type):
            passenger.booking_id = 'fassfafasfsa'  # assign some random booking id
            return True
        return False
