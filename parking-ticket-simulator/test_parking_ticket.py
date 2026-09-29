import unittest
from parking_meter import Parking_Meter
from parked_car import Parked_Car
from parking_ticket import Parking_Ticket


class test_parking_ticket(unittest.TestCase):
    
    def test_set_fine(self):
        # Arrange
        car1 = Parked_Car("Toyota", "Camry", "Red", "ABC123", 121)
        meter1 = Parking_Meter(60)
        ticket = Parking_Ticket(0, car1, meter1)

        # Act
        ticket.SetFine()

        # Assert
        self.assertEqual(ticket.fine, 35)

    def test_over_by_one_min(self):
        #Arrange
        car1 = Parked_Car("Honda", "Civic", "Blue", "XYZ789", 61)
        meter1 = Parking_Meter(60)
        ticket = Parking_Ticket(0, car1, meter1)

        #Act
        ticket.SetFine()

        # Assert
        self.assertEqual(ticket.fine, 25)


if __name__ == '__main__':
    unittest.main()