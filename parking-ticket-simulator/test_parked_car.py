import unittest
from parked_car import Parked_Car

class Test_Parked_Car(unittest.TestCase):

    def test_min_parked_output(self):
        #Arrange
        car = Parked_Car()

        #Act
        car.min_parked = 60

        #Assert
        self.assertEqual(car.min_parked, 60)
        self.assertIsInstance(car.min_parked, int)

    def test_invalid_min_parked(self):
    
        #Arrange
        car = Parked_Car()

        #Act and Assert
        with self.assertRaises(ValueError):
            car.min_parked = -10
        with self.assertRaises(TypeError):
            car.min_parked = "sixty"

if __name__ == '__main__':
    unittest.main()




