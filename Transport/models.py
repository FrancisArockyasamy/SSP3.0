from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey,JSON
from sqlalchemy.orm import relationship
from .database import Base

class Trip(Base):
    __tablename__ = "tbl_trips"
    trip_id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    time = Column(DateTime)
    starting_point = Column(String)
    destination = Column(String)
    purpose = Column(String)

    passengers = relationship("Passenger", back_populates="trip")
    boarding_details = relationship("BoardingDetail", back_populates="trip")
    boarding_fees = relationship("BoardingFee", back_populates="trip")
    fees = relationship("Fee", back_populates="trip")

class Passenger(Base):
    __tablename__ = "tbl_passengers"
    passenger_id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer, ForeignKey("tbl_trips.trip_id"))
    name = Column(String)
    contact_information = Column(String)
    boarding_point = Column(String)

    trip = relationship("Trip", back_populates="passengers")
    boarding_details = relationship("BoardingDetail", back_populates="passenger")

class BoardingDetail(Base):
    __tablename__ = "tbl_boarding_details"
    boarding_id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer, ForeignKey("tbl_trips.trip_id"))
    passenger_id = Column(Integer, ForeignKey("tbl_passengers.passenger_id"))
    stop_name = Column(String)
    boarding_time = Column(DateTime)
    alighting_time = Column(DateTime)

    trip = relationship("Trip", back_populates="boarding_details")
    passenger = relationship("Passenger", back_populates="boarding_details")

class Route(Base):
    __tablename__ = "tbl_routes"
    route_id = Column(Integer, primary_key=True, index=True)
    route_name = Column(String)
    distance = Column(Float)

class Vehicle(Base):
    __tablename__ = "tbl_vehicles"
    vehicle_id = Column(Integer, primary_key=True, index=True)
    registration_number = Column(String)
    seating_capacity = Column(Integer)
    maintenance_schedule = Column(String)

class BoardingFee(Base):
    __tablename__ = "tbl_boarding_fees"
    fee_id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer, ForeignKey("tbl_trips.trip_id"))
    vehicle_id = Column(Integer, ForeignKey("tbl_vehicles.vehicle_id"))
    boarding_fee = Column(Float)
    discount = Column(Float)
    concession = Column(Float)

    trip = relationship("Trip", back_populates="boarding_fees")
    vehicle = relationship("Vehicle")

class Fee(Base):
    __tablename__ = "tbl_fees"
    fee_id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer, ForeignKey("tbl_trips.trip_id"))
    total_amount_collected = Column(Float)
    outstanding_payments = Column(Float)

    trip = relationship("Trip", back_populates="fees")

class Bus(Base):
    __tablename__ = "tbl_buses"
    id = Column(Integer, primary_key=True, index=True)
    bus_number = Column(String, unique=True, index=True)
    description = Column(String)

class PassengerByBus(Base):
    __tablename__ = "tbl_passenger_by_bus"
    id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer, ForeignKey("tbl_trips.trip_id"))
    bus_id = Column(Integer,ForeignKey("tbl_buses.id"))
    description = Column(String)
    passengers = Column(JSON)