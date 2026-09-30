from parked_car import Parked_Car
from parking_meter import Parking_Meter
from parking_ticket import Parking_Ticket
from police_officer import Police_Officer
import math

def main():

    car1 = Parked_Car("Toyota", "Red", "Camry", "ABC123", 121)
    meter1 = Parking_Meter(60)
    Officer1 = Police_Officer("John Doe", "12345", car1, meter1)
    print(Officer1.Inspect())



if __name__ == "__main__":
    main()