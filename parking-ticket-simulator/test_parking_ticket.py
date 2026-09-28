import unittest
from parking_ticket import Parking_Ticket
from parked_car import Parked_Car


class test_parking_ticket(unittest.TestCase):
    
    def test_set_fine(self):
        # Create a parked car with 120 minutes parked
        car = Parked_Car("ABC123", "Toyota", "Red", 120)
        # Create a parking meter with 60 minutes purchased
        meter = Parking_Meter(60)
        # Create a parking ticket
        ticket = Parking_Ticket(0, car, meter)
        # Set the fine
        ticket.SetFine()
        # Check if the fine is calculated correctly
        self.assertEqual(ticket.fine, 35)