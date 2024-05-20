from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from МРПО.ПР6.Classes.Car import Car
from МРПО.ПР6.Classes.Client import Client
from МРПО.ПР6.Classes.Driver import Driver
from МРПО.ПР6.Classes.Location import Location
from МРПО.ПР6.Classes.id_mixin import IdMixin


class OrderStatus(Enum):
    """
    An Enum class representing the status of an order.
    """
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    WAITING = "Waiting"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class OrderCategory(Enum):
    """
    An Enum class representing the category of an order.
    """
    ECONOMIC = "Economic"
    COMFORT = "Comfort"
    BUSINESS = "Business"
    OTHER = "Other"


@dataclass
class Order(IdMixin):
    """Order for taxi"""
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
