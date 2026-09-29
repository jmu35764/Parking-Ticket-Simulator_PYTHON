import unittest
from police_officer import Police_Officer
from parking_meter import Parking_Meter
from parked_car import Parked_Car
from parking_ticket import Parking_Ticket

class test_police_officer(unittest.TestCase):
    
    def test_no_ticket(self):
        car1 = Parked_Car("Toyota", "Red", "Camry", "ABC123", 30)
        meter1 = Parking_Meter(60)
        officer = Police_Officer("John Doe", "12345", car1, meter1)
        self.assertIsNone(officer.Inspect())

    def test_parked_equals_meter(self):
        car1 = Parked_Car("Toyota", "Red", "Camry", "ABC123", 60)
        meter1 = Parking_Meter(60)
        officer = Police_Officer("John Doe", "12345", car1, meter1)
        self.assertIsNone(officer.Inspect())






