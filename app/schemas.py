from pydantic import BaseModel
from datetime import datetime

class SensorDataCreate(BaseModel):
    moisture: int
    temperature: float
    light: float

class SensorDataResponse(BaseModel):
    id: int
    timestamp: datetime
    moisture_level: int
    temperature: float
    light_level: float

    class Config:
        from_attributes = True
