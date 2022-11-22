#!/usr/bin/python3
"""UOM module containing the class description of the Uom class"""
from .base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship


class Uom(BaseModel, Base):
    """Defines the Uom class"""
    __tablename__ = "uom"

    symbol= Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    menu_items = relationship("MenuItem", backref="uom")

    def __init__(self, **kwargs):
        """Initializes a uom instance
        """
        super().__init__(**kwargs)
