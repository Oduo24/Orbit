#!/usr/bin/python3
"""customer module, contains the class description of the Customer class"""
from .base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship


class Customer(BaseModel, Base):
    """Defines the Customer class"""
    __tablename__ = "customers"

    customer_name = Column(String(100), nullable=False, unique=True)
    contact = Column(String(100), nullable=True)
    balance = Column(Integer, nullable=False, default=0)


    def __init__(self, **kwargs):
        """Initializes a customer instance
        """
        super().__init__(**kwargs)
