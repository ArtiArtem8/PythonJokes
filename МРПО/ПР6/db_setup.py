import datetime
import re
from enum import Enum as PyEnum

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker, backref
from sqlalchemy.types import Enum as SQLAlchemyEnum

Base = declarative_base()

VALID_MODELS_BY_BRAND: dict[str, set[str]] = {
    "Toyota": {"Camry", "Corolla", "RAV4"},
    "Honda": {"Accord", "Civic", "CR-V"},
    "Ford": {"F-150", "Escape", "Focus"},
    "Chevrolet": {"Silverado", "Equinox", "Malibu"},
    "Tesla": {"Model S", "Model 3", "Model X", "Model Y"}
}


class InvalidIdError(Exception):
    """Exception raised for invalid id values."""

    def __init__(self, id_value):
        self.id_value = id_value
        super().__init__(f"Id must be a positive integer. Got {id_value}.")


class IdMixin(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

    def __post_init__(self):
        if self.id is not None and self.id < 0:
            raise InvalidIdError(self.id)


class OrderStatus(PyEnum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    WAITING = "Waiting"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class OrderCategory(PyEnum):
    ECONOMIC = "Economic"
    COMFORT = "Comfort"
    BUSINESS = "Business"
    OTHER = "Other"


class CarInfo(Base):
    __tablename__ = 'car_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    color = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

    def __init__(self, brand, model, color, year):
        if brand not in VALID_MODELS_BY_BRAND:
            raise ValueError(f"Invalid brand: {brand}")
        if model not in VALID_MODELS_BY_BRAND.get(brand, []):
            raise ValueError(f"Invalid model: {model}")
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)


class Car(IdMixin, Base):
    __tablename__ = 'car'
    plate_number = Column(String, nullable=False, unique=True)
    seats = Column(Integer, nullable=False)
    car_info_id = Column(Integer, ForeignKey('car_info.id'), nullable=False)
    owner_id = Column(Integer, ForeignKey('driver.id'), nullable=True)

    car_info = relationship('CarInfo')
    owner = relationship('Driver', back_populates='cars')

    def __init__(self, plate_number, seats, car_info, owner=None):
        if not re.match(r'^[A-Z0-9А-Я]{6}$', plate_number):
            raise ValueError("Invalid plate number format")
        if seats <= 0:
            raise ValueError("Invalid number of seats: seats must be a positive integer.")
        self.plate_number = plate_number
        self.seats = seats
        self.car_info = car_info
        self.owner = owner


class Client(IdMixin, Base):
    __tablename__ = 'client'
    phone_number = Column(String, nullable=False, unique=True)
    orders = relationship('Order', back_populates='client')

    def __init__(self, phone_number):
        self.phone_number = phone_number


class Driver(IdMixin, Base):
    __tablename__ = 'driver'
    cars = relationship('Car', back_populates='owner')
    orders = relationship('Order', back_populates='driver')


class Order(IdMixin, Base):
    __tablename__ = 'order'
    car_id = Column(Integer, ForeignKey('car.id'), nullable=False)
    driver_id = Column(Integer, ForeignKey('driver.id'), nullable=False)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    start_location_id = Column(Integer, ForeignKey('location.id'), nullable=False)
    current_driver_location_id = Column(Integer, ForeignKey('location.id'), nullable=False)
    end_location_id = Column(Integer, ForeignKey('location.id'), nullable=False)
    price = Column(Float, nullable=False)
    start_date = Column(DateTime, default=lambda: datetime.datetime.now(datetime.UTC), nullable=False)
    category = Column(SQLAlchemyEnum(OrderCategory), default=OrderCategory.ECONOMIC, nullable=False)
    status = Column(SQLAlchemyEnum(OrderStatus), default=OrderStatus.PENDING, nullable=False)

    car = relationship('Car')
    driver = relationship('Driver', back_populates='orders')
    client = relationship('Client', back_populates='orders')
    start_location = relationship('Location', foreign_keys=[start_location_id],
                                  backref=backref('order_start', uselist=False))
    current_driver_location = relationship('Location', foreign_keys=[current_driver_location_id],
                                           backref=backref('order_current', uselist=False))
    end_location = relationship('Location', foreign_keys=[end_location_id], backref=backref('order_end', uselist=False))


def setup_db(engine_url='sqlite:///taxi_service.db'):
    engine = create_engine(engine_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


if __name__ == '__main__':
    session = setup_db()
    print("Database setup complete.", session)
