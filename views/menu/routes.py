#!/usr/bin/python3
"""defines the menu blueprint and the end routes"""

from flask import Blueprint, render_template, requests, flash, url_for

# models imports
from models.menu_items import MenuItem

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

# engine imports
from engine.db_storage import classes, DBStorage


menu_views = Blueprint('menu_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/menu')

@menu_views.route('/', strict_slashes=False)
def insert_new_item():
    """returns a form to enter details of new item"""
    return render_template('new_item.html')

@menu_views.route('/', methods=['POST'], strict_slashes=False)
def insert_new_item_post():
    """Processes the new item form data and stores in the database
    """
    item_name = request.form.get('item_name')
    price = request.form.get('Price')
    category_id = request.form.get('category_id')
    description = request.form.get('description')
    uom_id = request.form.get('uom_id')
    state = request.form.get('state')
    image = request.form.get('image')

    new_item_details = {"item_name":item_name, "price":price, "category_id":category_id, "description":description,
            "uom_id":uom_id, "state":state, "image":image
            }
    new_item_obj = MenuItem(**new_item_details)
    storage.reload()
    storage.new(new_item_obj)
    storage.save()

    flash('Item added successfuly...')
    return redirect(url_for('menu_views.insert_new_item'))
    



