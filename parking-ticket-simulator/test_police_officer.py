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
        #self.assertEqual(ticket.fine, 25)

    def test_illegal_minutes(self):
        car1 = Parked_Car("Toyota", "Red", "Camry", "ABC123", 121)
        meter1 = Parking_Meter(60)
        officer = Police_Officer("John Doe", "12345", car1, meter1)
        officer.Inspect()
        self.assertIsInstance(ticket, Parking_Ticket)
        self.assertEqual(ticket.fine, 35)

        car2 = Parked_Car("Honda", "Blue", "Civic", "XYZ789", 181)
        meter2 = Parking_Meter(60)
        officer2 = Police_Officer("Jane Smith", "67890", car2, meter2)
        ticket2 = officer2.Inspect()
        self.assertIsInstance(ticket2, Parking_Ticket)
        self.assertEqual(ticket2.fine, 45)






