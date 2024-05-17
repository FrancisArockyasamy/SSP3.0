from fastapi import FastAPI
import routers
from routers import trips, passengers, vehicles,boarding_details,boarding_fees,fees,routes,passengers_by_bus,buses
from models import Base
from database import engine

Base.metadata.create_all(bind= engine)

app = FastAPI()

# Include routers
app.include_router(trips.router, prefix="/trips", tags=["trips"])
app.include_router(passengers.router, prefix="/passengers", tags=["passengers"])
app.include_router(boarding_details.router, prefix="/boarding_details", tags=["boarding_details"])
app.include_router(routes.router, prefix="/routes", tags=["routes"])
app.include_router(vehicles.router, prefix="/vehicles", tags=["vehicles"])
app.include_router(boarding_fees.router, prefix="/boarding_fees", tags=["boarding_fees"])
app.include_router(fees.router, prefix="/fees", tags=["fees"])
app.include_router(passengers_by_bus.router, prefix="/passengers_by_bus", tags=["passengers_by_bus"])
app.include_router(buses.router, prefix="/buses", tags=["buses"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
