from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from .Car import Car

if TYPE_CHECKING:
    from .Order import Order


@dataclass(repr=True)
class Driver:
    """Driver for order"""
    id: int
    cars: list[Car] = field(default_factory=list)
    orders: list['Order'] = field(default_factory=list)


if __name__ == '__main__':
    car1 = Car(year=2003, brand="Tesla", model="Model Y", color="Blue", plate_number="x003ку", id=0, seats=2)
    car2 = Car(year=2015, brand="Toyota", model="Camry", color="Black", plate_number="x003ру", id=1, seats=4)
    driver = Driver(cars=[car1, car2], id=0)
    print(driver)
    var = driver.orders
    print(var)
