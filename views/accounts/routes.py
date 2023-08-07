#!/usr/bin/python3
"""Defines all the routes for the accounts view"""

from flask import Blueprint, render_template, request, flash, url_for, redirect, jsonify

from sqlalchemy.exc import IntegrityError

from models.accounts_models.ledger_groups import LedgerGroup
from models.accounts_models.ledgers import Ledger

from models import storage

# defining the accounts_views blueprint
accounts_views = Blueprint('accounts_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/accounts')


@accounts_views.route('/ledgerMaster', strict_slashes=False)
def master_ledger():
    """Returns the ledger mother template"""
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
    return render_template('ledger.html')

@accounts_views.route('/addNewLedger', methods=['POST',], strict_slashes=False)
def new_ledger():
    """Adds a new ledger to the database
    """
    if request.method == 'POST':
        ledger_details = request.get_json()

        # Call the function that sets the dr/cr values
        ledger_details = setting_dr_cr(ledger_details)

        # Creating the ledger object
        ledger_object = Ledger(**ledger_details)

        # Saving the ledger to the database
        try:
            storage.new(ledger_object)
            storage.save()
        except IntegrityError:
            return jsonify("ledger name already exists in the system")
        except Exception as e:
            return jsonify("Unknown Exception occured")
        else:
            return jsonify("New ledger added successfully")

def setting_dr_cr(ledger_details):
    """
    Helper function to set the dr or cr value
    """
    if ledger_details["drcr"] == "dr":
        ledger_details["dr"] = ledger_details["ledger_opening_amount"]
        ledger_details["cr"] = 0
    else:
        ledger_details["cr"] = ledger_details["ledger_opening_amount"]
        ledger_details["dr"] = 0
    del ledger_details["drcr"]
    return ledger_details



