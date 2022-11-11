#!/usr/bin/python3
"""tender_types module containing the class description of the Tender_types class"""
from .base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship


class TenderType(BaseModel, Base):
    """Defines the TenderType class"""
    __tablename__ = "tender_types"

    tender_name = Column(String(100), nullable=False, primary_key=True)
    description = Column(String(100), nullable=False)
    payments = relationship("Payment", backref="tender_type")

    def __init__(self):
        """Initializes a TenderType instance
        """
        super().__init__()
