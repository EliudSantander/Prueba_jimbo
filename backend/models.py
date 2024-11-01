from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String)

    created_at = Column(DateTime(), default=datetime.now())


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    price = Column(DECIMAL(10, 2))
    created_at = Column(DateTime(), default=datetime.now())