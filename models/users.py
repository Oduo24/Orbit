#!/usr/bin/python3
"""users module containing the class description of the Customer class"""
from .base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship

# flask-login imports
from flask_login import UserMixin


class User(BaseModel, Base, UserMixin):
    """Defines the User class"""
    __tablename__ = "users"

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email_address = Column(String(100), nullable=False)
    phone_number = Column(Integer, nullable=False)
    password = Column(String(100), nullable=False)
    account_balance = Column(Integer, nullable=True)


    def __init__(self, **kwargs):
        """Initializes a User instance
        """
        super().__init__(**kwargs)
