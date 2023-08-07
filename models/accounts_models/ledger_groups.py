#!/usr/bin/python3
"""This module contains the class description of ledger groups available"""

from datetime import datetime
from sqlalchemy import String, Column, Integer, DateTime, ForeignKey, Enum, Index
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base

from .ledgers import Ledger

class LedgerGroup(BaseModel, Base):
    """Defines the ledger groups class"""
    __tablename__ = 'ledger_groups'

    group_name = Column(String(100), nullable=False, unique=True)
    description = Column(String(250), nullable=True)
    nature_of_group = Column(Enum('asset', 'liability', 'income', 'expense', name='nature_of_ledger_account'), nullable=False)
    ledgers = relationship('Ledger', back_populates='ledger_group')

    def __init__(self, **kwargs):
        """Class constructor
        """
        super().__init__(**kwargs)

# Add an index on the 'group_name' column
Index('idx_group_name', LedgerGroup.group_name)
