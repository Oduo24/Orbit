#!/usr/bin/python3
"""menu_items module containing the class description of the MenuItem class"""

from .base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class MenuItem(BaseModel, Base):
    """Defines the MenuItem class"""
    __tablename__ = 'menu_items'

    item_name = Column(String(100), nullable=False, unique=True)
    price = Column(Integer, nullable=False)
    category_id = Column(String(100), ForeignKey("categories.id"))
    uom_id = Column(String(100), ForeignKey("uom.id"))
    quantity = Column(Integer, nullable=False)

    def __init__(self):
        """Class constructor
        """
        super().__init__()
