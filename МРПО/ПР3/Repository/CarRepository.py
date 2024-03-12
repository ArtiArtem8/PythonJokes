from dataclasses import field, dataclass

from .ABCRepository import AbstractRepository
from ..Classes.Car import Car


@dataclass
class CarRepository(AbstractRepository):
    """Repository for managing cars."""
    cars: list[Car] = field(default_factory=list)

    def remove(self, item):
        pass

    def get_all(self):
        pass

    def add(self, car: Car):
        self.cars.append(car)

    def get_by_id(self, car_id: int) -> Car:
        for car in self.cars:
            if car.id == car_id:
                return car
        raise ValueError("Car not found")
