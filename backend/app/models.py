from sqlalchemy import Column, Integer, String
from .database import Base


# this is defining the Task Model,
# basically creates a tasks table and defines how data is stored in it
class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)