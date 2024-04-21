from dataclasses import dataclass, field, asdict
from typing import TYPE_CHECKING

from МРПО.ПР4.Classes.Car import Car, CarInfo
from МРПО.ПР4.Classes.id_mixin import IdMixin

if TYPE_CHECKING:
    from .Order import Order


@dataclass(repr=True)
class Driver(IdMixin):
    """Driver for order"""
    cars: list[Car] = field(default_factory=list)
    orders: list['Order'] = field(default_factory=list)


if __name__ == '__main__':
    car1 = Car(owner=None, plate_number="X003KY", id=1, seats=2,
               car_info=CarInfo(year=2003, brand="Tesla", model="Model Y", color="Blue"))
    car2 = Car(owner=None, plate_number="X003PY", id=2, seats=4,
               car_info=CarInfo(year=2015, brand="Toyota", model="Camry", color="Black"))
    driver = Driver(cars=[car1, car2], id=1)
    print(asdict(driver))
    var = driver.orders
    print(var)
