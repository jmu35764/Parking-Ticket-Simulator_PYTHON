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

    def test_one_minute_over(self):
        car1 = Parked_Car("Toyota", "Red", "Camry", "ABC123", 61)
        meter1 = Parking_Meter(60)
        officer = Police_Officer("John Doe", "12345", car1, meter1)
        officer.Inspect()
        self.assertIsNotNone(officer.Inspect())
        self.assertIn("Fine: $25", officer.Inspect())
        #self.assertEqual(ticket.fine, 25)

    def test_one_hour_over(self):
        car2 = Parked_Car("Toyota", "Red", "Camry", "ABC123", 120)
        meter2 = Parking_Meter(60)
        officer2 = Police_Officer("John Doe", "12345", car2, meter2)
        officer2.Inspect()
        self.assertIsNotNone(officer2.Inspect())
        self.assertIn("Fine: $25", officer2.Inspect())

    def test_illegal_minutes(self):
        car1 = Parked_Car("Toyota", "Red", "Camry", "ABC123", 121)
        meter1 = Parking_Meter(60)
        officer = Police_Officer("John Doe", "12345", car1, meter1)
        officer.Inspect()
        self.assertIsNotNone(officer.Inspect())
        self.assertIn("Fine: $35", officer.Inspect())

        car2 = Parked_Car("Toyota", "Red", "Camry", "ABC123", 180)
        meter2 = Parking_Meter(60)
        officer2 = Police_Officer("John Doe", "12345", car2, meter2)
        officer2.Inspect()
        self.assertIsNotNone(officer2.Inspect())
        self.assertIn("Fine: $35", officer2 .Inspect())

        car3 = Parked_Car("Honda", "Blue", "Civic", "XYZ789", 181)
        meter3 = Parking_Meter(60)
        officer3 = Police_Officer("Jane Smith", "67890", car3, meter3)
        officer3.Inspect()
        self.assertIsNotNone(officer3.Inspect())
        self.assertIn("Fine: $45", officer3.Inspect())






