from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database

# Initialize the FastAPI app
app = FastAPI(title="Smart Pot API")

# Create the database tables on startup
models.Base.metadata.create_all(bind=database.engine)

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/data", response_model=schemas.SensorDataResponse)
async def create_sensor_data(data: schemas.SensorDataCreate, db: Session = Depends(get_db)):
    return crud.create_sensor_data(db=db, data=data)

@app.get("/data", response_model=list[schemas.SensorDataResponse])
async def read_sensor_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_sensor_data(db=db, skip=skip, limit=limit)
