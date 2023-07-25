#!/usr/bin/python3
"""orders module containing the class description of the Order class"""

from datetime import datetime
from .base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship

order_menuitem = Table("order_menuitem", Base.metadata,
        Column('item_name', String(100), ForeignKey('menu_items.item_name'), primary_key=True),
        Column('order_number', Integer, ForeignKey('orders.order_number'), nullable=False, primary_key=True),
        Column('quantity', Integer, nullable=False),
        Column('amount', Integer, nullable=False))


class Order(BaseModel, Base):
    """Defines the Order class"""
    __tablename__ = 'orders'

    order_number = Column(Integer, nullable=False, primary_key=True)
    customer = Column(String(100), nullable=False)
    waiter = Column(String(100), nullable=False)
    table = Column(String(100), nullable=False)
    counter = Column(String(100), nullable=False)
    tender = Column(String(100), nullable=False)
    total = Column(Integer, nullable=False)
    is_served = Column(Integer, default=0)
    isPaid = Column(String(100), nullable=True)
    menu_items = relationship("MenuItem", secondary=order_menuitem, backref="orders")

    def __init__(self, **kwargs):
        """Class constructor
        """
        super().__init__(**kwargs)
