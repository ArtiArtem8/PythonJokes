from datetime import datetime, timezone

from sqlalchemy.orm import Session

from db_setup import (setup_db, CarInfo, Location, Car, Client, Driver,
                      Order, OrderCategory, OrderStatus, Base)


def clear_all_tables(_session: Session):
    """Delete all entries from all tables."""
    meta = Base.metadata
    for table in reversed(meta.sorted_tables):
        print(f"Clearing table {table}")
        _session.execute(table.delete())
    _session.commit()


# Setup the database and create a session
session = setup_db()
clear_all_tables(session)
# Create CarInfo entries
car_info1 = CarInfo(brand='Toyota', model='Camry', color='Blue', year=2020)
car_info2 = CarInfo(brand='Tesla', model='Model 3', color='Red', year=2022)

# Add CarInfo entries to the session
session.add(car_info1)
session.add(car_info2)
session.commit()

# Create Location entries
location1 = Location(latitude=34.0522, longitude=-118.2437)
location2 = Location(latitude=36.1699, longitude=-115.1398)
location3 = Location(latitude=40.7128, longitude=-74.0060)

# Add Location entries to the session
session.add(location1)
session.add(location2)
session.add(location3)
session.commit()

# Create a Client entry
client = Client(phone_number="123-456-7890")

# Add Client entry to the session
session.add(client)
session.commit()

# Create a Driver entry
driver = Driver()

# Add Driver entry to the session
session.add(driver)
session.commit()

# Create Car entries
car1 = Car(plate_number="ABC123", seats=4, car_info=car_info1, owner=driver)
car2 = Car(plate_number="XYZ789", seats=4, car_info=car_info2, owner=driver)

# Add Car entries to the session
session.add(car1)
session.add(car2)
session.commit()

# Create an Order entry
order = Order(
    car=car1,
    driver=driver,
    client=client,
    start_location=location1,
    current_driver_location=location2,
    end_location=location3,
    price=100.0,
    start_date=datetime.now(timezone.utc),
    category=OrderCategory.COMFORT,
    status=OrderStatus.PENDING
)

# Add Order entry to the session
session.add(order)
session.commit()

# Query the database
# Retrieve all clients
clients = session.query(Client).all()
print("Clients:")
for c in clients:
    print(f"ID: {c.id}, Phone Number: {c.phone_number}")

# Retrieve all drivers
drivers = session.query(Driver).all()
print("\nDrivers:")
for d in drivers:
    print(f"ID: {d.id}")

# Retrieve all cars
cars = session.query(Car).all()
print("\nCars:")
for car in cars:
    print(f"id={car.id}:Plate Number: {car.plate_number}, Seats: {car.seats}, "
          f"Brand: {car.car_info.brand}, Model: {car.car_info.model}")

# Retrieve all orders
orders = session.query(Order).all()
print("\nOrders:")
for o in orders:
    print(f"Order ID: {o.id}, Client ID: {o.client.id},"
          f" Driver ID: {o.driver.id}, Price: {o.price}, Status: {o.status.value}")

""" Результат программы
Clients:
ID: 1, Phone Number: 123-456-7890

Drivers:
ID: 1

Cars:
Plate Number: ABC123, Seats: 4, Brand: Toyota, Model: Camry
Plate Number: XYZ789, Seats: 4, Brand: Tesla, Model: Model 3

Orders:
Order ID: 1, Client ID: 1, Driver ID: 1, Price: 100.0, Status: Pending"""

# Close the session
session.close()
