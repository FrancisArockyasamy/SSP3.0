# Pydantic models for input data validation

from pydantic import BaseModel


class CategoryCreate(BaseModel):
    category_name: str

class ItemCreate(BaseModel):
    name: str
    description: str
    quantity: int
    category_id: int

class VendorCreate(BaseModel):
    name: str
    contact_details: str

class PurchaseCreate(BaseModel):
    item_id: int
    vendor_id: int
    quantity: int
    cost_per_unit: float

class DistributionCreate(BaseModel):
    item_id: int
    department_id: int
    quantity_allocated: int

class StockMovementCreate(BaseModel):
    item_id: int
    from_location_id: int
    to_location_id: int
    quantity_moved: int

class ReorderLevelCreate(BaseModel):
    item_id: int
    reorder_level: int

class InventoryReceiptCreate(BaseModel):
    item_id: int
    supplier_id: int
    quantity_received: int