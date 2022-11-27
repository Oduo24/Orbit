#!/usr/bin/python3
"""Defines all the routes for the order view"""

from flask import Blueprint, render_template, request, flash, url_for, redirect

# models imports
from models.menu_items import MenuItem
from models.orders import Order

# python imports
from datetime import datetime
import uuid
import os

# sqlalchemy imports
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship


# base_model imports
from models.base_model import BaseModel, Base, time
from models import storage
from models.categories import Category

# engine imports
from engine.db_storage import classes, DBStorage

# define the order_views template
order_views = Blueprint('order_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/order')

@order_views.route('/all-orders', strict_slashes=False)
def get_all_orders():
    """returns all the orders in the system"""
    return render_template('order.html')

@order_views.route('/counter-order', methods=['GET','POST'], strict_slashes=False)
def make_counter_order():
    if request.method == 'POST':
        # Process order data
        pass

    all_items = storage.get_menu_item()

    return render_template('make_counter_order.html', all_items=all_items)



