#!/usr/bin/python3
"""customers module containing the class description of the Customer class"""
from .base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship


class Customer(BaseModel, Base):
    """Defines the Customer class"""
    __tablename__ = "customers"

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email_address = Column(String(100), nullable=False)
    phone_number = Column(Integer, nullable=False)
    account_balance = Column(Integer, nullable=False)
    orders = relationship("Order", backref="customer")


    def __init__(self):
        """Initializes an customer instance
        """
        super().__init__()
