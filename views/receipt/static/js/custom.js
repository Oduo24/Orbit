//////////////////////// ADDING A NEW ITEM FIELD ////////////////////////
document.querySelector('#add_item_field').addEventListener('click', event => {
    event.preventDefault();

    const tableBody = document.querySelector('#receiptDetails');

    // Creating a new tr element with td and form input for each row
    const tableRow = document.createElement('tr');

    // Appending 3 tableData elements to tableRow
    for (let i = 0; i < 4; i++) {
        const tableData = document.createElement('td');
        const formInput = document.createElement('input');

        // Adding class form-control to formInput
        formInput.classList.add('form-control');

        if (i == 0) {
            formInput.classList.add('customers');
            formInput.setAttribute('list', 'customerList');
        } else if (i == 1) {
            formInput.classList.add('receipt_amount');
        } else if (i == 2) {
            formInput.classList.add('remarks');
        }
        // Appending formInput to tableData
        tableData.appendChild(formInput);

        // Appending tableData to tableRow
        tableRow.appendChild(tableData);

        if (i == 3) {
            // Creating h2 Element instead of a button but in the html it is styled as a button
            // This is to prevent the default submission that occurs when Enter is pressed on an input 
            // element
            const h2Elem = document.createElement("h2");
            h2Elem.classList.add("btn");
            h2Elem.classList.add("btn-danger");
            h2Elem.classList.add("remove_receipt");
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

///////////////////////// REMOVING AN ITEM IN THE LIST ////////////////////////////
document.querySelector('#receiptDetails').addEventListener('click', event => {
	const target = event.target;

	if (target.classList.contains('remove_receipt')) {
		const row = target.closest('tr');
		row.remove();
		updateTotal();
	}
});

// Function that updates the sale total amount
function updateTotal() {
	let total = 0;
	document.querySelectorAll('.receipt_amount').forEach((elem) => {
	total = total + parseInt(elem.value);
	total = checkNegative(total)
	
	if (!isNaN(total)) {
		// Update the total amount
        	document.querySelector('#total_amount').innerHTML = +total;
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

// Function that checks for empty values
function hasEmptyValue(itemsObj) {
	return Object.values(itemsObj).some(value => !value);
}

// Function that does the form submission
async function postJSON(obj, url) {
	try {
		const response = await fetch(url, {
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

// Function that removes browser elements
function removeBrowserElements() {
    const tableBody = document.querySelector('#receiptDetails');
	tableBody.querySelectorAll('tr').forEach((row) => {
		row.remove();
	});
	document.querySelector('#paid_to_account').innerHTML = 0;
    document.querySelector('#receiptDate').value = '';
}

/////////////////////////// SUBMITTING PAYMENT FORM ////////////////////////////
document.querySelector('#receiptSaveBtn').addEventListener('click', event => {
    event.preventDefault();

    let receipt = {};
    let individualReceipts = [];

    const paid_to_account = document.querySelector('#paid_to_account').value;

    
    const customers = document.querySelectorAll('.customers');
    const receipt_amount = document.querySelectorAll('.receipt_amount');
    const remarks = document.querySelectorAll('.remarks');

    // Iterate over receipts setting individual receipt details
    for (let index = 0; index < customers.length; index++) {
        let receiptObj = {};

        receiptObj.customer = customers[index].value;
        receiptObj.receipt_amount = checkNegative(receipt_amount[index].value);
        receiptObj.remarks = remarks[index].value;

        // Check if there is any empty value
        const validity = hasEmptyValue(receiptObj);

        if (!validity) {
            individualReceipts.push(receiptObj);
        } else {
            alert("Empty values present in individual receipt.");
            return; // Stop further execution
        }
    }


    // Add individual receipt details to the receipt object
    receipt.paid_to_account = paid_to_account;
    receipt.individualReceipts = individualReceipts;
    
    const receiptValidity = hasEmptyValue(receipt);
    if (!receiptValidity) {
        url = '/receipt/new_receipt'
        // Post data to url
        postJSON(receipt, url)
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
        alert("Missing values...!");
        return; // Stop further execution
    }
});


