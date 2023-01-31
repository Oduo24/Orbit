#!/usr/bin/python3
"""tables module containing the class description of the Table class"""
from .base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship


class Counter(BaseModel, Base):
    """Defines the Counter class"""
    __tablename__ = "counters"

    counter_name = Column(String(100), nullable=False, unique=True)
    location = Column(String(100), nullable=False)


    def __init__(self, **kwargs):
        """Initializes a counter instance
        """
        super().__init__(**kwargs)
