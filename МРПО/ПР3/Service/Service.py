from datetime import datetime

from МРПО.ПР3.Classes.Car import Car
from МРПО.ПР3.Classes.Driver import Driver
from МРПО.ПР3.Classes.Location import Location
from МРПО.ПР3.Classes.Order import Order, OrderStatus, OrderCategory
from МРПО.ПР3.Repository.CarRepository import CarRepository
from МРПО.ПР3.Repository.ClientRepository import ClientRepository
from МРПО.ПР3.Repository.DriverRepository import DriverRepository
from МРПО.ПР3.Repository.OrderRepository import OrderRepository


class OrderService:
    def __init__(self, order_repository, car_repository, driver_repository, client_repository):
        self.order_repository: OrderRepository = order_repository
        self.car_repository: CarRepository = car_repository
        self.driver_repository: DriverRepository = driver_repository
        self.client_repository: ClientRepository = client_repository

    def create_order(self, car_id: int, driver_id: int, client_id: int, start_location: Location,
                     current_driver_location: Location, end_location: Location, price: float,
                     start_date: datetime, category: OrderCategory = OrderCategory.ECONOMIC,
                     num_passengers: int = 1) -> Order:
        """
        Creates a new order.
        """
        car = self.car_repository.get_by_id(car_id)
        if not self.check_seats_availability(car, num_passengers):
            raise ValueError("Not enough seats available in the car.")

        driver = self.driver_repository.get_by_id(driver_id)
        if not self.check_driver_availability(driver, self.order_repository.get_all()):  # Assuming no current orders
            raise ValueError("Driver is not available.")

        client = self.client_repository.get_by_id(client_id)

        order = Order(id=self.generate_order_id(), car=car, driver=driver, client=client,
                      start_location=start_location, current_driver_location=current_driver_location,
                      end_location=end_location, price=price, start_date=start_date, category=category)

        self.order_repository.add(order)
        return order

    def generate_order_id(self) -> int:
        """
        Generates a unique order ID.
        """
        return 0

    @staticmethod
    def check_seats_availability(car: Car, num_passengers: int) -> bool:
        """
        Checks if there are enough seats available in the car for the given number of passengers.
        """
        return car.seats >= num_passengers

    @staticmethod
    def check_driver_availability(driver: Driver, current_orders: list[Order]) -> bool:
        """
        Checks if the driver is available based on their current orders.
        """
        return len([order for order in current_orders if order.driver == driver]) == 0

    def can_complete_order(self, order_id: int) -> bool:
        """
        Checks if the order can be completed.
        """
        order = self.order_repository.get_by_id(order_id)
        return order.status != OrderStatus.COMPLETED

    def calculate_fare(self, order_id: int, distance: float, time: float) -> float:
        """
        Calculates the fare for the order based on distance and time.
        """
        order = self.order_repository.get_by_id(order_id)
        if order.category == OrderCategory.ECONOMIC:
            return distance * time

    def update_start_location(self, order_id: int, new_start_location: Location) -> Location:
        order = self.order_repository.get_by_id(order_id)
        order.start_location = new_start_location
        self.order_repository.update(order)

    def get_order_by_id(self, order_id: int) -> Order:
        return self.order_repository.get_by_id(order_id)

    def update_order_status(self, order_id: int, new_status: OrderStatus):
        order = self.order_repository.get_by_id(order_id)
        order.status = new_status
        self.order_repository.update(order)
