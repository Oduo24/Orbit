#!/usr/bin/python3
"""Defines the db storage methods. ie interacts with the database to create, delete, modify, query objects"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.categories import Category
from models.menu_items import MenuItem
from models.uom import Uom
from models.users import User
from models.orders import Order
from models.waiters import Waiter
from models.payments import Payment
from models.tables import Table
from models.users import User
from models.tender_types import TenderType
from models.base_model import Base

classes = {"Category": Category, "MenuItem":MenuItem, "Uom":Uom, "User":User, "Order":Order,
        "Waiter":Waiter, "Payment":Payment, "Table":Table, "TenderType":TenderType
        }

class DBStorage:
    """Defines a db storage object"""
    __engine = None
    __session = None
    

    def __init__(self):
        """Class constructor, instantiates a DBStorage object
        """
        os.environ['MYSQL_USER'] = 'gerald'
        os.environ['MYSQL_PWD'] = 'ruphinee'
        os.environ['MYSQL_DB'] = 'orbit_db'
        os.environ['MYSQL_HOST'] = 'localhost'


        MYSQL_USER = os.getenv("MYSQL_USER")
        MYSQL_PWD = os.getenv("MYSQL_PWD")
        MYSQL_HOST = os.getenv("MYSQL_HOST")
        MYSQL_DB = os.getenv("MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_DB))


    def all(self, cls):
        """Query the current db session and retrieve all the objects of the class cls
        """
        new_dict = {}
        for clss in classes:
            if cls is classes[clss]:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Adds a new object to the current db session
        """
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current db session
        """
        self.__session.commit()

    def delete(self, obj = None):
        """Deletes an object from the current db session if obj is not none
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the db
        """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()

    def close(self):
        """Closes the current session
        """
        self.__session.remove()

    def get_user(self, cls, email_address):
        """Retrieves a single object of the specified class and column value
        """
        self.reload()
        if cls and email_address:
            #retrieve the user with the email address
            obj = self.__session.query(cls).filter_by(email_address=email_address).first()
            if obj:
                return obj
            return None

    def get_user_session(self, user_id):
        """retrieves the ID of a user
        """
        self.reload()
        user = self.__session.query(User).get(user_id)
        return user
