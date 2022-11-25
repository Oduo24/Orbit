#!/usr/bin/python3
"""Defines all the routes for the waiter view"""

from flask import Blueprint, render_template, request, flash, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash


# models imports
from models.waiters import Waiter

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

# model imports
from models.waiters import Waiter

# engine imports
from engine.db_storage import classes, DBStorage

# define waiter_views template
waiter_views = Blueprint('waiter_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/waiter')

@waiter_views.route('/', strict_slashes=False)
def get_all_waiters():
    """returns all the waiters in the system
    """
    all_waiters = storage.get_all_waiters()
    if all_waiters:
        number_of_waiters = len(all_waiters)
    else:
        number_of_waiters = 0
    return render_template('waiter.html', all_waiters=all_waiters, number_of_waiters=number_of_waiters)

@waiter_views.route('/add-waiter', methods=['POST'], strict_slashes=False)
def add_new_waiter():
    """Adds a new waiter into the system
    """
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email_address = request.form.get('email_address')
        phone_number = request.form.get('phone_number')
        passcode = request.form.get('passcode')

        waiter_details = {"first_name":first_name, "last_name":last_name, "email_address":email_address, "phone_number":phone_number,
                "passcode":generate_password_hash(passcode, method='sha256')
                }
        waiter_obj = Waiter(**waiter_details)
        storage.new(waiter_obj)
        storage.save()
        
        flash('New waiter added successfuly...')
        return redirect(url_for('waiter_views.get_all_waiters'))

