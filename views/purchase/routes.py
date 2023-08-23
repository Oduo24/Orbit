import datetime
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

@purchases_views.route('/add_new_grn', methods=['GET', 'POST',], strict_slashes=False)
def add_new_grn():
    """Creates a new grn and save to database"""
    if request.method == 'POST':
        data = request.get_json()
        print(data)

        # Generate GRN document number
        grn_no = storage.generate_document_number('GRN')
        print(grn_no)

        if validate_date(data["date"]):
            cleaned_data = validate_items(data)
            print(cleaned_data)
            # Create grn
            grn_details = {"grn_no": grn_no, "amount": cleaned_data["total"], "supplier_name": cleaned_data["supplier"]}
            grn_object = GRN(**grn_details)
            storage.reload()
            storage.new_modified(grn_object)
            storage.save()
            # Adding grn items
            grn_id = storage.get_single_grn_id(GRN, grn_no).id # Obtained the specific grn id that will be associated with the items
            #grn_id = grn_object.id

            # Obtaining item ids
            for item in cleaned_data["items"]:
                grn_item_details = {}
                # Get id of the particular item
                stock_item_id = storage.get_stock_item_id(StockItems, item["name"]).id

                quantity = int(item["quantity"])
                rate = int(item["rate"])
                amount = int(item["amount"])
                
                # Add to the dictionary with item details
                grn_item_details["quantity"] = quantity
                grn_item_details["rate"] = rate
                grn_item_details["amount"] = amount
                grn_item_details["grn_id"] = grn_id
                grn_item_details["stock_item_id"] = stock_item_id
                
                grn_item_obj = GRNStockItem(**grn_item_details)
                storage.new_modified(grn_item_obj)
                storage.save()
            storage.close()


            return jsonify("GRN saved...")
        else:
            return jsonify("Backdated Entry...")


def validate_date(date):
    """Validates the entered date
    """
    # Convert into a python date object
    user_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    current_date = datetime.datetime.now().date()

    # Check for backdated entry
    if user_date >= current_date:
        return True
    return False

def validate_items(data):
    """Function calculates the total per item and quantity and the overal total
    """
    total = 0
    for item in data["items"]:
        item["amount"] = int(item["quantity"]) * int(item["rate"])
        total = total + int(item["amount"])
    data["total"] = total
    return data



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
            return jsonify({"itemPartNo": item_details.part_no, "itemBaseUnit": item_details.base_unit})
        else:
            return jsonify("Select Item Name...")

