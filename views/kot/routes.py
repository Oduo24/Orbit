#!/usr/bin/python3
"""Defines all the routes for the kitchen order ticket(kot) view"""

from flask import Blueprint, render_template


kot_views = Blueprint('kot_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/kot')

@kot_views.route('/', strict_slashes=False)
def get_all_kot():
    """returns all the kot in the kitchen counter"""
    return render_template('kot.html')
