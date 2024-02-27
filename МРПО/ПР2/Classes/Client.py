from dataclasses import dataclass

from Order import Order


@dataclass
class Client:
    """Client for order"""
    id: int
    phone_number: str
    orders = list[Order]
