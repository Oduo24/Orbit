#!/usr/bin/python3
"""orders module containing the class description of the Order class"""

from datetime import datetime
from .base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship

order_menuitem = Table("order_menuitem", Base.metadata,
        Column('order_id', String(60), ForeignKey('orders.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
        Column('menuitem_id', String(60), ForeignKey('menu_items.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True))

class Order(BaseModel, Base):
    """Defines the Order class"""
    __tablename__ = 'orders'

    order_number = Column(String(100), nullable=False, unique=True)
    user_id = Column(String(100), ForeignKey("users.id"))
    waiter_id = Column(String(100), ForeignKey("waiters.id"))
    table_id = Column(String(100), ForeignKey("tables.id"))
    amount = Column(Integer, ForeignKey("payments.id"), nullable=False)
    menu_items = relationship("MenuItem", secondary=order_menuitem, backref="orders")

    def __init__(self, **kwargs):
        """Class constructor
        """
        super().__init__(**kwargs)
