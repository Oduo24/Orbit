#!/usr/bin/python3
"""This module defines the Account class. Every created account is defined by this class"""

from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey, DateTime, Table, Date, Enum, Index, Boolean
from sqlalchemy.orm import relationship

class Account(BaseModel, Base):
    """Defines the Account class"""
    __tablename__ = 'accounts'

    account_no = Column(String(100), nullable=False)
    account_name = Column(String(100), nullable=False, unique=True)
    account_opening_amount = Column(Integer, nullable=False)
    group_name = Column(String(100), ForeignKey('account_groups.group_name'), nullable=False)
    account_group = relationship('AccountGroup', back_populates='accounts')
    transactions = relationship('Transaction', secondary='accounts_transactions', back_populates='accounts')
    credit_sale_trns = relationship('CreditSaleTransaction', secondary='accounts_credit_sale_transactions', back_populates='accounts')
    dr = Column(Integer, nullable=True)
    cr = Column(Integer, nullable=True)

    def __init__(self, **kwargs):
        """Class constructor
        """
        super().__init__(**kwargs)


class Transaction(BaseModel, Base):
    """Defines purchase transaction class"""
    __tablename__ = 'transactions'

    supplier = Column(String(100), ForeignKey('suppliers.supplier_name'), nullable=False)
    transaction_number = Column(String(100), nullable=True)
    amount = Column(Integer, nullable=False)
    description = Column(String(100), nullable=True)
    dr = Column(String(100), ForeignKey('accounts.id'), nullable=True)
    cr = Column(String(100), ForeignKey('accounts.id'), nullable=True)
    accounts = relationship('Account', secondary='accounts_transactions', back_populates='transactions')

    def __init__(self, **kwargs):
        """Class constructor
        """
        super().__init__(**kwargs)

# Create the association table for account_transaction
class AccountTransaction(Base):
    __tablename__ = 'accounts_transactions'

    account_id = Column(String(100), ForeignKey('accounts.id'), primary_key=True)
    transaction_id = Column(String(100), ForeignKey('transactions.id'), primary_key=True)


##################################### CREDIT SALES ################################################
class CreditSaleTransaction(BaseModel, Base):
    """Defines credit sales transaction class"""
    __tablename__ = 'credit_sale_transactions'

    customer_id = Column(String(100), ForeignKey('customers.id'), nullable=False)
    transaction_number = Column(String(100), primary_key=True, nullable=False)
    amount = Column(Integer, nullable=False)
    narration = Column(String(100), nullable=True)
    isPaid = Column(Boolean, default=False)
    dr = Column(String(100), ForeignKey('accounts.id'), nullable=True)
    cr = Column(String(100), ForeignKey('accounts.id'), nullable=True)
    accounts = relationship('Account', secondary='accounts_credit_sale_transactions', back_populates='credit_sale_trns')
    stock_items = relationship('StockItems', secondary='credit_sale_transaction_stock_items', backref='credit_sale_transaction')


    def __init__(self, **kwargs):
        """Class constructor
        """
        super().__init__(**kwargs)


# Add an index on the 'transaction_number' column
Index('idx_transaction_number', CreditSaleTransaction.transaction_number)

# Create the association table between accounts and credit_sale_transactions
class AccountCreditSaleTransaction(Base):
    __tablename__ = 'accounts_credit_sale_transactions'

    account_id = Column(String(100), ForeignKey('accounts.id'), primary_key=True)
    transaction_id = Column(String(100), ForeignKey('credit_sale_transactions.id'), primary_key=True)


# StockItem and CreditSaleTransaction assosciation table
credit_sale_transaction_stock_items = Table("credit_sale_transaction_stock_items", Base.metadata,
        Column('item_name', String(100), ForeignKey('stock_items.item_name'), primary_key=True),
        Column('transaction_number', String(100), ForeignKey('credit_sale_transactions.transaction_number'), nullable=False, primary_key=True),
        Column('quantity', Integer, nullable=False),
        Column('amount', Integer, nullable=False))

