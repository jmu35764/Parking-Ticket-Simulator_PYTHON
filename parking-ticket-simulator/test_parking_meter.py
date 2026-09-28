import unittest
from parking_meter import Parking_Meter

class test_parking_meter(unittest.TestCase):

    def test_min_purch(self):
        #Arrange
        meter = Parking_Meter()

        #Act
        meter.min_purch = 30

        #Assert
        self.assertEqual(meter.min_purch, 30)
        self.assertIsInstance(meter.min_purch, int)
