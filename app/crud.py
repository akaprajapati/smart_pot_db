from sqlalchemy.orm import Session
from . import models, schemas

def create_sensor_data(db: Session, data: schemas.SensorDataCreate):
    db_data = models.SensorData(
        moisture_level=data.moisture,
        temperature=data.temperature,
        light_level=data.light
    )
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_all_sensor_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SensorData).offset(skip).limit(limit).all()
