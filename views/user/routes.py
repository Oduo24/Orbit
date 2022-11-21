#!/usr/bin/python3
"""Defines all the routes for the user view"""

from flask import Blueprint, render_template


user_views = Blueprint('user_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/users')

@user_views.route('/', strict_slashes=False)
def get_all_users():
    """returns all the customers in the system"""
    return render_template('user.html')
