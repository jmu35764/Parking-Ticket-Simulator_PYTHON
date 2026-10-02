"""Defines a Police Officer class for the parking ticket simulator"""
from parked_car import Parked_Car
from parking_meter import Parking_Meter
from parking_ticket import Parking_Ticket

class Police_Officer:
    """Represents a police officer who can inspect parked cars for violations"""

    def __init__(self, name: str, badge_number:str, car: Parked_Car, meter:Parking_Meter) -> None:
        self.name = name
        self.badge_number = badge_number
        self.car = car
        self.meter = meter
        #self.ticket = Parking_Ticket(0, car, meter, name, badge_number)

    def Inspect(self):
    """Checks the parked car for violations
    If there is no violatin, no ticket will
    be created
    """
        if self.car.min_parked > self.meter.min_purch:
            ticket = Parking_Ticket(0, self.car, self.meter, self.name, self.badge_number)
            ticket.SetFine()
            #report = ticket.report
            return ticket.report()
        else:
            return "\nThere is no violation" and None






