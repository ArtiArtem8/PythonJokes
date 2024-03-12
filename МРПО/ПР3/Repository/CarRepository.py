from .ABCRepository import AbstractRepository
from ..Classes.Car import Car


# noinspection PyMissingConstructor
class CarRepository(AbstractRepository):
    """Repository for managing cars."""

    def remove(self, item):
        pass

    def get_all(self):
        pass

    def __init__(self):
        self.cars = []

    def add(self, car: Car):
        self.cars.append(car)

    def get_by_id(self, car_id: int) -> Car:
        for car in self.cars:
            if car.id == car_id:
                return car
        raise ValueError("Car not found")
