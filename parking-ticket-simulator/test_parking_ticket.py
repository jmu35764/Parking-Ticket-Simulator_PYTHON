import unittest
from parking_meter import Parking_Meter
from parked_car import Parked_Car
from parking_ticket import Parking_Ticket


class test_parking_ticket(unittest.TestCase):
    
    def test_set_fine(self):
        # Arrange
        car = Parked_Car("ABC123", "Toyota", "Red", 120)
        meter = Parking_Meter(60)
        ticket = Parking_Ticket(0, car, meter)

        # Act
        ticket.SetFine()

        # Assert
        self.assertEqual(ticket.fine, 35)

if __name__ == '__main__':
    unittest.main()