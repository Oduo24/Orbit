#!/usr/bin/python3
"""This module defines the leder class. Every created ledger is defined by this class"""

from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship

class Ledger(BaseModel, Base):
    """Defines the Order class"""
    __tablename__ = 'ledgers'

    account_no = Column(String(100), nullable=False)
    ledger_name = Column(String(100), nullable=False, unique=True)
    ledger_opening_amount = Column(Integer, nullable=False)
    group_name = Column(String(100), ForeignKey('ledger_groups.group_name'), nullable=False)
    ledger_group = relationship('LedgerGroup', back_populates='ledgers')
    dr = Column(Integer, nullable=True)
    cr = Column(Integer, nullable=True)


    def __init__(self, **kwargs):
        """Class constructor
        """
        super().__init__(**kwargs)
