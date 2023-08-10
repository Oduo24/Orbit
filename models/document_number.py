#!/usr/bin/python3
"""This module describes the class for document number generation"""
from .base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer

class DocumentNumber(Base):
    __tablename__ = 'document_numbers'

    last_number = Column(Integer, default=0, primary_key=True)
