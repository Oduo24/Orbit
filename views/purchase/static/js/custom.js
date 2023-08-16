// Event to add new field for purchase item details
const tableBody = document.querySelector('#grnItemDetails');

// Event listener to create another field to add an item
document.querySelector('#add_item_field').addEventListener('click', event => {
    event.preventDefault();

    // Creating a new tr element with td and form input for each row
    const tableRow = document.createElement('tr');

    // Appending 6 tableData elements to tableRow
    for (let i = 0; i < 7; i++) {
        const tableData = document.createElement('td');
        const formInput = document.createElement('input');

	// Adding class form-control to formInput
        formInput.classList.add('form-control');


	// Check if the next field is the amount field and make it a disabled input
	if (i == 0) {
	    formInput.classList.add('grn_item_part_no');
 	    formInput.setAttribute('disabled', '');
	} else if (i == 1) {
	    formInput.classList.add('grn_item_name');
	    formInput.setAttribute('list', 'stock_items_list');
	} else if (i == 2) {
	    formInput.classList.add('grn_item_unit');
	    formInput.setAttribute('disabled', '');
	} else if (i == 3) {
	    formInput.classList.add('grn_item_quantity');
	    formInput.setAttribute('type', 'number');
	} else if (i == 4) {
	    formInput.classList.add('grn_item_rate');
	    formInput.setAttribute('type', 'number');
	} else if (i == 5) {
	    formInput.classList.add('grn_item_amount');
	    formInput.setAttribute('disabled', '');
	}
	
        // Appending formInput to tableData
        tableData.appendChild(formInput);

        // Appending tableData to tableRow
        tableRow.appendChild(tableData);
	
	if (i == 6) {
            const buttonElement = document.createElement("button");
            buttonElement.classList.add("btn");
            buttonElement.classList.add("btn-danger");
            buttonElement.classList.add("remove_grn_item");
            buttonElement.innerText = "-";

	    // Removing formInput element
	    tableData.removeChild(formInput);

            // Appending buttonElement to the tableData element
            tableData.appendChild(buttonElement);

            // Appending tableData to tableRow
            tableRow.appendChild(tableData);
        }
    }

    tableBody.appendChild(tableRow);

});


// Event listener for change in quantity to update the item amount
document.querySelector('#grnItemDetails').addEventListener('input', event => {
	const target = event.target;

	if (target.classList.contains('grn_item_quantity')) {
        	const row = target.closest('tr'); // Find the closest <tr> element
        	const rate = parseFloat(row.querySelector('.grn_item_rate').value);
        	const quantity = parseInt(target.value);
		const amount = rate * quantity;
        	row.querySelector('.grn_item_amount').value = amount;
		}
});

// Event listener for change in rate to update the item amount
document.querySelector('#grnItemDetails').addEventListener('input', event => {
        const target = event.target;
   
        if (target.classList.contains('grn_item_rate')) {
        	const row = target.closest('tr'); // Find the closest <tr> element
        	const quantity = parseFloat(row.querySelector('.grn_item_quantity').value);
        	const rate = parseInt(target.value);
        	const amount = rate * quantity;
        	row.querySelector('.grn_item_amount').value = amount;
		}
});



// Event to handle the selection of item name.(Retrieves the details of selected item name)

document.querySelector('#grnItemDetails').addEventListener('change', async function (event) { 
	const target = event.target;

	if (target.classList.contains('grn_item_name')) {
		const row = target.closest('tr');
		const itemName = row.querySelector('.grn_item_name').value;
		const data = { itemName: itemName };
		const partNoAndBaseUnit = await retrieveItemDetails(data);
		
		if (JSON.stringify(partNoAndBaseUnit) != JSON.stringify("Select Item Name...")) {
			// Set the part no and base unit fields for the item
			row.querySelector('.grn_item_part_no').value = partNoAndBaseUnit.itemPartNo
			row.querySelector('.grn_item_unit').value = partNoAndBaseUnit.itemBaseUnit
		} else {
			alert("Select Item Name...")	
		}
	}
});


// Function that retrieves all the details of a particular item name
async function retrieveItemDetails(itemName) {
	try {
		const response = await fetch('/purchases/item_details', {
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

// Event listener for removing an item in the grn list of items

