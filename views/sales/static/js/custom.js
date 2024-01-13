///////////////////////////// CREDIT SALE HANDLING /////////////////////////////////////////

// On selecting an item, fetch the item details and add to dom setting id = item_name
// Function that retrieves all the details of a particular item name
async function retrieveItemDetails(itemName) {
	try {
		const response = await fetch('/sales/item_details', {
			method: "POST",
      			headers: {
        			"Content-Type": "application/json",
      				},
      			body: JSON.stringify(itemName),
		});
		const result = await response.json();
        return result;

	} catch (error) {
		alert(`Error: ${error}`);
	}
}

// Event to handle the selection of item name.(Retrieves the details of selected item name)
document.querySelector('#salesInvItemDetails').addEventListener('change', async function (event) { 
	try {
        const target = event.target;

        if (target.classList.contains('sale_item_name')) {
            const row = target.closest('tr');
            const itemName = row.querySelector('.sale_item_name').value;
            const data = { itemName: itemName };
            const itemDetails = await retrieveItemDetails(data);

            if (itemDetails.error) {
                throw Error(itemDetails.error);
            }
            
            row.querySelector('.sale_item_part_no').value = itemDetails.part_no;
            row.querySelector('.sale_item_unit').value = itemDetails.base_unit;

            row.querySelector('.avail_item_quantity').disabled = false;
            row.querySelector('.avail_item_quantity').value = itemDetails.quantity;
            row.querySelector('.avail_item_quantity').disabled = true;

            row.querySelector('.sale_item_rate').disabled = false;
            row.querySelector('.sale_item_rate').value = itemDetails.rate;
            row.querySelector('.sale_item_rate').disabled = true;
        }
  } catch(error) {
    alert(error);
  }
});


// Event listener for change in quantity to update the item amount
document.querySelector('#salesInvItemDetails').addEventListener('input', event => {
	const target = event.target;

	if (target.classList.contains('sale_quantity')) {
        	const row = target.closest('tr'); // Find the closest <tr> element
        	const rate = parseInt(row.querySelector('.sale_item_rate').value);
        	const quantity = parseInt(target.value);
		const amount = checkNegative(rate * quantity);
        	row.querySelector('.sale_item_amount').value = amount;
		updateTotal();
		}
});


// Function that updates the sale total amount
function updateTotal() {
	let total = 0;
	document.querySelectorAll('.sale_item_amount').forEach((elem) => {
	const clonedElem = elem.cloneNode();
	clonedElem.disabled = false;
	total = total + parseInt(clonedElem.value);
	total = checkNegative(total)
	
	if (!isNaN(total)) {
		// Update the total amount
        	document.querySelector('#sale_total_amount').innerHTML = +total;
	}
	});
}


function checkNegative(number) {
	number = parseInt(number);
	if (number < 0) {
		return number * -1;
	} else if (number === 0) {
		alert("Invalid zero values");
	} else {
		return number;
	}
}


document.querySelector('#add_item_field').addEventListener('click', event => {
    event.preventDefault();

    // Event listener to create another field to add an item
    const tableBody = document.querySelector('#salesInvItemDetails');

    // Creating a new tr element with td and form input for each row
    const tableRow = document.createElement('tr');

    // Appending 6 tableData elements to tableRow
    for (let i = 0; i < 8; i++) {
        const tableData = document.createElement('td');
        const formInput = document.createElement('input');

        // Adding class form-control to formInput
        formInput.classList.add('form-control');

  // Check if the next field is the amount field and make it a disabled input
  if (i == 0) {
      formInput.classList.add('sale_item_part_no');
      formInput.setAttribute('disabled', '');
  } else if (i == 1) {
      formInput.classList.add('sale_item_name');
      formInput.setAttribute('list', 'stock_items_list');
  } else if (i == 2) {
      formInput.classList.add('sale_item_unit');
      formInput.setAttribute('disabled', '');
  } else if (i == 3) {
      formInput.classList.add('avail_item_quantity');
      formInput.setAttribute('type', 'number');
      formInput.setAttribute('disabled', '');
  } else if (i == 4) {
      formInput.classList.add('sale_quantity');
      formInput.setAttribute('type', 'number');

  } else if (i == 5) {
      formInput.classList.add('sale_item_rate');
      formInput.setAttribute('type', 'number');
      formInput.setAttribute('disabled', '');

  } else if (i == 6) {
      formInput.classList.add('sale_item_amount');
      formInput.setAttribute('disabled', '');
  }

  // Appending formInput to tableData
  tableData.appendChild(formInput);

  // Appending tableData to tableRow
  tableRow.appendChild(tableData);

  if (i == 7) {
      // Creating h2 Element instead of a button but in the html it is styled as a button
      // This is to prevent the default submission that occurs when Enter is pressed on an input 
      // element
      const h2Elem = document.createElement("h2");
      h2Elem.classList.add("btn");
      h2Elem.classList.add("btn-danger");
      h2Elem.classList.add("remove_sale_item");
      h2Elem.innerText = "-";

      // Removing formInput element
      tableData.removeChild(formInput);
      tableRow.removeChild(tableData);

      // Appending buttonElement to the tableData element
      tableData.appendChild(h2Elem);

      // Appending tableData to tableRow
      tableRow.appendChild(tableData);
      }
    }
    tableBody.appendChild(tableRow);
});

