import xml.etree.ElementTree as ET
from dataclasses import asdict
from typing import TypeVar, Generic, List, Optional

from МРПО.ПР4.XML.generate_data import generate_test_data

T = TypeVar('T')


class XMLRepository(Generic[T]):
    def __init__(self, file_path: str, root_tag: str, item_tag: str):
        self.file_path = file_path
        self.root_tag = root_tag
        self.item_tag = item_tag

    def _write_to_xml(self, data: List[T]):
        root = ET.Element(self.root_tag)
        for item in data:
            print(data)
            item_element = ET.Element(self.item_tag)
            for key, value in item.items():
                field_element = ET.Element(key)
                field_element.text = str(value)
                item_element.append(field_element)
            root.append(item_element)
        tree = ET.ElementTree(root)
        tree.write(self.file_path)

    def _read_from_xml(self) -> List[T]:
        try:
            tree = ET.parse(self.file_path)
            root = tree.getroot()
            items = []
            for item_element in root.findall(self.item_tag):
                item_dict = {}
                for field_element in item_element:
                    item_dict[field_element.tag] = field_element.text
                items.append(item_dict)
            return items
        except (ET.ParseError, FileNotFoundError):
            return []

    def add(self, item: T):
        data = self._read_from_xml()
        data.append(asdict(item))
        self._write_to_xml(data)

    def update(self, item: T):
        data = self._read_from_xml()
        for i, data_item in enumerate(data):
            if data_item["id"] == item.id:
                data[i] = item.__dict__
                break
        self._write_to_xml(data)

    def get(self, item_id: int) -> Optional[T]:
        data = self._read_from_xml()
        for item_dict in data:
            if int(item_dict.get("id")) == item_id:
                return item_dict
        return None

    def delete(self, item_id: int):
        data = self._read_from_xml()
        for i, item_dict in enumerate(data):
            if int(item_dict.get("id")) == item_id:
                del data[i]
                break
        self._write_to_xml(data)


if __name__ == '__main__':
    from МРПО.ПР4.Classes import Driver, Client, Order, Car
    from typing import List

    num_drivers = 3
    num_clients = 2
    num_cars_per_driver = 2
    num_orders_per_client = 3

    drivers, clients, orders, cars = generate_test_data(num_drivers, num_clients, num_cars_per_driver,
                                                        num_orders_per_client)

    # Assuming you have instances of drivers, clients, orders, and cars
    drivers: List[Driver] = drivers  # List of Driver instances
    clients: List[Client] = cars     # List of Client instances
    orders: List[Order] = clients    # List of Order instances
    cars: List[Car] = orders         # List of Car instances

    # Initialize XMLRepository instances for each entity type
    driver_repository = XMLRepository(file_path="drivers.xml", root_tag="drivers", item_tag="driver")
    client_repository = XMLRepository(file_path="clients.xml", root_tag="clients", item_tag="client")
    order_repository = XMLRepository(file_path="orders.xml", root_tag="orders", item_tag="order")
    car_repository = XMLRepository(file_path="cars.xml", root_tag="cars", item_tag="car")

    # Save data for drivers
    for driver in drivers:
        driver_repository.add(driver)

    # Save data for clients
    for client in clients:
        client_repository.add(client)

    # Save data for orders
    for order in orders:
        order_repository.add(order)

    # Save data for cars
    for car in cars:
        car_repository.add(car)
