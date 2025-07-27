from sqlalchemy import Column, Integer, String, JSON
from app.database import Base

class WheelSpec(Base):
    __tablename__ = "wheel_specifications"
    
    id = Column(Integer, primary_key=True, index=True)
    form_number = Column(String, unique=True, index=True)  # Ensure this is unique
    submitted_by = Column(String)
    submitted_date = Column(String)
    fields = Column(JSON)

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheet"

    id = Column(Integer, primary_key=True, index=True)
    form_number = Column(String, unique=True, index=True, nullable=False)
    inspection_by = Column(String, nullable=False)
    inspection_date = Column(String, nullable=False)
    bogie_details = Column(JSON, nullable=False)
    bogie_checksheet = Column(JSON, nullable=False)
    bmbc_checksheet = Column(JSON, nullable=False)