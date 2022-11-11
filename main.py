#!/usr/bin/python3
"""Entry pooint into the application"""

"""python imports"""
from datetime import datetime
import uuid
import os

"""sqlalchemy imports"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship

"""base_model imports"""
from models.base_model import BaseModel, Base, time
from models import storage

"""engine imports"""
from engine.db_storage import classes, DBStorage

"""models"""
from models.categories import Category
from models.menu_items import MenuItem
from models.uom import Uom
from models.customers import Customer
from models.payments import Payment
from models.orders import Order
from models.waiters import Waiter
from models.tables import Table
from models.tender_types import TenderType

if __name__ == '__main__':
    first_category = Category()
    print(first_category.to_dict())
    storage.reload()
    storage.save()
    
