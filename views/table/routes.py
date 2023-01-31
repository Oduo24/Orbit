#!/usr/bin/python3
"""Defines all the routes for the waiter view"""

from flask import Blueprint, render_template, request, flash, url_for, redirect

# models imports
from models.tables import Table

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
from models.tables import Table

# engine imports
from engine.db_storage import classes, DBStorage

# define table_views blueprint
table_views = Blueprint('table_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/table')

@table_views.route('/all-tables', methods=['GET','POST'], strict_slashes=False)
def get_all_tables():
    """returns all the tables in the system
    """
    all_tables = storage.get_all_tables()
    print(all_tables)
    number_of_tables = len(all_tables)
    return render_template('table.html', all_tables=all_tables, number_of_tables=number_of_tables)

@table_views.route('/add-table', methods=['GET', 'POST'], strict_slashes=False)
def add_table():
    """Adds a new table to the database
    """
    if request.method == 'POST':
        table_name = request.form.get('table_name')
        capacity = request.form.get('capacity')
        location = request.form.get('location')

        table = storage.check_table_if_exists(table_name)
        if table:
            flash('Table with the name {} already exists'.format(table.table_name))
            return redirect(url_for('table_views.get_all_tables'))
        else:
            table_details = {"table_name":table_name, "capacity":capacity, "location":location}
            table_obj = Table(**table_details)
            storage.new(table_obj)
            storage.save()

            flash('Table added successfuly...')
            return redirect(url_for('table_views.get_all_tables'))

    else:
        return render_template('new_table.html')

