#!/usr/bin/python3
"""Entry point into the flask application"""

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
from models.payments import Payment
from models.orders import Order
from models.waiters import Waiter
from models.tables import Table
from models.tender_types import TenderType
from models.users import User

"""flask imports"""
from flask import Flask

"""Importing the blueprints defined in views"""
from views.standard.routes import standard_views
from views.menu.routes import menu_views
from views.user.routes import user_views
from views.auth.routes import auth_views
from views.order.routes import order_views
from views.kot.routes import kot_views
from views.accounting.routes import account_views
from views.delivery.routes import delivery_views
from views.waiter.routes import waiter_views

# Handling login imports
from flask_login import LoginManager



"""Creating an app instance"""
app = Flask(__name__)

# secret key for session
app.secret_key = "1234567890qwertyuiopasdfghjklzxcvbnm"


"""Registering blueprints"""
app.register_blueprint(standard_views)
app.register_blueprint(menu_views)
app.register_blueprint(user_views)
app.register_blueprint(auth_views)
app.register_blueprint(order_views)
app.register_blueprint(kot_views)
app.register_blueprint(account_views)
app.register_blueprint(delivery_views)
app.register_blueprint(waiter_views)

# Initializing the db
# storage.reload()
# storage.save()

# Initializing login_manager
login_manager = LoginManager()
login_manager.login_view = 'auth_views.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    """since the user_id is just the primary key of our user table, we use it in the query for the user
    """
    return storage.get_user_session(user_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

    
