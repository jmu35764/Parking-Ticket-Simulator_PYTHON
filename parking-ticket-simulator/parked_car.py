class Parked_Car:
    def __init__(self, make: str = "make", color: str = "color", model: str = "model", lic_num: str = "license number", min_parked: int = 0) -> None:
        self.make = make
        self.color = color
        self.model = model
        self.lic_num = lic_num
        self.min_parked = min_parked


    @property
    def min_parked(self):
        return self._min_parked

    @min_parked.setter
    def min_parked(self, value):
        if not isinstance(value, int):
            raise TypeError("Minutes parked must be an integer")
        if value < 0:
            raise ValueError("Minutes parked cannot be negative")
        self._min_parked = value

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        if not isinstance(value, str):
            raise TypeError("Make must be a string")
        if not value:
            raise ValueError("Make cannot be empty")
#        raise_error(value)
        self._make = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if not isinstance(value, str):
            raise TypeError("Color must be a string")
        if not value:
            raise ValueError("Color cannot be empty")
        self._color = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not isinstance(value, str):
            raise TypeError("Model must be a string")
        if not value:
            raise ValueError("Model cannot be empty")
        self._model = value

    @property
    def lic_num(self):
        return self._lic_num

    @lic_num.setter
    def lic_num(self, value):
        if not isinstance(value, str):
            raise TypeError("License number must be a string")
        if not value:
            raise ValueError("License number cannot be empty")
        self._lic_num = value

#    def raise_error(self, value):
#       if not isinstance(value, str):
#            raise TypeError("Make must be a string")
#        if not value:
#            raise ValueError("Make cannot be empty")







        