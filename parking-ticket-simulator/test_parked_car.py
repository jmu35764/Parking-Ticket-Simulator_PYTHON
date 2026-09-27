import unittest
from parked_car import Parked_Car

class Test_Parked_Car(unittest.TestCase):
    def test_min_parked(self):
        #Arrange
        car = Parked_Car()

        #Act
        car.min_parked = 60

        #Assert
        self.assertEqual(car.min_parked, 60)
        self.assertIsInstance(car.min_parked, int)

if __name__ == '__main__':
    unittest.main()




