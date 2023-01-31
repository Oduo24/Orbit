#!/usr/bin/python3
"""Defines all the routes for the order view"""

from flask import Blueprint, render_template, request, flash, url_for, redirect, jsonify

# Threading imports
import threading
import queue
import requests
import time

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
from models.orders import Order

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
    all_orders = storage.get_all_orders()
    if all_orders:
        number_of_orders = len(all_orders)
        return render_template('order.html', all_orders=all_orders, number_of_orders=number_of_orders)

@order_views.route('/counter-order', methods=['GET','POST'], strict_slashes=False)
def make_counter_order():
    if request.method == 'POST':
        # Process order data
        data = request.get_json()

        # Store the order in the db
        order_number = storage.get_unique_number("orders").number

        order_details = {"order_number": order_number, 
                        "customer": data["customer"],
                        "waiter": data["waiter"],
                        "table": data["table"],
                        "counter": data["counter"],
                        "tender": data["tender"],
                        "total": data["total"],
                        "isPaid": "False",
                        }

        # Increment the order number and save to the db
        new_number = order_number + 1
        storage.update_order_number(new_number)

        # If tender type is CASH save to the db
        if data["tender"] == "CASH":
            order_obj = Order(**order_details)
            storage.new(order_obj)
            storage.save()

            # Call the function that saves the order items to the db pass it the data object and order number
            save_order_items(data, order_number)

            # respond with a list of order number and the tender type
            response = [order_details["order_number"], "CASH"]
            return jsonify(response)
        
        else: #data["tender"] == "MPESA":
            q = queue.Queue()
            phone_number = data["customer"]

            # Create a thread
            mpesa_transaction_check = threading.Thread(target=process_mpesa_payment, args=(q, phone_number,))
            
            # Start the thread
            mpesa_transaction_check.start()

            #wait for the response
            mpesa_check_response = q.get()

            if mpesa_check_response == "Success":
                #response = "Transaction for number {} of amount {} found".format(data["customer"], data["total"])
                
                order_obj = Order(**order_details)
                storage.new(order_obj)
                storage.save()
                # Call the function that saves the order items to the db and pass it the data object and order number
                save_order_items(data, order_number)

                # respond with a list of order number and the tender type
                response = [order_details["order_number"], "MPESA"]
                return jsonify(response)

            else:
                return "Failed"
    
    else:
        # get all the tables
        all_tables = storage.get_all_tables()
        number_of_tables = len(all_tables)
        all_waiters = storage.get_all_waiters()
        number_of_waiters = len(all_waiters)

        all_tender_types = storage.get_tender_types()
        number_of_tender_types = len(all_tender_types)

        all_items = storage.get_menu_item()

        return render_template('make_counter_order.html', all_items=all_items,
                all_waiters=all_waiters,
                number_of_waiters=number_of_waiters,
                all_tables=all_tables,
                number_of_tables=number_of_tables,
                all_tender_types=all_tender_types,
                number_of_tender_types=number_of_tender_types
                )

def process_mpesa_payment(q, number):
    """ Processes the MPESA by checking if the combination of number, and total amount is in the mpesa transactions db table
    """
    # if the transaction is in the db respond with a success else failed
    ###
    ###
    import time
    # Sleep for 5 seconds
    time.sleep(5)
    
    # Put the response in the queue
    q.put("Success")

def save_order_items(data, order_number):
    """ Saves the order items to the database, takes thwo params: data that contains 
    the details of the items. order_number: the order number related to the items
    """
    item_names = data["items"]
    quantities = data["quantities"]
    amounts = data["amounts"]

    for item in item_names:
        quantity = quantities[item_names.index(item)]
        amount = amounts[item_names.index(item)]

        # Create an instance of an order item
        storage.create_order_item_inst(order_number, item, quantity, amount)

