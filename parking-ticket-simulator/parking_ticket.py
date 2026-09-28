from parked_car import Parked_Car
from parking_meter import Parking_Meter

class Parking_Ticket():
    
    def __init__ (self, fine: int = 0, car: Parked_Car = None, meter: Parking_Meter = None) -> None:
        self.fine = fine
        self.car = car
        self.meter = meter

    






