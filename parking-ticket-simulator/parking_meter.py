"""Define the Parking_Meter class for the Parking Ticket Simulator"""
class Parking_Meter():

    """Automatically sets the value for minutes purchased to zero"""
    def __init__ (self, min_purch: int = 0) -> None:
        self.min_purch = min_purch
    
    """For the minutes purchased property"""
    @property
    def min_purch(self):
        return self._min_purch

    """Ensures the minutes purchased is a valid integer"""
    @min_purch.setter
    def min_purch(self, value):
        if not isinstance(value, int):
            raise TypeError("Minutes purchased must be an integer")
        if value < 0:
            raise ValueError("Minutes purchased cannot be negative")
        self._min_purch = value

    """Prints the parking meter's information"""
    def list(self):
        return f"Minutes Purchased: {self.min_purch}"




