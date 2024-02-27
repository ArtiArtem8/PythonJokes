from ..Classes.Car import Car
from ..Classes.Driver import Driver
from ..Classes.Location import Location
from ..Classes.Order import Order, OrderStatus, OrderCategory


def check_seats_availability(car: Car, num_passengers: int) -> bool:
    return car.seats >= num_passengers


def check_driver_availability(driver: Driver, current_orders: list[Order]) -> bool:
    return len([order for order in current_orders if order.driver == driver]) == 0


def can_complete_order(order: Order) -> bool:
    """Check if the order can be completed."""
    return order.status != OrderStatus.COMPLETED


def calculate_fare(order: Order, distance: float, time: float) -> float:
    """Calculate the fare for the order based on distance and time."""
    if order.category == OrderCategory.ECONOMIC:
        pass
    return distance * time


def track_vehicle_location(vehicle_id: int) -> Location:
    """Track the current location of a vehicle."""
    # Add logic to track the location of the vehicle with the given ID
    pass
