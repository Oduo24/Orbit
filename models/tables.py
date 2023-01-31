#!/usr/bin/python3
"""tables module containing the class description of the Table class"""
from .base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship


class Table(BaseModel, Base):
    """Defines the Table class"""
    __tablename__ = "tables"

    table_name = Column(String(100), nullable=False, unique=True)
    location = Column(String(100), nullable=False)
    capacity = Column(Integer, nullable=False)

    def __init__(self, **kwargs):
        """Initializes a table instance
        """
        super().__init__(**kwargs)
