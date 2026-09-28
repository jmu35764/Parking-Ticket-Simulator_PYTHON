import unittest
from parked_car import Parked_Car

class Test_Parked_Car(unittest.TestCase):

    def test_default_constructor(self):
        #Arrange
        car = Parked_Car()

        #Act and Assert
        self.assertEqual(car.make, "make")
        self.assertEqual(car.color, "color")
        self.assertEqual(car.model, "model")
        self.assertEqual(car.lic_num, "license number") 
        self.assertEqual(car.min_parked, 0) 
    
    def test_constructor(self):
        #Arrange
        car = Parked_Car("Ford", "Black", "Fusion", "123ABC", 0)

        #Act and Assert
        self.assertEqual(car.make, "Ford")
        self.assertEqual(car.color, "Black")
        self.assertEqual(car.model, "Fusion")
        self.assertEqual(car.lic_num, "123ABC")
        self.assertEqual(car.min_parked, 0)

    def test_empty_string_constructor(self):
        #Arrange
        car = Parked_Car("", "", "", "", 0)
        #Act and Assert
        self.assertEqual(car.make, "")
        self.assertEqual(car.color, "")
        self.assertEqual(car.model, "")
        self.assertEqual(car.lic_num, "")
        self.assertEqual(car.min_parked, 0)
    
    def test_min_parked_output(self):
        #Arrange
        car = Parked_Car()

        #Act
        car.min_parked = 60

        #Assert
        self.assertEqual(car.min_parked, 60)
        self.assertIsInstance(car.min_parked, int)

    def test_neg_min_parked(self):
    
        #Arrange
        car1 = Parked_Car()
        #car2 = Parked_Car()

        #Act and Assert
        car1.min_parked = -10
        #car2.min_parked = "sixty"

        """with self.assertRaises(ValueError):
            car1.min_parked = -10
        with self.assertRaises(TypeError):
            car1.min_parked = "sixty" """

    def test_string_min_parked(self):
        #Arrange
        car = Parked_Car()
        #Act and Assert
        with self.assertRaises(TypeError):
            car.min_parked = "sixty"    

if __name__ == '__main__':
    unittest.main()




