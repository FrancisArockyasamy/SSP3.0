from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base, engine # Assuming Base is defined in database.py

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)  # Use 'name' instead of 'category_name'

    items = relationship("Item", back_populates="category")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    quantity = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="items")

class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_details = Column(String)

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    vendor_id = Column(Integer, ForeignKey("vendors.id"))
    purchase_date = Column(DateTime, default=datetime.now)
    quantity = Column(Integer)
    cost_per_unit = Column(Float)

class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    current_quantity = Column(Integer)

class Distribution(Base):
    __tablename__ = "distribution"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    department_id = Column(Integer)
    quantity_allocated = Column(Integer)

class StockMovement(Base):
    __tablename__ = "stock_movement"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    from_location_id = Column(Integer)
    to_location_id = Column(Integer)
    quantity_moved = Column(Integer)
    movement_date = Column(DateTime, default=datetime.now)

class ReorderLevel(Base):
    __tablename__ = "reorder_levels"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    reorder_level = Column(Integer)

class InventoryReceipt(Base):
    __tablename__ = "inventory_receipts"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    supplier_id = Column(Integer, ForeignKey("vendors.id"))
    quantity_received = Column(Integer)
    receipt_date = Column(DateTime, default=datetime.now)

Base.metadata.create_all(bind=engine)