#!/usr/bin/python3
"""Defines all the routes for the sales view"""

from flask import Blueprint, render_template, request, flash, url_for, redirect, jsonify

# models imports
from models.customers import Customer
from models.purchases import StockItems
from models.accounts_models.accounts import Receipt


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
receipt_views = Blueprint('receipt_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/receipt')

@receipt_views.route('/new_receipt', methods=['GET','POST'], strict_slashes=False)
def receive_payment():
    if request.method == 'POST':
        try:
            storage.reload()
            receipt_details = request.get_json()
            dr_account_id = storage.get_account(receipt_details["paid_to_account"]).id

            generated_receipts = []
            for individual_receipt in receipt_details["individualReceipts"]:
                receipt_no = storage.generate_document_number("RCT")
                generated_receipts.append(receipt_no)
                customer = storage.get_customer_by_name(individual_receipt["customer"])
                cr_account_id = storage.get_account('Receivables').id
                receiptObj = {
                    "receipt_number": receipt_no,
                    "amount": individual_receipt["receipt_amount"],
                    "remark": individual_receipt["remarks"],
                    "dr_account_id": dr_account_id,
                    "cr_account_id": cr_account_id
                }
                new_receipt = Receipt(**receiptObj)
                new_receipt.customer = customer
                storage.save()
            return jsonify(generated_receipts), 200

        except Exception as e:
            storage.rollback()
            return jsonify({"error": "Error saving receipt information"}), 500
        finally:
            storage.close()

    else:
        customers = storage.get_all_objects(Customer)
        accounts = storage.get_all_paying_accounts()
        return render_template('receipt.html', customers=customers, accounts=accounts)
    

       