from Car import Car
from dataclasses import dataclass

from Order import Order


@dataclass(repr=True)
class Driver:
    """Driver for order"""
    id: int
    cars: list[Car]
    orders = list[Order]


if __name__ == '__main__':
    car1 = Car(year=2003, brand="Ford", model="Model T", color="Blue", plate_number="x003ку", owner=None)
    car2 = Car(year=2015, brand="Toyota", model="Camry", color="Black", plate_number="x003ру", owner=None)
    driver = Driver(cars=[car1, car2])
    print(driver)
