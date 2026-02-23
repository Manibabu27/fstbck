from db import Base
from sqlalchemy.ext.declarative import declarative_base

import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer,Boolean,DateTime


class employe_details(Base):
    __tablename__ = "employe_details"
    employee_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True)
    department = Column(String)

class attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String)