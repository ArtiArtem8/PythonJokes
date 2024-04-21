from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from МРПО.ПР4.Classes.id_mixin import IdMixin

if TYPE_CHECKING:
    from .Order import Order


@dataclass
class Client(IdMixin):
    """Client for order"""
    phone_number: str
    orders: list['Order'] = field(default_factory=list)


if __name__ == '__main__':
    client = Client(id=1, phone_number="1234567890")
    print(client)
    client.orders.append(1)
    print(client)
