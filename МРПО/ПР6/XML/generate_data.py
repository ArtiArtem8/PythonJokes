from МРПО.ПР6.Classes.Car import Car, CarInfo
from МРПО.ПР6.Classes.Client import Client
from МРПО.ПР6.Classes.Driver import Driver
from МРПО.ПР6.Classes.Location import Location
from МРПО.ПР6.Classes.Order import Order, OrderStatus, OrderCategory

from datetime import datetime
import random
import string


def generate_random_string(length: int) -> str:
    """Generate a random string of specified length."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def generate_random_phone_number() -> str:
    """Generate a random phone number."""
    return ''.join(random.choices(string.digits, k=10))


def generate_random_location() -> Location:
    """Generate a random location."""
    return Location(latitude=random.uniform(-90, 90), longitude=random.uniform(-180, 180))


def generate_random_car_info() -> CarInfo:
    """Generate random car information."""
    brands = ["Toyota", "Honda", "Ford", "Chevrolet", "Tesla"]
    models_by_brand = {
        "Toyota": ["Camry", "Corolla", "RAV4"],
        "Honda": ["Accord", "Civic", "CR-V"],
        "Ford": ["F-150", "Escape", "Focus"],
        "Chevrolet": ["Silverado", "Equinox", "Malibu"],
        "Tesla": ["Model S", "Model 3", "Model X", "Model Y"]
    }
    brand = random.choice(brands)
    model = random.choice(models_by_brand[brand])
    color = generate_random_string(5)
    year = random.randint(2000, 2023)
    return CarInfo(brand=brand, model=model, color=color, year=year)


def generate_test_data(num_drivers: int, num_clients: int, num_cars_per_driver: int, num_orders_per_client: int) -> \
tuple[list[Driver], list[Client], list[Order], list[Car]]:
    """Generate test data for drivers, clients, orders, and cars."""
    drivers = []
    clients = []
    orders = []
    cars = []

    # Generate clients
    for i in range(num_clients):
        client_id = i + 1
        phone_number = generate_random_phone_number()
        client = Client(id=client_id, phone_number=phone_number)
        clients.append(client)
    # Generate drivers
    for i in range(num_drivers):
        driver_id = i + 1

        driver = Driver(id=driver_id)
        drivers.append(driver)

        # Generate cars for each driver
        for j in range(num_cars_per_driver):
            car_info = generate_random_car_info()
            plate_number = generate_random_string(6).upper()
            seats = random.randint(2, 7)
            car = Car(id=(i * num_cars_per_driver) + j + 1, plate_number=plate_number, seats=seats, car_info=car_info,
                      owner=driver)
            cars.append(car)
            driver.cars.append(car)

        # Generate orders for each client
        for k in range(num_orders_per_client):
            client_id = (i * num_orders_per_client) + k + 1
            start_location = generate_random_location()
            current_driver_location = generate_random_location()
            end_location = generate_random_location()
            price = random.uniform(10, 100)
            start_date = datetime.now()
            category = random.choice(list(OrderCategory))
            status = random.choice(list(OrderStatus))
            client = random.choice(clients)
            order = Order(id=client_id, car=random.choice(driver.cars), driver=driver, client=client,
                          start_location=start_location,
                          current_driver_location=current_driver_location, end_location=end_location, price=price,
                          start_date=start_date, category=category, status=status)
            orders.append(order)
            client.orders.append(order)



    return drivers, clients, orders, cars


# Generate test data with 3 drivers, 2 clients, 2 cars per driver, and 3 orders per client
num_drivers = 3
num_clients = 2
num_cars_per_driver = 2
num_orders_per_client = 3

drivers, clients, orders, cars = generate_test_data(num_drivers, num_clients, num_cars_per_driver,
                                                    num_orders_per_client)

# Print some sample data for verification
print("Sample Drivers:")
for driver in drivers:
    print(driver)

print("\nSample Clients:")
for client in clients:
    print(client)

print("\nSample Orders:")
for order in orders:
    print(order)

print("\nSample Cars:")
for car in cars:
    print(car)
