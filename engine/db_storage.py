#!/usr/bin/python3
"""Defines the db storage methods. ie interacts with the database to create, delete, modify, query objects"""
import os
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, scoped_session
from models.categories import Category
from models.menu_items import MenuItem
from models.uom import Uom
from models.users import User
from models.orders import Order, order_menuitem
from models.waiters import Waiter
from models.payments import Payment
from models.tables import Table
from models.users import User
from models.tender_types import TenderType
from models.base_model import Base
from models.counters import Counter
from models.unique_number_gen import Unique_number
from models.accounts_models.ledger_groups import LedgerGroup
from models.accounts_models.ledgers import Ledger

classes = {"Category": Category, "MenuItem":MenuItem, "Uom":Uom, "User":User, "Order":Order,
        "Waiter":Waiter, "Payment":Payment, "Table":Table, "TenderType":TenderType, "Counter":Counter, "Unique_number": Unique_number,
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

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(MYSQL_USER, MYSQL_PWD, MYSQL_HOST, MYSQL_DB),
                pool_size=100, max_overflow=0)


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
        self.reload()
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
        self.__session.close()

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

    def get_uom(self, symbol=None):
        """Checks if a uom symbol already exists in the database
        """
        self.reload()
        if symbol:
            #retrieve the uom
            obj = self.__session.query(Uom).filter_by(symbol=symbol).first()
            if obj:
                return obj
            return None
        else:
            # Retrieve all the uoms available in the database and convert to a list object
            # that does not contain tuples
            obj = [uom.symbol for uom in self.__session.query(Uom.symbol)]
            return obj


    def get_category(self, category_name=None):
        """Checks if a category already exists in the database
        """
        self.reload()
        if category_name:
            # Retrieve the category
            obj = self.__session.query(Category).filter_by(category_name=category_name).first()
            if obj:
                return obj
            return None
        else:
            # Retrieve all the category names available
            obj = [category.category_name for category in self.__session.query(Category.category_name)]
            return obj


    def get_menu_item_by_category_id(self, category_id=None):
        """Checks if an item already exists in the database
        """
        self.reload()
        if category_id:
            #retrieve the items belonging to the passed category_id
            obj = self.__session.query(MenuItem).filter_by(category_id=category_id).all()
            if obj:
                return obj
            return None

    def get_menu_item(self, item_name=None):
        """Checks if an item already exists in the database
        """
        self.reload()
        if item_name:
            #retrieve the item
            obj = self.__session.query(MenuItem).filter_by(item_name=item_name).first()
            if obj:
                return obj
            return None
        else:
            # Retrieve all the menu items in the database
            obj = self.__session.query(MenuItem).all()
            return obj

    def get_inactive_menu_items(self):
        """Retrieves all the inactive menu_items
        """
        self.reload()
        obj = self.__session.query(MenuItem).filter_by(state='Inactive').all()
        if obj:
            return obj
        else:
            return None

    def get_budget_menu_search(self, amount):
        """Retrieves the menu items where the price is <= amount
        """
        self.reload()
        if amount:
            obj = self.__session.query(MenuItem).filter(MenuItem.price <= amount).all()
            if obj:
                return obj
            return None

    def check_table_if_exists(self, table_name=None):
        """Checks if the table name supplied already exists
        """
        self.reload()
        if table_name:
            obj = self.__session.query(Table).filter_by(table_name=table_name).first()
            if obj:
                return obj
            return None

    def get_all_tables(self):
        """Returns all the tables in the sytem
        """
        self.reload()
        obj = self.__session.query(Table).all()
        if obj:
            return obj
        return None

    def get_all_waiters(self):
        """Retrieves all the waiters in the database
        """
        self.reload()
        obj = self.__session.query(Waiter).all()
        if obj:
            return obj
        return None


    def get_counters(self):
        """retrieve all the counter instances in the database
        """
        self.reload()
        # Retrieve all the menu items in the database
        obj = [counter.counter_name for counter in self.__session.query(Counter.counter_name)]
        if obj:
            return obj
        return None

    def get_tender_types(self):
        """retrieve all tender_types instances in the database
        """
        self.reload()
        # Retrieve all the tender types in the database
        obj = [tender.tender_name for tender in self.__session.query(TenderType.tender_name)]
        if obj:
            return obj
        return None

    def get_unique_number(self, name):
        """Retrieves the current unique number stored of the type (name) from the db
        """
        unique_number = self.__session.query(Unique_number).filter_by(name=name).first()
        return unique_number

    def get_all_orders(self):
        """Retrieves all the orders in the database
        """
        obj = self.__session.query(Order).all()
        if obj:
            return obj
        return None

    def update_order_number(self, new_order_number):
        """ Increments unique order number
        """
        self.reload()
        self.__session.query(Unique_number).filter(Unique_number.name == "orders").update({Unique_number.number: new_order_number})
        self.save()
        return None

    def create_order_item_inst(self, order_number, item, quantity, amount):
        """ Creates an instance of order item
        """
        item_inst = order_menuitem.insert().values(
                    item_name = item,
                    order_number = order_number,
                    quantity = quantity,
                    amount = amount
                )
        conn = self.__engine.connect()
        conn.execute(item_inst)
        conn.close()
        return None

    def get_unserved_orders(self):
        """Returns all unserved orders if there is none returns None
        """
        unserved_orders = self.__session.query(Order).filter(Order.isPaid == "False").order_by(Order.created_at.desc()).all()
       
       # changing the date format to dd/mm/yyyy
        for order in unserved_orders:
            order.created_at = order.created_at.strftime('%d/%m/%Y')

        if unserved_orders:
            return unserved_orders
        return None

    def get_order_items(self, data):
        """Retrieves all the items in the table 'order_menuitem' that belong to the order number 'data'
        """
        order_items = select([order_menuitem]).where(order_menuitem.c.order_number == data)

        # Create a connection
        conn = self.__engine.connect()
        result = conn.execute(order_items)
        return result

    def modify_order_status(self, order_number):
        """Check and modify order status where necessary
        """
        self.reload()
        order_to_update = self.__session.query(Order).filter_by(order_number=order_number).first()
        if order_to_update:
            order_to_update.is_served = 1
            self.save()
            self.close()
            return 1
        return 0
        

