from parked_car import Parked_Car
from parking_meter import Parking_Meter
from parking_ticket import Parking_Ticket

class Police_Officer:
    
    def __init__(self, name: str, badge_number:str, car: Parked_Car, meter:Parking_Meter) -> None:
        self.name = name
        self.badge_number = badge_number
        self.car = car
        self.meter = meter
        self.ticket = Parking_Ticket(0, car, meter)

    def Inspect(self):
        if self.car.min_parked > self.meter.min_purch:
            return self.ticket
        else:
            return None





