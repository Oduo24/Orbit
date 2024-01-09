import datetime
from flask import Blueprint, render_template, request, flash, url_for, redirect, jsonify

from sqlalchemy.exc import IntegrityError

from models.purchases import GRN, GRNStockItem, PurchaseInvoice, Supplier, StockItems
from models.accounts_models.accounts import Account, Transaction

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
        grns = storage.get_all_objects(GRN)
        purchase_invoices = storage.get_all_objects(PurchaseInvoice)
        number_of_grns = len(grns)
    except Exception as e:
        storage.rollback()
        storage.close()
        return render_template('purchase.html')

    return render_template('purchase.html', suppliers=suppliers,
                                            grns=grns,
                                            number_of_grns=number_of_grns,
                                            stock_items=stock_items,
                                            purchase_invoices=purchase_invoices,
                                            number_of_invoices=len(purchase_invoices))

@purchases_views.route('/add_new_grn', methods=['GET', 'POST',], strict_slashes=False)
def add_new_grn():
    """Creates a new grn and save to database"""
    if request.method == 'POST':
        data = request.get_json()

        storage.reload()
        # Generate GRN document number
        grn_no = storage.generate_document_number('GRN')

        if validate_date(data["date"]):
            cleaned_data = validate_items(data)

            try:
                # Create grn
                grn_details = { "grn_no": grn_no, 
                                "amount": cleaned_data["total"], 
                                "supplier_name": cleaned_data["supplier"], 
                                "reference_no": cleaned_data["reference_no"]
                                }
                grn_object = GRN(**grn_details)

                items_list = []
                print(cleaned_data["items"])
                for item in cleaned_data["items"]:
                    grn_item_details = {}
                    # Get id of the particular item
                    stockItem = storage.get_stock_item_by_id(StockItems, item["name"])
                    
                    # Add to the dictionary with item details
                    grn_item_details["quantity"] = int(item["quantity"])
                    grn_item_details["rate"] = int(item["rate"])
                    grn_item_details["amount"] = int(item["amount"])
                    grn_item_details["grn_id"] = grn_object.id
                    grn_item_details["stock_item_id"] = stockItem.id
                    
                    grn_item_obj = GRNStockItem(**grn_item_details)
                    items_list.append(grn_item_obj)

                    # Increament the stock quantity of each item
                    stockItem.quantity += int(grn_item_details["quantity"])
                    storage.new_modified(stockItem)
                    
                
                    print(stockItem.quantity, stockItem.item_name)

                grn_object.items.extend(items_list)
                storage.new_modified(grn_object)
                storage.save()

            except IntegrityError as ie:
                storage.rollback()
                storage.close()
                return jsonify("Error: Possible duplicate entry of item name."), 500
            except Exception as e:
                storage.rollback()
                storage.close()
                return jsonify(str(e) + "\n Potentially an invalid item name has been entered."), 500

            storage.close()
            return jsonify(f"SUCCESS>\nGRN No. {grn_no} saved."), 200
        else:
            return jsonify("Backdated Entry...")


def validate_date(date):
    """Validates the entered date
       I have removed the functionality of this function since every grn has its automatic
       creation date as an object in the model, hence it returns True for each case
    """
    # Convert into a python date object
    user_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    current_date = datetime.datetime.now().date()

    # Check for backdated entry
    if user_date >= current_date:
        return True
    return True

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


@purchases_views.route('/grn_details', methods=['GET', 'POST'], strict_slashes=False)
def grn_details():
    """Retrieves the details of a particular grn number"""
    if request.method == "POST":
        try:
            grn_no = request.get_json()
            grn = storage.get_single_grn_id(GRN, grn_no)
            items = grn.items
            grn_details = {}

            all_items = []
            for item in items:
                item_dict = {}

                # append quantity, rate and amount to item_dict
                item_dict["quantity"] = item.quantity
                item_dict["amount"] = item.amount
                item_dict["rate"] = item.rate

                # Get the stock item id
                item_id = item.stock_item_id
                stock_item = storage.get_item_by_id(item_id)

                # Appending the item part_no, itemname and uom
                item_dict["item_name"] = stock_item.item_name
                item_dict["part_no"] = stock_item.part_no
                item_dict["uom"] =  stock_item.base_unit

                # Appending to the all_items list
                all_items.append(item_dict)

            grn_details["items"] = all_items
            grn_details["grn_total"] = grn.amount
            grn_details["supplier"] = grn.supplier_name
            grn_details["ref_no"] = grn.reference_no
            grn_details["grn_no"] = grn.grn_no
            # Close session

        except Exception as e:
            return jsonify({"error": f"Could not retrieve data from the db.\n {e}"}), 500

        return jsonify(grn_details), 200

@purchases_views.route('/pending_grns', methods=['GET', 'POST'], strict_slashes=False)
def pending_grns():
    """
    Function that returns pending grns(grns of the supplier that have not been invoiced)
    """
    if request.method == 'POST':

        try:
            supplier_name = request.get_json()
            
            # Get session
            storage.reload()

            grns = storage.get_pending_grns(supplier_name)
            grns_list = [grn.grn_no for grn in grns]

            return jsonify(grns_list), 200

            # Close session
            storage.close()

        except Exception as e:
            return jsonify({"error": f"Could not retrieve pending grns from the db.\n {e}"}), 500

@purchases_views.route('/new_invoice', methods=['GET', 'POST'], strict_slashes=False)
def new_invoice():
    """
    Creates and saves new grn
    """
    if request.method == 'POST':
        try:
            data = request.get_json()

            #purchase invoice object details
            invoice_no = storage.generate_document_number('INV')
            grn = storage.get_single_grn_id(GRN, data["GRN_No"])
            grn_id = grn.id
            supplier_name = grn.supplier_name

            purchase_invoice_details = {
                    "invoice_no": invoice_no,
                    "supplier_invoice_date": data["Supplier_Invoice_Date"],
                    "grn_no": grn_id,
                    "supplier_name": supplier_name,
                    "reference_no": data["Supplier_Invoice_No"],
                    "narration": data["narration"]
                    }
            new_invoice = PurchaseInvoice(**purchase_invoice_details)
            # Mark grn as already invoiced
            grn.is_invoiced = True

            #storage.reload()
            storage.new_modified(new_invoice)
            storage.new_modified(grn)

            # Handle transaction
            # Accounts involved are accounts payable and inventory account dr inventory and cr accounts payable
            # accounts are inventory, payables
            inventory_account = storage.get_account("Inventory")
            payables_account = storage.get_account("Payables")

            transaction_details = {
                    "supplier": supplier_name,
                    "transaction_number": invoice_no,
                    "amount": grn.amount,
                    "dr": inventory_account.id,
                    "cr": payables_account.id,
                    }
            new_transaction = Transaction(**transaction_details)

            # append the accounts related to this transaction
            new_transaction.accounts.append(inventory_account)
            new_transaction.accounts.append(payables_account)
            storage.new_modified(new_transaction)

            # update the supplier account balance
            supplier = storage.get_supplier(supplier_name)
            supplier.balance = supplier.balance + int(grn.amount)
            storage.new_modified(supplier)
        except Exception as e:
            storage.rollback()
            storage.close()
            return jsonify({"error": f"Could not create a new invoice. \n {e}"}), 500

        storage.save()
        storage.close()
        return jsonify(f"SUCCESS. \n Invoice number {invoice_no} created."), 200
