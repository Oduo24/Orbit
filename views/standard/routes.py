#!/usr/bin/python3
"""Describes all the routes for the index view"""

from flask import Blueprint, render_template


standard_views = Blueprint('standard_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/')

@standard_views.route('/', strict_slashes=False)
def index():
    """returns the index page"""
    return render_template('index.html')


@standard_views.app_errorhandler(404)
def not_found(e):
    """Returns the 404-not found page"""
    return render_template('404.html', error = e.code)
