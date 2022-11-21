#!/usr/bin/python3
"""Defines all the routes for the accounts view"""

from flask import Blueprint, render_template


account_views = Blueprint('account_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/account')

@account_views.route('/', strict_slashes=False)
def get_accounts():
    """returns all the customers in the system"""
    return render_template('account.html')
