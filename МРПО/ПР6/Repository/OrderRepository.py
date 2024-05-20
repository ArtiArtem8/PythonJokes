from dataclasses import dataclass, field

from ..Repository.ABCRepository import AbstractRepository

from МРПО.ПР6.Classes.Order import Order


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
        return self.orders

    def remove(self, item):
        self.orders.remove(item)

    def update(self, order):
        pass

