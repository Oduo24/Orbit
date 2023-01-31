#!/usr/bin/python3
"""Class description for creation of unique numbers"""
from .base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship


class Unique_number(BaseModel, Base):
    """Defines the Unique_number class"""
    __tablename__ = "unique_numbers"

    name = Column(String(100), nullable=False)
    number = Column(Integer, nullable=False)

    def __init__(self, **kwargs):
        """Initializes a uom instance
        """
        super().__init__(**kwargs)
