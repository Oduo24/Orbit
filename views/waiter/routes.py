#!/usr/bin/python3
"""Defines all the routes for the waiter view"""

from flask import Blueprint, render_template


waiter_views = Blueprint('waiter_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/waiter')

@waiter_views.route('/', strict_slashes=False)
def get_all_waiters():
    """returns all the waiters in the system"""
    return render_template('waiter.html')
