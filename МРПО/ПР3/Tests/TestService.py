"""test"""
import unittest
from datetime import datetime
from unittest.mock import MagicMock

from МРПО.ПР3.Classes.Car import Car, CarInfo
from МРПО.ПР3.Classes.Client import Client
from МРПО.ПР3.Classes.Driver import Driver
from МРПО.ПР3.Classes.Location import Location
from МРПО.ПР3.Classes.Order import OrderCategory
from МРПО.ПР3.Repository.ABCRepository import AbstractRepository
from МРПО.ПР3.Service.Service import OrderService


class TestOrderService(unittest.TestCase):
    def setUp(self):
        self.order_repository = MagicMock(AbstractRepository)
        self.car_repository = MagicMock(AbstractRepository)
        self.driver_repository = MagicMock(AbstractRepository)
        self.client_repository = MagicMock(AbstractRepository)
        self.order_service = OrderService(self.order_repository, self.car_repository, self.driver_repository,
                                          self.client_repository)

    def test_create_order(self):
        car = Car(id=1, plate_number="ABC123", seats=4,
                  car_info=CarInfo(brand="Toyota", model="Corolla", color="Blue", year=2020))
        driver = Driver(id=1)  # Create a mock driver object
        client = Client(id=1, phone_number="1234567890")  # Create a mock client object
        start_location = Location(0, 0)  # Create a mock start location object
        current_driver_location = Location(0, 0)  # Create a mock current driver location object
        end_location = Location(1, 1)  # Create a mock end location object
        price = 10.0
        start_date = datetime.now()
        category = OrderCategory.ECONOMIC
        num_passengers = 3

        # Mock the behavior of repositories
        self.car_repository.get_by_id.return_value = car
        self.driver_repository.get_by_id.return_value = driver
        self.client_repository.get_by_id.return_value = client

        # Test create_order method
        order = self.order_service.create_order(car_id=1, driver_id=1, client_id=1,
                                                start_location=start_location,
                                                current_driver_location=current_driver_location,
                                                end_location=end_location,
                                                price=price,
                                                start_date=start_date,
                                                category=category,
                                                num_passengers=num_passengers)

        # Assertions
        self.assertEqual(order.car, car)
        self.assertEqual(order.driver, driver)
        self.assertEqual(order.client, client)
        self.assertEqual(order.start_location, start_location)
        self.assertEqual(order.current_driver_location, current_driver_location)
        self.assertEqual(order.end_location, end_location)
        self.assertEqual(order.price, price)
        self.assertEqual(order.start_date, start_date)
        self.assertEqual(order.category, category)


if __name__ == '__main__':
    unittest.main()
