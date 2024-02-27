from dataclasses import dataclass
from datetime import datetime

from Car import Car
from Client import Client
from Location import Location


@dataclass
class Order:
    """Order for taxi class"""
    car: Car
    client: Client
    start_location: Location
    end_location: Location
    price: float
    start_date: datetime
    category: str
