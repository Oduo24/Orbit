#!/usr/bin/python3
"""Defines all the routes for the delivery view"""

from flask import Blueprint, render_template


delivery_views = Blueprint('delivery_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/delivery')

@delivery_views.route('/', strict_slashes=False)
def get_all_deliveries():
    """returns all the deliveries in the system"""
    return render_template('delivery.html')
