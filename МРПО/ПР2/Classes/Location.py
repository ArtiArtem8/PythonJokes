from dataclasses import dataclass


@dataclass
class Location:
    """Location for order"""
    latitude: float
    longitude: float
