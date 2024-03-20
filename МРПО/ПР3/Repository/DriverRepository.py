from dataclasses import field, dataclass

from ..Repository.ABCRepository import AbstractRepository

from ..Classes.Driver import Driver


@dataclass
class DriverRepository(AbstractRepository):
    """Repository for managing drivers."""
    drivers: list[Driver] = field(default_factory=list)

    def remove(self, item):
        pass

    def get_all(self):
        pass

    def add(self, driver: Driver):
        self.drivers.append(driver)

    def get_by_id(self, driver_id: int) -> Driver:
        for driver in self.drivers:
            if driver.id == driver_id:
                return driver
        raise ValueError("Driver not found")
