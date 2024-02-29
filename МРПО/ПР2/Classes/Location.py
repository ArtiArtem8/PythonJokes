from dataclasses import dataclass


@dataclass(frozen=True)
class Location:
    """Location for order"""
    latitude: float
    longitude: float
