from dataclasses import dataclass, field

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Order import Order


@dataclass(frozen=True)
class Client:
    """Client for order"""
    id: int
    phone_number: str
    orders: list['Order'] = field(default_factory=list)
