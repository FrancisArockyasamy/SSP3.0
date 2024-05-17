from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database

router = APIRouter()

@router.post("/routes/", response_model=schemas.Route)
async def create_route(route: schemas.RouteCreate, db: Session = Depends(database.get_db)):
    db_route = models.Route(**route.dict())
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    return db_route

@router.get("/routes/", response_model=List[schemas.Route])
async def read_routes(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    routes = db.query(models.Route).offset(skip).limit(limit).all()
    return routes

@router.get("/routes/{route_id}", response_model=schemas.Route)
async def read_route(route_id: int, db: Session = Depends(database.get_db)):
    route = db.query(models.Route).filter(models.Route.route_id == route_id).first()
    if route is None:
        raise HTTPException(status_code=404, detail="Route not found")
    return route
