#!/usr/bin/python3
"""This module defines the leder class. Every created ledger is defined by this class"""

from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey, DateTime, Table, Date, Enum
from sqlalchemy.orm import relationship

class Ledger(BaseModel, Base):
    """Defines the Order class"""
    __tablename__ = 'ledgers'

    account_no = Column(String(100), nullable=False)
    ledger_name = Column(String(100), nullable=False, unique=True)
    ledger_opening_amount = Column(Integer, nullable=False)
    group_name = Column(String(100), ForeignKey('ledger_groups.group_name'), nullable=False)
    ledger_group = relationship('LedgerGroup', back_populates='ledgers')
    transactions = relationship('Transaction', secondary='ledgers_transactions', back_populates='ledgers')
    dr = Column(Integer, nullable=True)
    cr = Column(Integer, nullable=True)


    def __init__(self, **kwargs):
        """Class constructor
        """
        super().__init__(**kwargs)


class Transaction(BaseModel, Base):
    __tablename__ = 'transactions'

    date = Column(Date, nullable=False)
    transaction_number = Column(String(100), nullable=True)
    amount = Column(Integer, nullable=False)
    description = Column(String(100), nullable=True)
    transaction_type = Column(Enum('dr', 'cr'), nullable=False)
    ledgers = relationship('Ledger', secondary='ledgers_transactions', back_populates='transactions')

    def __init__(self, **kwargs):
        """Class constructor
        """
        super().__init__(**kwargs)

# Create the association table for ledger_transaction
class LedgerTransaction(Base):
    __tablename__ = 'ledgers_transactions'

    ledger_id = Column(String(100), ForeignKey('ledgers.id'), primary_key=True)
    transaction_id = Column(String(100), ForeignKey('transactions.id'), primary_key=True)
