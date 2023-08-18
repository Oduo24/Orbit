#!/usr/bin/python3
"""This module defines the leder class. Every created ledger is defined by this class"""

from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey, DateTime, Table, Date, Enum, Index
from sqlalchemy.orm import relationship


class GRN(BaseModel, Base):
    """Defines the GRN class"""
    __tablename__ = 'grns'
    
    grn_no = Column(String(100), nullable=False)
    amount = Column(Integer, nullable=False)
    supplier_name = Column(String(100), ForeignKey("suppliers.supplier_name"), nullable=False)

    # One to many relationship between grn and suppliers table
    supplier = relationship('Supplier', back_populates='grns')

    # One to many relationship between grn and the association table grn_stockitems
    items = relationship('GRNStockItem', back_populates="grn")


    def __init__(self, **kwargs):
        """Class constructor
        """
        super().__init__(**kwargs)
    
class GRNStockItem(Base):
    """The association table between GRN and stock items"""
    __tablename__ = 'grn_stockitems'

    quantity = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)

    # Foreign keys to link to grns and stock_items table
    grn_id = Column(String(100), ForeignKey('grns.id'), primary_key=True)
    stock_item_id = Column(String(100), ForeignKey("stock_items.id"), primary_key=True)
    
    # Relationship from grn_stockitems to grn
    grn = relationship('GRN', back_populates='items')
    # Relationship from grn_stockitems to stock_items
    stock_item = relationship('StockItems')




class Purchase(BaseModel, Base):
    """Defines the Purchase transactions class"""
    __tablename__ = 'purchases'

    transaction_no = Column(String(100), nullable=False)
    grn_no = Column(String(100), ForeignKey('grns.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    supplier_name = Column(String(100), ForeignKey("suppliers.supplier_name"), nullable=False)

    # 1:N relationship between supplier and purchases
    supplier = relationship('Supplier', back_populates='purchase')

    # 1: N relationship between purchases and the association table purchases_stockitems
    items = relationship('PurchaseStockItems', back_populates='purchase')

    def __init__(self, **kwargs):
        """Class constructor
        """
        super().__init__(**kwargs)


class PurchaseStockItems(Base):
    """Association table between  purchases and stockitems"""
    __tablename__ = 'purchases_stockitems'

    quantity = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)

    # Foreign keys to link to stockitems and purchases
    purchase_id = Column(String(100), ForeignKey("purchases.id"), primary_key=True)
    stockitems_id = Column(String(100), ForeignKey("stock_items.id"))

    # Relationship from purchases_stockitems to purchases and stock_items
    purchase = relationship('Purchase', back_populates='items')
    stock_item = relationship('StockItems')



class Supplier(BaseModel, Base):
    """Defines the Supplier class"""
    __tablename__ = 'suppliers'

    account_no = Column(String(100), nullable=False)
    supplier_name = Column(String(100), nullable=False, unique=True)
    contact = Column(String(100), nullable=True)

    # Relationship with Purchase transactions
    purchase= relationship('Purchase', back_populates='supplier')
    dr = Column(Integer, nullable=True)
    cr = Column(Integer, nullable=True)

    # Relationship with GRN
    grns = relationship('GRN', back_populates='supplier')


    def __init__(self, **kwargs):
        """Class constructor
        """
        super().__init__(**kwargs)

# Add an index on the 'supplier_name' column
Index('idx_supplier_name', Supplier.supplier_name)


class StockItems(BaseModel, Base):
    """Defines the Stock items class"""
    __tablename__ = 'stock_items'

    part_no = Column(String(100), nullable=False, unique=True)
    item_name = Column(String(100), nullable=False)
    item_description = Column(String(100), nullable=True)
    base_unit = Column(Enum('pcs', 'dozen', 'bars', 'litres', 'boxes', 'kgs', 'ml'), nullable=False)
    quantity = Column(Integer, nullable=False) 

    def __init__(self, **kwargs):
        """Class constructor
        """
        super().__init__(**kwargs)
