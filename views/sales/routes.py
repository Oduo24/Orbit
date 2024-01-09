#!/usr/bin/python3
"""Defines all the routes for the sales view"""

from flask import Blueprint, render_template, request, flash, url_for, redirect, jsonify

import threading
import queue

# models imports
from models.customers import Customer
from models.purchases import StockItems

# python imports


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

# define the sales_views template
sales_views = Blueprint('sales_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/sales')

@sales_views.route('/item_details', methods=['GET','POST'], strict_slashes=False)
def get_stock_item_details():
    if request.method == 'POST':
        item_name = request.get_json()
        storage.reload()
        stock_item = storage.get_stock_item_by_id(StockItems, item_name['itemName']) # Gets item by name and not ID
        print(stock_item)
        storage.close()
        item_details = {
            'part_no': stock_item.part_no,
            'item_name': stock_item.item_name,
            'base_unit': stock_item.base_unit,
            'quantity': stock_item.quantity,
            'rate': stock_item.rate
        }
        return jsonify(item_details), 200
        
    
    
@sales_views.route('/sale', methods=['GET','POST'], strict_slashes=False)
def make_credit_sale():
    if request.method == 'POST':
        pass
    
        """
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
    """
    else:
        
        storage.reload() # Get a sesssion
        #price_lists = 
        customers = storage.get_all_objects(Customer)
        stock_items = storage.get_all_objects(StockItems)
        storage.save()
        storage.close() # Close the sesssion
        return render_template('credit_sale.html', customers=customers, stock_items=stock_items)

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

