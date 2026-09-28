from parked_car import Parked_Car
from parking_meter import Parking_Meter
import math

class Parking_Ticket():
    
    def __init__ (self, fine: int = 0, car: Parked_Car = None, meter: Parking_Meter = None) -> None:
        self.fine = SetFine()
        self.car = car
        self.meter = meter

   def SetFine(self):
       if self.car.min_parked > self.meter.min_purch:
           self.fine = 25 + math.ceil((self.car.min_parked - self.meter.min_purch-60) / 60) * 10
       return self.fine