// Event listener for removing an item in the invoice list of items
document.querySelector('#salesInvItemDetails').addEventListener('click', event => {
	const target = event.target;

	if (target.classList.contains('remove_sale_item')) {
		const row = target.closest('tr');
		row.remove();
		updateTotal();
	}
});



///////////////////// HANDLING INVOICE SUBMISSION //////////////////////

// Function that checks for empty values
function hasEmptyValue(itemsObj) {
	return Object.values(itemsObj).some(value => !value);
}

// Function that removes browser elements
function removeBrowserElements() {
    const tableBody = document.querySelector('#salesInvItemDetails');
	tableBody.querySelectorAll('tr').forEach((row) => {
		row.remove();
	});
	document.querySelector('#sale_total_amount').innerHTML = 0;
	document.querySelector('#customer').value = '';
        document.querySelector('#saleDate').value = '';
	document.querySelector('#narration').value = '';
}

// Function that does the form submission
async function postJSON(obj) {
	try {
		const response = await fetch('/sales/sale', {
			method: 'POST',
			headers: {
        			"Content-Type": "application/json",
      				},
			body: JSON.stringify(obj),
		});

		const result = await response.json();
        return result;
	
	} catch (error) {
		alert(`Error: ${error}`);
	}
}


// Event listener for submitting inv
document.querySelector('#saleSaveBtn').addEventListener('click', selectAllSaleDetails);

function selectAllSaleDetails(event) {
    event.preventDefault();
    let invObj = {};
    let itemsArray = [];

    const customer = document.querySelector('#customer').value;
    const date = document.querySelector('#saleDate').value;
    const narration = document.querySelector('#narration').value;
    const total = document.querySelector('#sale_total_amount').innerHTML;
    
    const itemName = document.querySelectorAll('.sale_item_name');
    const qty = document.querySelectorAll('.sale_quantity');
    const rate = document.querySelectorAll('.sale_item_rate');

    // Iterate over items
    for (let index = 0; index < itemName.length; index++) {
        let itemsObj = {};

        itemsObj.name = itemName[index].value;
        itemsObj.quantity = checkNegative(qty[index].value);
        itemsObj.rate = checkNegative(rate[index].value);

        // Check if there is any empty value
        const validity = hasEmptyValue(itemsObj);

        if (!validity) {
            itemsArray.push(itemsObj);
        } else {
            alert("Empty values present in item details.");
            return; // Stop further execution
        }
    }

    // Add inv details to the invoice object
    invObj.customer = customer;
    invObj.date = date;
    invObj.narration = narration; 
    invObj.total = total;
    invObj.items = itemsArray;
    
    const invValidity = hasEmptyValue(invObj);
    if (!invValidity) {
        // Post data to url
        postJSON(invObj)
        .then(result => {
            if (result.error) {
                throw Error(result.error);
            } else {
                removeBrowserElements();
                alert(result);
            }
        })
        .catch(error => {
            alert(error);
        });
    } else {
        alert("Missing Customer Name, Narration, or Date...");
        return; // Stop further execution
    }
}



