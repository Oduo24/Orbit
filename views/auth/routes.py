#!/usr/bin/python3
"""This module defines all the authentication routes for the app"""

from flask import Blueprint, render_template, url_for, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

"""Models"""
from models.users import User

"""python imports"""
from datetime import datetime
import uuid
import os

"""sqlalchemy imports"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship


"""base_model imports"""
from models.base_model import BaseModel, Base, time
from models import storage

"""engine imports"""
from engine.db_storage import classes, DBStorage


# flask-login imports
from flask_login import login_user, login_required, current_user, logout_user


# define auth_views blueprient
auth_views = Blueprint('auth_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/auth')


@auth_views.route('/login', strict_slashes=False)
def login():
    """Authenticate the user"""
    return render_template('login.html')

@auth_views.route('/login', methods = ['POST'], strict_slashes=False)
def login_post():
    """Logs in the user with the given credentials
    """
    email_address = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    user= storage.get_user(User, email_address)

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth_views.login'))
    else:
        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        return redirect(url_for('auth_views.profile'))


@auth_views.route('/signup', strict_slashes=False)
def signup():
    """Returns the signup form"""
    return render_template('signup.html')


@auth_views.route('/signup', methods = ['POST'], strict_slashes=False)
def signup_post():
    """signs up a new user to our system"""
    email_address = request.form.get('email')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    phone_number = request.form.get('phone_number')
    password = request.form.get('password')

    # storage.reload()
    user = storage.get_user(User, email_address)
    
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth_views.signup'))
    else:
        user_details = {"email_address":email_address, "first_name":first_name, "last_name":last_name, "phone_number":phone_number,
                "password":generate_password_hash(password, method='sha256')}
        new_user = User(**user_details)
        storage.new(new_user)
        storage.save()
        return redirect(url_for('auth_views.login')) 


@auth_views.route('/profile', strict_slashes=False)
@login_required
def profile():
    """Returns the user profile after successful login"""
    return render_template('profile.html', name=current_user.first_name)


@auth_views.route('/logout', strict_slashes=False)
@login_required
def logout():
    logout_user()
    """Logs out the user"""
    return redirect(url_for('standard_views.index'))










@auth_views.route('/test', strict_slashes=False)
def test():
    """Tests user instance"""
    gee_dbcolumns= {"name":"Gerald", "email_address":"geraldoduo@gmail.com", "password":"fanuel"}
    user_obj = User(**gee_dbcolumns)
    storage.reload()
    storage.new(user_obj)
    storage.save()
    return "Success..."
