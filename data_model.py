from sqlalchemy import Column, Integer, String
from database.db import Base

class ProcessedData(Base):
    __tablename__ = "processed_data"

    id = Column(Integer, primary_key=True, index=True)
    input_data = Column(String)
    result = Column(String)