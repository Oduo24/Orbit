#!/usr/bin/python3
"""Defines all the routes for the order view"""

from flask import Blueprint, render_template


order_views = Blueprint('order_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/order')

@order_views.route('/', strict_slashes=False)
def get_all_orders():
    """returns all the orders in the system"""
    return render_template('order.html')
