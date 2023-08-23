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
	    // Creating h2 Element instead of a button but in the html it is styled as a button
	    // This is to prevent the default submission that occurs when Enter is pressed on an input 
	    // element
            const h2Elem = document.createElement("h2");
            h2Elem.classList.add("btn");
            h2Elem.classList.add("btn-danger");
            h2Elem.classList.add("remove_grn_item");
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


// Event listener for change in quantity to update the item amount
document.querySelector('#grnItemDetails').addEventListener('input', event => {
	const target = event.target;

	if (target.classList.contains('grn_item_quantity')) {
        	const row = target.closest('tr'); // Find the closest <tr> element
        	const rate = parseFloat(row.querySelector('.grn_item_rate').value);
        	const quantity = parseInt(target.value);
		const amount = rate * quantity;
        	row.querySelector('.grn_item_amount').value = amount;
		updateTotal();
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
		updateTotal();
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
document.querySelector('#grnItemDetails').addEventListener('click', event => {
	const target = event.target;


	if (target.classList.contains('remove_grn_item')) {
		const row = target.closest('tr');
		row.remove();
		updateTotal();
	}
});

// Function that updates the grn total amount
function updateTotal() {
	let total = 0;
	document.querySelectorAll('.grn_item_amount').forEach((elem) => {
	const clonedElem = elem.cloneNode();
	clonedElem.disabled = false;
	total = total + parseInt(clonedElem.value);
	
	if (!isNaN(total)) {
		// Update the total amount
        	document.querySelector('#grn_total_amount').innerHTML = +total;
	}
	});
}

// Event listener for submitting grn

document.querySelector('#grnSaveBtn').addEventListener('click', selectAllGrnDetails);


// Function that selects all grn details
function selectAllGrnDetails(event) {
	event.preventDefault();
	let grnObj = {};
	let itemsArray = [];

	const supplier = document.querySelector('#supplierName').value;
	const date = document.querySelector('#grnDate').value;
	const total = document.querySelector('#grn_total_amount').innerHTML;
	
	const itemName = document.querySelectorAll('.grn_item_name');
	const qty = document.querySelectorAll('.grn_item_quantity');
	const rate =document.querySelectorAll('.grn_item_rate');
	const amount = document.querySelectorAll('.grn_item_amount');


	itemName.forEach((elem, index) => {		
		let itemsObj = {};

		itemsObj.name = elem.value;
		itemsObj.quantity = qty[index].value;
		itemsObj.rate = rate[index].value;

		// Check if there is any empty value
		const validity = hasEmptyValue(itemsObj);

		if (!validity) {
			itemsArray.push(itemsObj);
		} else {
			alert("empty values present");
		}

	});
	// Add grn details to the grn object
	grnObj.supplier = supplier;
	grnObj.date = date;
	grnObj.total = total;
	grnObj.items = itemsArray;
	
	const grnValidity = hasEmptyValue(grnObj);
	if (!grnValidity) {
		// Post data to url
		postJSON(grnObj);


	} else {
		alert("Missing Supplier Name or Date...");
	}
	
}

function hasEmptyValue(itemsObj) {
	return Object.values(itemsObj).some(value => !value);
}

async function postJSON(obj) {
	try {
		const response = await fetch('/purchases/add_new_grn', {
			method: 'POST',
			headers: {
        			"Content-Type": "application/json",
      				},
			body: JSON.stringify(obj),
		});

		const result = await response.json();

		// Removing details on the browser after successful storage
		removeBrowserElements();
	
		alert(`${result}`);

		

	} catch (error) {
		alert(`Error: ${error}`);
	}
}

function removeBrowserElements() {
	tableBody.querySelectorAll('tr').forEach((row) => {
		row.remove();
	});
	document.querySelector('#grn_total_amount').innerHTML = 0;
	document.querySelector('#supplierName').value = '';
        document.querySelector('#grnDate').value = '';

}
