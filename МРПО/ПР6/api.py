
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from db_setup import setup_db, CarInfo, Location, Car, Client, Driver, Order, OrderCategory, OrderStatus, Base
from unit_of_work import UnitOfWork

app = FastAPI()

class CarInfoModel(BaseModel):
    brand: str
    model: str
    color: str
    year: int

class ClientModel(BaseModel):
    phone_number: str

class DriverModel(BaseModel):
    pass

class LocationModel(BaseModel):
    latitude: float
    longitude: float

class OrderModel(BaseModel):
    car_id: int
    driver_id: int
    client_id: int
    start_location_id: int
    current_driver_location_id: int
    end_location_id: int
    price: float
    start_date: datetime
    category: OrderCategory
    status: OrderStatus

# Dependency to get DB session
def get_db():
    with UnitOfWork() as session:
        yield session

# CRUD operations for CarInfo
@app.post("/carinfo/", response_model=CarInfoModel)
def create_carinfo(car_info: CarInfoModel, session: Session = Depends(get_db)):
    db_car_info = CarInfo(**car_info.dict())
    session.add(db_car_info)
    session.commit()
    session.refresh(db_car_info)
    return db_car_info

@app.get("/carinfo/", response_model=List[CarInfoModel])
def read_carinfos(skip: int = 0, limit: int = 10, session: Session = Depends(get_db)):
    carinfos = session.query(CarInfo).offset(skip).limit(limit).all()
    return carinfos

# CRUD operations for Client
@app.post("/client/", response_model=ClientModel)
def create_client(client: ClientModel, session: Session = Depends(get_db)):
    db_client = Client(phone_number=client.phone_number)
    session.add(db_client)
    session.commit()
    session.refresh(db_client)
    return db_client

@app.get("/client/", response_model=List[ClientModel])
def read_clients(skip: int = 0, limit: int = 10, session: Session = Depends(get_db)):
    clients = session.query(Client).offset(skip).limit(limit).all()
    return clients

# CRUD operations for Driver
@app.post("/driver/", response_model=DriverModel)
def create_driver(driver: DriverModel, session: Session = Depends(get_db)):
    db_driver = Driver()
    session.add(db_driver)
    session.commit()
    session.refresh(db_driver)
    return db_driver

@app.get("/driver/", response_model=List[DriverModel])
def read_drivers(skip: int = 0, limit: int = 10, session: Session = Depends(get_db)):
    drivers = session.query(Driver).offset(skip).limit(limit).all()
    return drivers

# CRUD operations for Order
@app.post("/order/", response_model=OrderModel)
def create_order(order: OrderModel, session: Session = Depends(get_db)):
    db_order = Order(**order.dict())
    session.add(db_order)
    session.commit()
    session.refresh(db_order)
    return db_order

@app.get("/order/", response_model=List[OrderModel])
def read_orders(skip: int = 0, limit: int = 10, session: Session = Depends(get_db)):
    orders = session.query(Order).offset(skip).limit(limit).all()
    return orders

# Endpoint to clear all tables (for testing purposes)
@app.delete("/clear/")
def clear_all(session: Session = Depends(get_db)):
    clear_all_tables(session)
    return {"message": "All tables cleared"}

def clear_all_tables(session: Session):
    """Delete all entries from all tables."""
    meta = Base.metadata
    for table in reversed(meta.sorted_tables):
        session.execute(table.delete())
    session.commit()