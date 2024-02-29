from ..Classes.Order import Order


class OrderRepository:
    """Repository for managing orders."""

    def __init__(self):
        self.orders = []

    def add_order(self, order: Order):
        self.orders.append(order)

    def get_order_by_id(self, order_id: int) -> Order:
        for order in self.orders:
            if order.id == order_id:
                return order
        raise ValueError("Order not found")
