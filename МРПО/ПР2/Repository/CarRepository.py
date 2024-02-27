from ..Classes.Car import Car


class CarRepository:
    """Repository for managing cars."""

    def __init__(self):
        self.cars = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def get_car_by_id(self, car_id: int) -> Car:
        for car in self.cars:
            if car.id == car_id:
                return car
        raise ValueError("Car not found")
