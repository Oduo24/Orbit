#!/usr/bin/python3
"""This module contains the class description of account groups available"""

from datetime import datetime
from sqlalchemy import String, Column, Integer, DateTime, ForeignKey, Enum, Index
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base

from .accounts import Account

class AccountGroup(BaseModel, Base):
    """Defines the account groups class"""
    __tablename__ = 'account_groups'

    group_name = Column(String(100), nullable=False, unique=True)
    description = Column(String(250), nullable=True)
    nature_of_group = Column(Enum('asset', 'liability', 'income', 'expense', name='nature_of_account_group'), nullable=False)
    accounts = relationship('Account', back_populates='account_group')

    def __init__(self, **kwargs):
        """Class constructor
        """
        super().__init__(**kwargs)

# Add an index on the 'group_name' column
Index('idx_group_name', AccountGroup.group_name)
