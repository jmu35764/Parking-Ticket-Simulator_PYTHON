
from parked_car import Parked_Car
from parking_meter import Parking_Meter
#from police_officer import Police_Officer
import math


class Parking_Ticket:
    def __init__(self, fine: int = 0, car: Parked_Car = None, meter: Parking_Meter = None, officer_name: str = None, off_num: str = None) -> None:
        #self.fine = self.SetFine()
        self.car = car
        self.meter = meter
        self.fine = self.SetFine()
        self.officer_name = officer_name
        self.off_num = off_num

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
        return f"Officer: {self.officer_name}\n Badge Number: {self.off_num}\n{self.car.list()}\n{self.meter.list()}\nFine: ${self.fine}"





