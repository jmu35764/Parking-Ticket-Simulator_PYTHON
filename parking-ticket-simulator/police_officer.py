from parked_car import Parked_Car
from parking_meter import Parking_Meter
from parking_ticket import Parking_Ticket

class Police_Officer:
    
    def __init__(self, name: str, badge_number:str, car: Parked_Car, meter:Parking_Meter) -> None:
        self.name = name
        self.badge_number = badge_number
        self.car = car
        self.meter = meter
        #self.ticket = Parking_Ticket(0, car, meter, name, badge_number)

    def Inspect(self):
        if self.car.min_parked > self.meter.min_purch:
            ticket = Parking_Ticket(0, self.car, self.meter, self.name, self.badge_number)
            ticket.SetFine()
            #report = ticket.report
            return ticket.report()
        else:
            return "There is no violation"

    def list(self):
        return f"\nOfficer Name: {self.name}\nBadge Number: {self.badge_number}"





