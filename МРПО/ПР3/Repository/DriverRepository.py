from .ABCRepository import AbstractRepository
from ..Classes.Driver import Driver


# noinspection PyMissingConstructor
class DriverRepository(AbstractRepository):
    """Repository for managing drivers."""

    def remove(self, item):
        pass

    def get_all(self):
        pass

    def __init__(self):
        self.drivers = []

    def add(self, driver: Driver):
        self.drivers.append(driver)

    def get_by_id(self, driver_id: int) -> Driver:
        for driver in self.drivers:
            if driver.id == driver_id:
                return driver
        raise ValueError("Driver not found")
