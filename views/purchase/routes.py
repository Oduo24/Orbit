from flask import Blueprint, render_template, request, flash, url_for, redirect, jsonify

from sqlalchemy.exc import IntegrityError

from models.purchases import GRN, GRNStockItem, Purchase, PurchaseStockItems, Supplier, StockItems

from models import storage

# defining the purchases_views blueprint
purchases_views = Blueprint('purchases_views', __name__,
                            template_folder='templates',
                            static_folder='static',
                            url_prefix='/purchases')


@purchases_views.route('/add_stock_item', methods=['POST',], strict_slashes=False)
def new_stock_item():
    """Creates a new stock item and saves to the database"""
    if request.method == "POST":
        data = request.get_json()

        # Creating the StockItem object
        item_object = StockItems(**data)

        # Saving the ledger to the database
        try:
            storage.new(item_object)
            storage.save()
        except IntegrityError:
            return jsonify("part number already exists in the system")
        except Exception as e:
            return jsonify("Unknown Exception occured")
        else:
            return jsonify("New item added successfully")

@purchases_views.route('/purchases_master_template', methods=['GET',], strict_slashes=False)
def get_all_purchases():
    """Returns the purchases master template with all the purchases present in the system"""
    # Retrieve all the suppliers in the database
    try:
        stock_items = storage.get_all_objects(StockItems)
        suppliers = storage.get_all_objects(Supplier)
    except Exception as e:
        flash("Error: Could not retrieve suppliers from the db")
        return render_template('purchase.html')

    return render_template('purchase.html', suppliers=suppliers,
                                            stock_items=stock_items)

@purchases_views.route('/add_new_grn', methods=['GET',], strict_slashes=False)
def add_new_grn():
    """Creates a new grn and save to database"""
    # Generate GRN document number
    grn_no = storage.generate_document_number('GRN')


@purchases_views.route('/item_details', methods=['GET', 'POST'], strict_slashes=False)
def item_name_details():
    """Retrieves the details of a particular item name"""
    if request.method == "POST":
        data = request.get_json()
        item_name = data["itemName"]

        try:
            item_details = storage.get_single_item_details(StockItems, item_name)
        except Exception:
            return jsonify("Could not retrieve item details from the db")
        if item_details:
            print(item_details.part_no)
            return jsonify({"itemPartNo": item_details.part_no, "itemBaseUnit": item_details.base_unit})
        else:
            return jsonify("Select Item Name...")

