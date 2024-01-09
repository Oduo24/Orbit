#!/usr/bin/python3
"""Defines all the routes for the kitchen order ticket(kot) view"""

from flask import Blueprint, render_template, request, flash, url_for, redirect, jsonify
import requests
from models.orders import Order
from models.orders import order_menuitem
# sqlalchemy imports
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship


# base_model imports
from models.base_model import BaseModel, Base, time
from models import storage

#from models.orders import Order

# engine imports
from engine.db_storage import classes, DBStorage


kot_views = Blueprint('kot_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/kot')

@kot_views.route('/', strict_slashes=False)
def get_all_kot():
    """Retrieve all the orders in the database that have not been served
    """
    try:
        orders = storage.get_unserved_orders()
        number_of_orders = len(orders)

    except Exception as e:
        print(e)
        storage.rollback()
        storage.close()
        return render_template('kot.html',)

    return render_template('kot.html', orders=orders, number_of_orders=number_of_orders)

@kot_views.route('/order-details', methods=["GET", "POST"], strict_slashes=False)
def get_order_items():
    """Retrieves all the items from the order_menuitem table for the order number
    """
    if request.method == "POST":
        data = int(request.get_json())

        # Select all the items that belong to the order number 'data'
        try:
            order_items = storage.get_order_items(data)
            items_list = []
            for row in order_items:
                items_list.append(row[order_menuitem.c.item_name])
                items_list.append(row[order_menuitem.c.quantity])
                items_list.append(row[order_menuitem.c.amount])

            return jsonify(items_list)
        except Exception as e:
            storage.rollback()
            storage.close()
            return render_template('kot.html',)

@kot_views.route('/order-status', methods=["GET", "POST"], strict_slashes=False)
def check_modify_order_status():
    """Sets the order status to 1(Served)
    """
    if request.method == "POST":
        order_number = int(request.get_json()['order_number'])
        status = storage.modify_order_status(order_number)

        if status == 1:
            return jsonify("Order status Changed to Served...")
        else:
            return jsonify("Order status Not changed...")
        

    #return jsonify('This is the order number {}'.format(order_number))
