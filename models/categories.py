#!/usr/bin/python3
"""Categories module containing the class description of the categories class"""
from .base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    """Defines the Category class"""
    __tablename__ = "categories"

    category_name = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    menu_items = relationship("MenuItem", backref="category")

    def __init__(self):
        """Initializes an category instance
        """
        super().__init__()




    

