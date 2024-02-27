from dataclasses import dataclass

from Driver import Driver


@dataclass
class Car:
    """Car for driver"""
    plate_number: str
    owner: Driver | None
    brand: str
    model: str
    color: str
    year: int



