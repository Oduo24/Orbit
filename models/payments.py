#!/usr/bin/python3
"""payments module containing the class description of the Payment class"""

from .base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Payment(BaseModel, Base):
    """Defines the Payment class"""
    __tablename__ = 'payments'

    transaction_id = Column(String(100), nullable=False, unique=True)
    tender_type_id = Column(String(100), ForeignKey("tender_types.id"))


    def __init__(self):
        """Class constructor
        """
        super().__init__()
