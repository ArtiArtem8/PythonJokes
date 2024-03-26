import re
from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from МРПО.ПР3.Classes.id_mixin import IdMixin

if TYPE_CHECKING:
    from .Driver import Driver

VALID_MODELS_BY_BRAND: dict[str, set[str]] = {
    "Toyota": {"Camry", "Corolla", "RAV4"},
    "Honda": {"Accord", "Civic", "CR-V"},
    "Ford": {"F-150", "Escape", "Focus"},
    "Chevrolet": {"Silverado", "Equinox", "Malibu"},
    "Tesla": {"Model S", "Model 3", "Model X", "Model Y"}
}

class CarInfo:
    pass

@dataclass
class CarInfo:
    """Car information model for car in database"""
    brand: str
    model: str
    color: str
    year: int

    def __post_init__(self):
        if self.brand not in VALID_MODELS_BY_BRAND:
            raise ValueError(f"Invalid brand: {self.brand}")
        if self.model not in VALID_MODELS_BY_BRAND.get(self.brand, []):
            raise ValueError(f"Invalid model: {self.model}")


@dataclass
class Car(IdMixin):
    """Car Model for driver in database"""
    plate_number: str
    seats: int
    car_info: CarInfo
    owner: Optional['Driver'] = None

    def __post_init__(self):
        super().__post_init__()
        if not re.match(r'^[A-Z0-9А-Я]{6}$', self.plate_number):
            raise ValueError("Invalid plate number format")
        if self.seats <= 0:
            raise ValueError("Invalid number of seats: seats must be a positive integer.")


if __name__ == '__main__':
    car = Car(id=1, plate_number="ABC123", seats=4, car_info=CarInfo("Toyota", "Corolla", "Red", 2020))
    print(car)
