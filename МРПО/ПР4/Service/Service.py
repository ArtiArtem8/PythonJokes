from datetime import datetime

from МРПО.ПР4.Classes.Car import Car
from МРПО.ПР4.Classes.Client import Client
from МРПО.ПР4.Classes.Driver import Driver
from МРПО.ПР4.Classes.Location import Location
from МРПО.ПР4.Classes.Order import Order, OrderStatus, OrderCategory


class OrderService:
    def __init__(self,
                 orders: list[Order] = None,
                 cars: list[Car] = None,
                 drivers: list[Driver] = None,
                 clients: list[Client] = None):
        self.orders: list[Order] = orders or []
        # self.cars: list[Car] = cars or []
        # self.drivers: list[Driver] = drivers or []
        # self.clients: list[Client] = clients or []

    def create_order(self, car: Car, driver: Driver, client: Client, start_location: Location,
                     current_driver_location: Location, end_location: Location, price: float,
                     start_date: datetime = None, category: OrderCategory = OrderCategory.ECONOMIC,
                     num_passengers: int = 1) -> Order:
        """
        Creates a new order.
        """
        if not isinstance(car, Car):
            raise TypeError("Invalid car parameter. Expected Car instance.")
        if not isinstance(driver, Driver):
            raise TypeError("Invalid driver parameter. Expected Driver instance.")
        if not isinstance(client, Client):
            raise TypeError("Invalid client parameter. Expected Client instance.")
        if not isinstance(start_location, Location):
            raise TypeError("Invalid start_location parameter. Expected Location instance.")
        if not isinstance(current_driver_location, Location):
            raise TypeError("Invalid current_driver_location parameter. Expected Location instance.")
        if not isinstance(end_location, Location):
            raise TypeError("Invalid end_location parameter. Expected Location instance.")
        if not isinstance(price, float):
            raise TypeError("Invalid price parameter. Expected float.")
        if not isinstance(start_date, datetime):
            raise TypeError("Invalid start_date parameter. Expected datetime instance.")
        if not isinstance(category, OrderCategory):
            raise TypeError("Invalid category parameter. Expected OrderCategory instance.")
        if not isinstance(num_passengers, int):
            raise TypeError("Invalid num_passengers parameter. Expected int.")
        if start_date is None:
            start_date = datetime.now()

        if start_date < datetime.now():
            raise ValueError("Start date cannot be in the past.")

        if not self.check_driver_availability(driver):
            raise ValueError("Driver is not available")

        if not self.check_seats_availability(car, num_passengers):
            raise ValueError("Not enough car seats")

        if start_location.distance_to(end_location, 'm') <= 100:
            raise ValueError("Distance is too small, must be greater than 100 meters")

        if car not in driver.cars:
            raise ValueError(f"Car {car} is not belong to driver")


        order_id = self.generate_order_id()
        order = Order(id=order_id, car=car, driver=driver, client=client,
                      start_location=start_location, current_driver_location=current_driver_location,
                      end_location=end_location, price=price, start_date=start_date, category=category)

        driver.orders.append(order)
        client.orders.append(order)
        self.orders.append(order)
        return order

    # def find_available_taxi(self, start_location: Location, num_passengers: int, category: OrderCategory) -> Optional[Car]:
    #     """
    #     Finds an available taxi based on the start location, number of passengers, and category.
    #     Returns None if no available taxi is found.
    #     """
    #     drivers = self.driver_repository.drivers
    #     available_drivers: list[Driver] = list(
    #         filter(lambda x: self.check_driver_availability(x, self.order_repository.orders), drivers)
    #     )
    #
    #     for driver in available_drivers:
    #         if self.check_seats_availability(driver.cars[0], num_passengers) and driver.cars[0].category == category:
    #             return driver
    #
    #     return None
    #

    @staticmethod
    def generate_order_id() -> int:
        """
        Generates a unique order ID.
        """
        from random import randint
        return randint(0, 999_999_999)

    @staticmethod
    def check_seats_availability(car: Car, num_passengers: int) -> bool:
        """
        Checks if there are enough seats available in the car for the given number of passengers.
        """
        return car.seats >= num_passengers

    @staticmethod
    def check_driver_availability(driver: Driver) -> bool:
        """
        Checks if the driver is available based on their current orders.
        """
        return len(driver.orders) == 0

    @staticmethod
    def can_complete_order(order: Order) -> bool:
        """
        Checks if the order can be completed.
        """
        return order.status != OrderStatus.COMPLETED

    @staticmethod
    def calculate_fare(order: Order, distance: float, time: float) -> float:
        """
        Calculates the fare for the order based on distance and time.
        """
        if order.category == OrderCategory.ECONOMIC:
            return distance * time

    @staticmethod
    def update_start_location(order: Order, new_start_location: Location) -> Order:
        if not isinstance(new_start_location, Location):
            raise ValueError("Invalid start location.")
        order.start_location = new_start_location
        return order

    @staticmethod
    def update_order_status(order: Order, new_status: OrderStatus) -> Order:
        order.status = new_status
        return order
