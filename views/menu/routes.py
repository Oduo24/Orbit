#!/usr/bin/python3
"""defines the menu blueprint and the end routes"""

from flask import Blueprint, render_template, request, flash, url_for, redirect

# models imports
from models.menu_items import MenuItem
from models.uom import Uom

# python imports
from datetime import datetime
import uuid
import os

# sqlalchemy imports
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship


# base_model imports
from models.base_model import BaseModel, Base, time
from models import storage
from models.categories import Category

# engine imports
from engine.db_storage import classes, DBStorage


menu_views = Blueprint('menu_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/menu')

@menu_views.route('/inventory', strict_slashes=False)
def all_inventory_items():
    """Returns all the inventory menu items
    """
    all_uoms = storage.get_uom()
    length_of_uom = len(all_uoms)
    
    all_categories = storage.get_category()
    length_of_category = len(all_categories)

    all_items = storage.get_menu_item()
    number_of_items = len(all_items)


    return render_template('inventory.html', all_uoms=all_uoms,
            all_categories = all_categories,
            length_of_category=length_of_category,
            all_items = all_items,
            number_of_items = number_of_items,
            length_of_uom=length_of_uom)
                                



@menu_views.route('/process-new-item', methods=['POST'], strict_slashes=False)
def insert_new_item_post():
    """Processes the new item form data and stores in the database
    """
    item_name = request.form.get('item_name')
    price = request.form.get('price')
    category = request.form.get('category')
    description = request.form.get('description')
    uom = request.form.get('uom')
    state = request.form.get('state')
    image = request.form.get('image')
    
    
    menu_item = storage.get_menu_item(item_name)

    if menu_item:
        flash('Item with hte name {} already exists'.format(menu_item.item_name))
        return redirect(url_for('menu_views.all_inventory_items'))
    else:
        # get the id of the category and the uom provided
        category_id = storage.get_category(category).id
        uom_id = storage.get_uom(uom).id

        new_item_details = {"item_name":item_name, "price":int(price), "category_id":category_id, "description":description,
            "uom_id":uom_id, "state":state, "image":image}

        new_item_obj = MenuItem(**new_item_details)
        storage.reload()
        storage.new(new_item_obj)
        storage.save()

        flash('Item added successfuly...')
        return redirect(url_for('menu_views.all_inventory_items'))
    


@menu_views.route('/add-new-uom-post', methods=['POST'], strict_slashes=False)
def add_uom_post():
    """Processes the uom posted and adds to the database
    """
    symbol = request.form.get('symbol')
    description = request.form.get('description')

    uom = storage.get_uom(symbol)
    if uom:
        flash('UOM {} already exists'.format(uom.symbol))
        return redirect(url_for('menu_views.all_inventory_items'))
    else:
        uom_details = {"symbol":symbol, "description":description}
        uom_details_obj = Uom(**uom_details)
        storage.new(uom_details_obj)
        storage.save()

        flash('UOM added successfuly...')
        return redirect(url_for('menu_views.all_inventory_items'))



@menu_views.route('/add-new-category-post', methods=['POST'], strict_slashes=False)
def add_category_post():
    """Processes the category posted and adds to the database
    """
    category_name = request.form.get('category_name')
    description = request.form.get('description')

    category = storage.get_category(category_name)
    if category:
        flash('category {} already exists'.format(category.category_name))
        return redirect(url_for('menu_views.all_inventory_items'))
    else:
        category_details = {"category_name":category_name, "description":description}
        category_details_obj = Category(**category_details)
        storage.new(category_details_obj)
        storage.save()

        flash('Category added successfuly...')
        return redirect(url_for('menu_views.all_inventory_items'))

@menu_views.route('/all-menu-items', methods=['GET', 'POST'], strict_slashes=False)
def all_menu_items():
    """Retrieves a list of all menu items available or a filtered one per category
    """
    if request.method == 'POST':
        # Handle post data
        return "Post data being processed"
    else:
        all_items = storage.get_menu_item()
        number_of_items = len(all_items)
        return render_template('menu.html', all_items=all_items, number_of_items=number_of_items)

@menu_views.route('/all-menu-items-category-wise', methods=['GET','POST'], strict_slashes=False)
def items_category_wise():
    """Retrieves the menu items based on category
    """
    if request.method == 'POST':
        category_name = request.form.get('category')
    
        # get the category_id from the database
        category_id = storage.get_category(category_name).id

        # query the items table for menu items with the category_id above
        menu_items = storage.get_menu_item_by_category_id(category_id)

        return render_template('categoriwise_items.html', menu_items=menu_items)
    else:
        # return a blank form
        return render_template('categoriwise_items.html')

    # ensure to render the same menu template with the category items


@menu_views.route('/all-menu-items-inactive', strict_slashes=False)
def items_inactive():
    """Retrieve menu items from the cheapest to the most expensive
    """
    inactive_items = storage.get_inactive_menu_items()
    if inactive_items:
        return str([item.item_name for item in inactive_items])
    else:
        return "No inactive item found..."

@menu_views.route('/budget-menu-search', methods=['POST'], strict_slashes=False)
def budget_search():
    """returns a search of the menu based on the budget price
    """
    amount = request.form.get('amount')

    # Query the database for the menu items based on the provided amount
    menu_items = storage.get_budget_menu_search(amount)

    if menu_items:
        # Return the retrieved objects
        pass
    else:
        #return "Sorry, no items found..."
        pass


