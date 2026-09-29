class Parking_Meter():

    def __init__ (self, min_purch: int = 0) -> None:
        self.min_purch = min_purch

    @property
    def min_purch(self):
        return self._min_purch

    @min_purch.setter
    def min_purch(self, value):
        if not isinstance(value, int):
            raise TypeError("Minutes purchased must be an integer")
        if value < 0:
            raise ValueError("Minutes purchased cannot be negative")
        self._min_purch = value

    def list(self):
        return f"\nMinutes Purchased: {self.min_purch}"




