""" Define the Parked_Car class for the parking ticket simulator """

class Parked_Car:
    """Automatically sets the values for the parked car class to simple values to recognize when no data has been entered """
    def __init__(self, make: str = "make", color: str = "color", model: str = "model", lic_num: str = "license number", min_parked: int = 0) -> None:
        self.make = make
        self.color = color
        self.model = model
        self.lic_num = lic_num
        self.min_parked = min_parked


    @property
    """For the minutes parked property"""
    def min_parked(self):
        return self._min_parked

    @min_parked.setter
    """Makes sure the minutes parked is a valid integer"""
    def min_parked(self, value):
        if not isinstance(value, int):
            raise TypeError("Minutes parked must be an integer")
        if value < 0:
            raise ValueError("Minutes parked cannot be negative")
        self._min_parked = value

    @property
    """For the make property"""
    def make(self):
        return self._make

    @make.setter
    """Makes sure the make is a valid string"""
    def make(self, value):
        if not isinstance(value, str):
            raise TypeError("Make must be a string")
        if not value:
            raise ValueError("Make cannot be empty")
        self._make = value

    @property
    """For the color property"""
    def color(self):
        return self._color

    @color.setter
    """Makes sure the color is a valid string"""
    def color(self, value):
        if not isinstance(value, str):
            raise TypeError("Color must be a string")
        if not value:
            raise ValueError("Color cannot be empty")
        self._color = value

    @property
    """For the model property"""
    def model(self):
        return self._model

    @model.setter
    """Makes sure the model is a valid string"""
    def model(self, value):
        if not isinstance(value, str):
            raise TypeError("Model must be a string")
        if not value:
            raise ValueError("Model cannot be empty")
        self._model = value

    @property
    """For the license number property"""
    def lic_num(self):
        return self._lic_num

    @lic_num.setter
    """Makes sure the license number is a valid string

    Args: 
    value (str): The license number to setvalue to

    Returns:
    None

    Raises:
    TypeError : If the value is not a string
    ValueError: If the value is an empty string
    """
    def lic_num(self, value):
        if not isinstance(value, str):
            raise TypeError("License number must be a string")
        if not value:
            raise ValueError("License number cannot be empty")
        self._lic_num = value

    """Prints all of the car's information"""
    def list(self):
        return f"Make: {self.make}\nColor: {self.color}\nModel: {self.model}\nLicense Number: {self.lic_num}\nMinutes Parked: {self.min_parked}"

      