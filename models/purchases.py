#!/usr/bin/python3
"""This module defines the leder class. Every created ledger is defined by this class"""

from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey, DateTime, Table, Date, Enum, Index, Boolean
from sqlalchemy.orm import relationship


class GRN(BaseModel, Base):
    """Defines the GRN class"""
    __tablename__ = 'grns'
    
    grn_no = Column(String(100), nullable=False)
    amount = Column(Integer, nullable=False)
    supplier_name = Column(String(100), ForeignKey("suppliers.supplier_name"), nullable=False)
    reference_no = Column(String(100), default=0, nullable=False)
    is_invoiced = Column(Boolean, default=False)

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
    rate = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)

    # Foreign keys to link to grns and stock_items table
    grn_id = Column(String(100), ForeignKey('grns.id'), primary_key=True)
    stock_item_id = Column(String(100), ForeignKey("stock_items.id"), primary_key=True)
    
    # Relationship from grn_stockitems to grn
    grn = relationship('GRN', back_populates='items')
    # Relationship from grn_stockitems to stock_items
    stock_item = relationship('StockItems')




class PurchaseInvoice(BaseModel, Base):
    """Defines the Purchase invoice class"""
    __tablename__ = 'purchase_invoice'

    invoice_no = Column(String(100), nullable=False)
    supplier_invoice_date = Column(Date)
    grn_no = Column(String(100), ForeignKey('grns.id'), unique=True, nullable=False)
    supplier_name = Column(String(100), ForeignKey('suppliers.supplier_name'), nullable=False)
    reference_no = Column(String(100), default=0, nullable=False)
    narration = Column(String(250), nullable=True)

    supplier = relationship('Supplier', back_populates='purchase_invoices')

    def __init__(self, **kwargs):
        """Class constructor
        """
        super().__init__(**kwargs)




class Supplier(BaseModel, Base):
    """Defines the Supplier class"""
    __tablename__ = 'suppliers'

    account_no = Column(String(100), nullable=False)
    supplier_name = Column(String(100), nullable=False, unique=True)
    contact = Column(String(100), nullable=True)

    dr = Column(Integer, nullable=True)
    cr = Column(Integer, nullable=True)

    # Relationship with Purchase invoice transactions
    purchase_invoices = relationship('PurchaseInvoice', back_populates='supplier')

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
