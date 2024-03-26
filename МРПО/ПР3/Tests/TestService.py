"""test"""
import unittest
from datetime import datetime
from unittest.mock import MagicMock

from МРПО.ПР3.Classes.Car import Car, CarInfo
from МРПО.ПР3.Classes.Client import Client
from МРПО.ПР3.Classes.Driver import Driver
from МРПО.ПР3.Classes.Location import Location
from МРПО.ПР3.Classes.Order import OrderCategory, Order, OrderStatus
from МРПО.ПР3.Repository.ABCRepository import AbstractRepository
from МРПО.ПР3.Service.Service import OrderService


class TestOrderService(unittest.TestCase):
    def setUp(self):
        self.order_service = OrderService()

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

        # Test create_order method
        order = self.order_service.create_order(car, driver, client,
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

    #  Trying to update the order's start location with an invalid location
    def test_update_start_location_invalid(self):
        order = Order(id=1, car=Car(id=1, plate_number="ABC123", seats=4,
                                    car_info=CarInfo(brand="Toyota", model="Corolla", color="Blue", year=2020)),
                      driver=Driver(id=1),
                      client=Client(id=1, phone_number="1234567890"),
                      start_location=Location(0, 0),
                      current_driver_location=Location(0, 0),
                      end_location=Location(1, 1),
                      price=10.0,
                      start_date=datetime.now(),
                      category=OrderCategory.ECONOMIC,
                      status=OrderStatus.PENDING)

        # Mock the behavior of repositories
        self.order_repository.get_by_id = MagicMock(return_value=order)

        # Test update_start_location method with invalid location
        with self.assertRaises(ValueError):
            self.order_service.update_start_location(order_id=1, new_start_location=None)

    #  Updating the order's start location
    def test_update_start_location(self):
        order = Order(id=1, car=Car(id=1, plate_number="ABC123", seats=4,
                                    car_info=CarInfo(brand="Toyota", model="Corolla", color="Blue", year=2020)),
                      driver=Driver(id=1),
                      client=Client(id=1, phone_number="1234567890"),
                      start_location=Location(0, 0),
                      current_driver_location=Location(0, 0),
                      end_location=Location(1, 1),
                      price=10.0,
                      start_date=datetime.now(),
                      category=OrderCategory.ECONOMIC,
                      status=OrderStatus.PENDING)

        # Mock the behavior of repositories
        self.order_repository.get_by_id = MagicMock(return_value=order)
        self.order_repository.update = MagicMock(return_value=order)

        # Test update_start_location method
        updated_order = self.order_service.update_start_location(order_id=1, new_start_location=Location(2, 2))

        # Assertions
        self.assertEqual(updated_order.start_location, Location(2, 2))

    #  Test the get_order_by_id method of the OrderService class
    def test_get_order_by_id(self):
        order = Order(id=1, car=Car(id=1, plate_number="ABC123", seats=4,
                                    car_info=CarInfo(brand="Toyota", model="Corolla", color="Blue", year=2020)),
                      driver=Driver(id=1),
                      client=Client(id=1, phone_number="1234567890"),
                      start_location=Location(0, 0),
                      current_driver_location=Location(0, 0),
                      end_location=Location(1, 1),
                      price=10.0,
                      start_date=datetime.now(),
                      category=OrderCategory.ECONOMIC,
                      status=OrderStatus.PENDING)

        # Mock the behavior of repositories
        self.order_repository.get_by_id = lambda id: list(filter(lambda x: x.id == id, [order]))[0]

        # Test get_order_by_id method
        retrieved_order = self.order_service.get_order_by_id(order_id=1)

        # Assertions
        self.assertEqual(retrieved_order, order)

    #  Test the update_order_status method of the OrderService class
    def test_update_order_status(self):
        order = Order(id=1, car=Car(id=1, plate_number="ABC123", seats=4,
                                    car_info=CarInfo(brand="Toyota", model="Corolla", color="Blue", year=2020)),
                      driver=Driver(id=1),
                      client=Client(id=1, phone_number="1234567890"),
                      start_location=Location(0, 0),
                      current_driver_location=Location(0, 0),
                      end_location=Location(1, 1),
                      price=10.0,
                      start_date=datetime.now(),
                      category=OrderCategory.ECONOMIC,
                      status=OrderStatus.PENDING)

        # Mock the behavior of repositories
        self.order_repository.get_by_id = MagicMock(return_value=order)
        self.order_repository.update = MagicMock(return_value=order)

        # Test update_order_status method
        updated_order = self.order_service.update_order_status(order_id=1, new_status=OrderStatus.COMPLETED)

        # Assertions
        self.assertEqual(updated_order.status, OrderStatus.COMPLETED)


if __name__ == '__main__':
    unittest.main()
