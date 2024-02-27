from ..Classes.Driver import Driver


class DriverRepository:
    """Repository for managing drivers."""
    def __init__(self):
        self.drivers = []

    def add_driver(self, driver: Driver):
        self.drivers.append(driver)

    def get_driver_by_id(self, driver_id: int) -> Driver:
        for driver in self.drivers:
            if driver.id == driver_id:
                return driver
        raise ValueError("Driver not found")