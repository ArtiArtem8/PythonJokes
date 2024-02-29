from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from Car import Car
from Client import Client
from Location import Location
from Driver import Driver


class OrderStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    WAITING = "Waiting"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class OrderCategory(Enum):
    ECONOMIC = "Economic"
    COMFORT = "Comfort"
    BUSINESS = "Business"
    OTHER = "Other"


@dataclass
class Order:
    """Order for taxi"""
    id: int
    car: Car
    driver: Driver
    client: Client
    start_location: Location
    current_driver_location: Location
    end_location: Location
    price: float
    start_date: datetime
    category: OrderCategory = OrderCategory.ECONOMIC
    status: OrderStatus = OrderStatus.PENDING
