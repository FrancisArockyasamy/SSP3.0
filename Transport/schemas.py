from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class TripBase(BaseModel):
    date: datetime
    time: datetime
    starting_point: str
    destination: str
    purpose: str

class TripCreate(TripBase):
    pass

class Trip(TripBase):
    trip_id: int
    class Config:
        orm_mode = True

class PassengerBase(BaseModel):
    name: str
    contact_information: str
    boarding_point: str

class PassengerCreate(PassengerBase):
    trip_id: int

class Passenger(PassengerBase):
    passenger_id: int
    trip_id: int
    class Config:
        orm_mode = True

class BoardingDetailBase(BaseModel):
    stop_name: str
    boarding_time: datetime
    alighting_time: datetime

class BoardingDetailCreate(BoardingDetailBase):
    trip_id: int
    passenger_id: int

class BoardingDetail(BoardingDetailBase):
    boarding_id: int
    trip_id: int
    passenger_id: int
    class Config:
        orm_mode = True

class RouteBase(BaseModel):
    route_name: str
    distance: float

class RouteCreate(RouteBase):
    pass

class Route(RouteBase):
    route_id: int
    class Config:
        orm_mode = True

class VehicleBase(BaseModel):
    registration_number: str
    seating_capacity: int
    maintenance_schedule: str

class VehicleCreate(VehicleBase):
    pass

class VehicleUpdate(VehicleBase):
    pass

class Vehicle(VehicleBase):
    vehicle_id: int
    class Config:
        orm_mode = True

class BoardingFeeBase(BaseModel):
    boarding_fee: float
    discount: float
    concession: float

class BoardingFeeCreate(BoardingFeeBase):
    trip_id: int
    vehicle_id: int

class BoardingFee(BoardingFeeBase):
    fee_id: int
    trip_id: int
    vehicle_id: int
    class Config:
        orm_mode = True

class FeeBase(BaseModel):
    total_amount_collected: float
    outstanding_payments: float

class FeeCreate(FeeBase):
    trip_id: int

class Fee(FeeBase):
    fee_id: int
    trip_id: int
    class Config:
        orm_mode = True
        
class FeeGet(FeeBase):
    fee_id: int
    trip_id: int
    class Config:
        orm_mode = True

class PassengerTripCreate(BaseModel):
    name: str
    contact_information: str
    boarding_point: str
    trip_details: dict

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "contact_information": "john.doe@example.com",
                "boarding_point": "Bus Stop A",
                "trip_details": {
                    "date": "2024-05-20",
                    "time": "09:00:00",
                    "starting_point": "Location A",
                    "destination": "Location B",
                    "purpose": "Work commute"
                }
            }
        }

class PassengerByBus(BaseModel):
    bus_number: str
    trip_number: str
    passengers: List[str]

    class Config:
        schema_extra = {
            "example": {
                "bus_number": "Bus101",
                "passengers": ["John Doe", "Jane Smith"]
            }
        }
        
class BusCreate(BaseModel):
    bus_number: str
    description: str

class Bus(BaseModel):
    id:int
    bus_number: str
    description: str
    
class PassengerByBusBase(BaseModel):
    trip_id: int
    bus_id: int
    description: Optional[str] = None
    passengers: List[str] 

class PassengerByBusCreate(PassengerByBusBase):
    pass

class PassengerByBusUpdate(PassengerByBusBase):
    pass

class PassengerByBus(PassengerByBusBase):
    id: int

    class Config:
        orm_mode: True