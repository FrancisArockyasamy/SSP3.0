from fastapi import FastAPI, HTTPException, Depends, status
from models import *
from schemas import *
from database import SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/categories/", response_model=CategoryCreate)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = Category(name=category.category_name)  # Use 'name' instead of 'category_name'
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    categoryModel = CategoryCreate(category_name=db_category.name)
    return categoryModel

@app.post("/items/", response_model=ItemCreate)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    itemModel = ItemCreate(**db_item.__dict__)
    return itemModel

@app.post("/vendors/", response_model=VendorCreate)
def create_vendor(vendor: VendorCreate, db: Session = Depends(get_db)):
    db_vendor = Vendor(**vendor.dict())
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    vendorModel = VendorCreate(**db_vendor.__dict__)
    return vendorModel

@app.post("/purchases/", response_model=PurchaseCreate)
def create_purchase(purchase: PurchaseCreate, db: Session = Depends(get_db)):
    db_purchase = Purchase(**purchase.dict())
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)

    purchaseModel = PurchaseCreate(**db_purchase.__dict__)
    return purchaseModel

@app.post("/distributions/", response_model=DistributionCreate)
def create_distribution(distribution: DistributionCreate, db: Session = Depends(get_db)):
    db_distribution = Distribution(**distribution.dict())
    db.add(db_distribution)
    db.commit()
    db.refresh(db_distribution)

    distributionModel = Distribution(**db_distribution.__dict__)
    return distributionModel

@app.post("/stock_movements/", response_model=StockMovementCreate)
def create_stock_movement(stock_movement: StockMovementCreate, db: Session = Depends(get_db)):
    db_stock_movement = StockMovement(**stock_movement.dict())
    db.add(db_stock_movement)
    db.commit()
    db.refresh(db_stock_movement)
    stockMovementModel = StockMovementCreate(**db_stock_movement.__dict__)
    return stockMovementModel

@app.post("/reorder_levels/", response_model=ReorderLevelCreate)
def create_reorder_level(reorder_level: ReorderLevelCreate, db: Session = Depends(get_db)):
    db_reorder_level = ReorderLevel(**reorder_level.dict())
    db.add(db_reorder_level)
    db.commit()
    db.refresh(db_reorder_level)

    reorderLevelModel = ReorderLevelCreate(**db_reorder_level.__dict__)
    return reorderLevelModel

@app.post("/inventory_receipts/", response_model=InventoryReceiptCreate)
def create_inventory_receipt(inventory_receipt: InventoryReceiptCreate, db: Session = Depends(get_db)):
    db_inventory_receipt = InventoryReceipt(**inventory_receipt.dict())
    db.add(db_inventory_receipt)
    db.commit()
    db.refresh(db_inventory_receipt)

    inventoryReceiptModel = InventoryReceiptCreate(**db_inventory_receipt.__dict__)
    return inventoryReceiptModel

