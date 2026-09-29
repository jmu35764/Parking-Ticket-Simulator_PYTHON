
from parked_car import Parked_Car
from parking_meter import Parking_Meter
import math


class Parking_Ticket:
    def __init__(self, fine: int = 0, car: Parked_Car = None, meter: Parking_Meter = None) -> None:
        #self.fine = self.SetFine()
        self.car = car
        self.meter = meter
        self.fine = self.SetFine()

    def SetFine(self) -> int:
        if self.car is None or self.meter is None:
            return None

        over = self.car.min_parked - self.meter.min_purch
        if over <= 0:
            self.fine = 0
        elif over > 0 and over <= 60:
            self.fine = 25
        else:
            self.fine = 25 + math.ceil((over-60) / 60) * 10
        return self.fine

    def report(self):
        return self.car.list() + self.meter.list() + f"\nFine: ${self.fine}"

    





