import unittest
from parking_meter import Parking_Meter
from parked_car import Parked_Car
from parking_ticket import Parking_Ticket


class test_parking_ticket(unittest.TestCase):
    
    def test_set_fine(self):
        # Arrange
        car1 = Parked_Car("Toyota", "Red", "Camry", "ABC123", 121)
        meter1 = Parking_Meter(60)
        ticket = Parking_Ticket(0, car1, meter1)

        # Act
        ticket.SetFine()

        # Assert
        self.assertEqual(ticket.fine, 35)

    def test_over_by_one_min(self):
        #Arrange
        car1 = Parked_Car("Honda", "Blue", "Civic", "XYZ789", 61)
        meter1 = Parking_Meter(60)
        ticket = Parking_Ticket(0, car1, meter1)

        #Act
        ticket.SetFine()

        # Assert
        self.assertEqual(ticket.fine, 25)

    def test_less_than_or_equal_to_meter(self):
        #Arrange
        car1 = Parked_Car("Ford", "Black", "Focus", "LMN456", 30)
        meter1 = Parking_Meter(60)
        ticket = Parking_Ticket(0, car1, meter1)
        #Act
        ticket.SetFine()
        #Assert
        self.assertEqual(ticket.fine, 0)

    def test_create_report(self):
        # Arrange
        car1 = Parked_Car("Toyota", "Red", "Camry", "ABC123", 121)
        meter1 = Parking_Meter(60)
        ticket = Parking_Ticket(0, car1, meter1)
        ticket.SetFine()

        # Act
        report = ticket.report()

        # Assert
        self.assertIn("Make: Toyota", report)
        self.assertIn("Color: Red", report)
        self.assertIn("Model: Camry", report)
        self.assertIn("License Number: ABC123", report)
        self.assertIn("Minutes Parked: 121", report)
        self.assertIn("Minutes Purchased: 60", report)
        self.assertIn("Fine: $35", report)

if __name__ == '__main__':
    unittest.main()