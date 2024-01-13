#!/usr/bin/python3
"""Defines all the routes for the sales view"""

from flask import Blueprint, render_template, request, flash, url_for, redirect, jsonify

import threading
import queue
import sys
# models imports
from models.customers import Customer
from models.purchases import StockItems
from models.accounts_models.accounts import CreditSaleTransaction, CreditSaleTransactionStockItems

# python imports


# sqlalchemy imports
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import String, Column, Integer
from sqlalchemy.exc import IntegrityError
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

        try:
            storage.reload()
            stock_item = storage.get_stock_item_by_id(StockItems, item_name['itemName']) # Gets item by name and not ID
            storage.close()
        except Exception as e:
            return jsonify({"error": "Server error: Could not retrieve data from the database"}), 500
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
        data = request.get_json()

        try:
            storage.reload()
            # Generate sales invoice document number
            sales_invoice_no = storage.generate_document_number('SINV')

            cleaned_data = validate_items(data)
            # Retrieve customer
            customer = storage.get_customer_by_name(cleaned_data["customer"])
            # Retrieve related accounts
            sales_account = storage.get_account("Credit Sales")
            accounts_receivable = storage.get_account("Receivables")

            # Create sales invoice
            sales_inv_details = { "transaction_number": sales_invoice_no,
                            "amount": cleaned_data["total"],
                            "customer_id": customer.id,
                            "narration": cleaned_data["narration"],
                            "dr": accounts_receivable.id,
                            "cr": sales_account.id
                            }
            # New credit sale transaction object
            new_credit_sale_transaction = CreditSaleTransaction(**sales_inv_details)
            # append the accounts related to this transaction
            new_credit_sale_transaction.accounts.append(sales_account)
            new_credit_sale_transaction.accounts.append(accounts_receivable)

            items_list = []
            for item in cleaned_data["items"]:
                inv_item_details = {}
                # Get id of the particular item
                stockItem = storage.get_stock_item_by_id(StockItems, item["name"])
                
                # Add to the dictionary with item details
                inv_item_details["quantity"] = int(item["quantity"])
                inv_item_details["amount"] = int(item["amount"])
                inv_item_details["transaction_number"] = new_credit_sale_transaction.transaction_number
                inv_item_details["stock_item_id"] = stockItem.id
                
                inv_item_obj = CreditSaleTransactionStockItems(**inv_item_details)
                items_list.append(inv_item_obj)

                # Decreament the stock quantity of each item
                stockItem.quantity -= int(inv_item_details["quantity"])
                storage.new_modified(stockItem)

                # Update the customer balance amount
                customer.balance += cleaned_data["total"]
                storage.new_modified(customer)


            new_credit_sale_transaction.stock_items.extend(items_list)
            storage.new_modified(new_credit_sale_transaction)
            storage.save()

        except IntegrityError as ie:
            storage.rollback()
            storage.close()
            return jsonify({"error": "Possible duplicate entry of item name."}), 500
        storage.close()
        return jsonify(f"SUCCESS>\nInvoice No. {sales_invoice_no} saved."), 200

    else:
        storage.reload() # Get a sesssion
        #price_lists = 
        customers = storage.get_all_objects(Customer)
        stock_items = storage.get_all_objects(StockItems)
        storage.save()
        storage.close() # Close the sesssion
        return render_template('credit_sale.html', customers=customers, stock_items=stock_items)
    

def validate_items(data):
    """Function calculates the total per item and quantity and the overal total
    """
    total = 0
    for item in data["items"]:
        item["amount"] = int(item["quantity"]) * int(item["rate"])
        total = total + int(item["amount"])
    data["total"] = total
    return data
