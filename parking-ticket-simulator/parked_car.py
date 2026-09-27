class Parked_Car:
    def __init__(self, make: str = "", model: str = "", lic_num: str = "", min_parked: int = 0) -> None:
        self.make = make
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



    







        