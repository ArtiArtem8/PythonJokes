"""test"""
import unittest
from datetime import datetime

from МРПО.ПР5.Classes.Car import Car, CarInfo
from МРПО.ПР5.Classes.Client import Client
from МРПО.ПР5.Classes.Driver import Driver
from МРПО.ПР5.Classes.Location import Location
from МРПО.ПР5.Classes.Order import OrderCategory
from МРПО.ПР5.Service.Service import OrderService


class TestOrderService(unittest.TestCase):
    def setUp(self):
        self.order_service = OrderService()

    def test_create_order(self):
        car = Car(id=1, plate_number="ABC123", seats=4,
                  car_info=CarInfo(brand="Toyota", model="Corolla", color="Blue", year=2020))
        driver = Driver(id=1)  # Create a mock driver object
        driver.cars.append(car)
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

    def test_generate_order_id_unique_id(self):
        order_id_1 = self.order_service.generate_order_id()
        order_id_2 = self.order_service.generate_order_id()

        self.assertNotEqual(order_id_1, order_id_2)

    def test_check_seats_availability_enough_seats(self):
        car = Car(id=1, plate_number="ABC123", seats=4,
                  car_info=CarInfo(year=2003, brand="Tesla", color="Red", model="Model Y"))
        num_passengers = 3

        result = self.order_service.check_seats_availability(car, num_passengers)

        self.assertTrue(result)

    def test_check_seats_availability_enough_seats(self):
        car = Car(id=1, plate_number="ABC123", seats=4,
                  car_info=CarInfo(year=2003, brand="Tesla", color="Red", model="Model Y"))

        num_passengers = 3

        result = self.order_service.check_seats_availability(car, num_passengers)

        self.assertTrue(result)

    def test_check_driver_availability_available_driver(self):
        driver = Driver(id=1)

        result = self.order_service.check_driver_availability(driver)

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
