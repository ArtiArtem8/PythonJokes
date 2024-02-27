import dataclasses
from dataclasses import dataclass

from Driver import Driver

VALID_BRANDS: set[str] = {"Toyota", "Honda", "Ford", "Chevrolet", "Tesla"}
VALID_MODELS_BY_BRAND: dict[str, set[str]] = {
    "Toyota": {"Camry", "Corolla", "RAV4"},
    "Honda": {"Accord", "Civic", "CR-V"},
    "Ford": {"F-150", "Escape", "Focus"},
    "Chevrolet": {"Silverado", "Equinox", "Malibu"},
    "Tesla": {"Model S", "Model 3", "Model X", "Model Y"}
}


@dataclass
class Car:
    """Car for driver"""
    id: int
    plate_number: str
    owner: Driver | None
    seats: int
    brand: str
    model: str
    color: str
    year: int

    def __post_init__(self):
        if self.brand not in VALID_BRANDS:
            raise ValueError(f"Invalid make: {self.brand}")
        if self.model not in VALID_MODELS_BY_BRAND.get(self.brand, []):
            raise ValueError(f"Invalid model: {self.model}")
