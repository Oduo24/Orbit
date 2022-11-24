#!/usr/bin/python3
"""Defines all the routes for the waiter view"""

from flask import Blueprint, render_template


table_views = Blueprint('table_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/table')

@table_views.route('/all-tables', strict_slashes=False)
def get_all_tables():
    """returns all the tables in the system"""
    return render_template('table.html')

