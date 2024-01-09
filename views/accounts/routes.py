#!/usr/bin/python3
"""Defines all the routes for the accounts view"""

from flask import Blueprint, render_template, request, flash, url_for, redirect, jsonify

from sqlalchemy.exc import IntegrityError

from datetime import datetime

from models.accounts_models.accounts_group import AccountGroup
from models.accounts_models.accounts import Account, Transaction
from models.purchases import Supplier
from models import storage

# defining the accounts_views blueprint
accounts_views = Blueprint('accounts_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/accounts')


@accounts_views.route('/AccountMaster', strict_slashes=False)
def master_account():
    """Returns the Account mother template"""
    """
    group_name = "testGroup2"
        description = "test"
        nature_of_group = "asset"

        new_group_dict = {"group_name": group_name, "description": description, "nature_of_group": nature_of_group}

        new_group = LedgerGroup(**new_group_dict)
        account_storage.new(new_group)
        account_storage.save()

        print(new_group)
        return "SUccess..."
    """
    return render_template('accounts.html')

@accounts_views.route('/addNewAccount', methods=['POST',], strict_slashes=False)
def new_account(): #means new_account
    """Adds a new account to the database
    """
    if request.method == 'POST':
        account_details = request.get_json()

        # Call the function that sets the dr/cr values
        account_details = setting_dr_cr(account_details)

        # Creating the Account object
        account_object = Account(**account_details)

        # Saving the account to the database
        try:
            storage.new(account_object)
            storage.save()
            storage.close()
        except IntegrityError as e:
            return jsonify("Account name already exists in the system")
        except Exception as e:
            return jsonify("Unknown Exception occured")
        else:
            return jsonify("New account added successfully")

def setting_dr_cr(account_details):
    """
    Helper function to set the dr or cr value
    """
    if account_details["drcr"] == "dr":
        account_details["dr"] = account_details["account_opening_amount"]
        account_details["cr"] = 0
    else:
        account_details["cr"] = account_details["account_opening_amount"]
        account_details["dr"] = 0
    del account_details["drcr"]
    return account_details


@accounts_views.route('/last_payment_info', methods=['POST', 'GET'], strict_slashes=False)
def last_payment_info():
    """Get the details of last payment made"""
    if request.method == 'POST':
        supplier_and_account = request.get_json()

        # Get last payment
        storage.reload()
        last_payment = storage.get_last_payment(supplier_and_account["supplier"])
        balance = storage.get_supplier(supplier_and_account["supplier"]).balance

        if last_payment:
            # Return last payment details
            last_payment_details = {
                "date": last_payment.created_at.strftime("%d/%m/%Y"),
                "balance": balance
            }
            result = jsonify(last_payment_details)
            storage.save()
            storage.close()
            return result, 200
        else:
            last_payment_details = {
                    "date": 0,
                    "balance": 0
            }
            result = jsonify(last_payment_details)
            storage.save()
            storage.close()
            return result, 200
        

@accounts_views.route('/pay', methods=['POST', 'GET'], strict_slashes=False)
def payment():
    if request.method == 'POST':
        try:
            payment_details = request.get_json()
            payment_no = storage.generate_document_number("PAY")
            # Handle the transaction. Credit the paying account and debit the accounts payable
            storage.reload()
            paying_account = storage.get_account(payment_details["payingAccount"])
            payables_account = storage.get_account("Payables")

            transaction_details = {
                        "supplier": payment_details["supplier"],
                        "transaction_number": payment_no,
                        "amount": payment_details["amountPaid"],
                        "dr": payables_account.id,
                        "cr": paying_account.id,
                        }
            
            new_transaction = Transaction(**transaction_details)

            # append the accounts related to this transaction
            new_transaction.accounts.append(paying_account)
            new_transaction.accounts.append(payables_account)
            storage.new_modified(new_transaction)

            # update the supplier account balance
            supplier = storage.get_supplier(payment_details["supplier"])
            supplier.balance = supplier.balance - int(payment_details["amountPaid"])
            storage.new_modified(supplier)   
        except Exception as e:
            storage.rollback()
            storage.close()
            return jsonify({"error": f"Could not create a new payment. \n {e}"}), 500
        
        storage.save()
        storage.close()
        return jsonify(f"SUCCESS. \n Payment number {payment_no} created."), 200
    
    #payment_voucher_number = storage.generate_document_number('PAY')
    suppliers = storage.get_all_objects(Supplier)
    paying_accounts = storage.get_all_paying_accounts()

    return render_template('payment.html',
                           suppliers=suppliers,
                           paying_accounts=paying_accounts
                           )


