#!/usr/bin/python3
"""defines the menu blueprint and the end routes"""

from flask import Blueprint, render_template, request, flash, url_for, redirect

# models imports


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


counter_views = Blueprint('counter_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/counter')

@counter_views.route('/counters', strict_slashes=False)
def all_counters():
    """Returns all the counters in the system
    """
    all_counters = storage.get_counters()
    number_of_counters = len(all_counters)
    
    return render_template('setup.html', all_counters=all_counters,
            number_of_counters = number_of_counters)

