import unittest

from police_officer import Police_Officer


class test_police_officer(unittest.TestCase):
    def test_no_ticket(self):
        car1 = Parked_Car("Toyota", "Red", "Camry", "ABC123", 30)
        meter1 = Parking_Meter(60)
        officer = Police_Officer("John Doe", "12345", car1, meter1)
        self.assertIsNone(officer.Inspect())






