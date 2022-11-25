#!/usr/bin/python3
"""waiters module containing the class description of the Waiter class"""
from .base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship

waiter_table = Table("waiter_table", Base.metadata,
        Column('waiter_id', String(60), ForeignKey('waiters.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
        Column('table_id', String(60), ForeignKey('tables.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True))

class Waiter(BaseModel, Base):
    """Defines the Waiter class"""
    __tablename__ = "waiters"

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email_address = Column(String(100), nullable=False)
    phone_number = Column(Integer, nullable=False)
    passcode = Column(String(100), nullable=False)
    orders = relationship("Order", backref="waiter")
    tables = relationship("Table", secondary=waiter_table, backref="waiters")

    def __init__(self, **kwargs):
        """Initializes a waiter instance
        """
        super().__init__(**kwargs)
