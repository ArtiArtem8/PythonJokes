from dataclasses import dataclass, field

from .ABCRepository import AbstractRepository
from ..Classes.Order import Order


@dataclass
class OrderRepository(AbstractRepository):
    """Repository for managing orders."""
    orders: list[Order] = field(default_factory=list)

    def add(self, order: Order):
        self.orders.append(order)

    def get_by_id(self, order_id: int) -> Order:
        for order in self.orders:
            if order.id == order_id:
                return order
        raise ValueError("Order not found")

    def get_all(self):
        pass

    def remove(self, item):
        pass
