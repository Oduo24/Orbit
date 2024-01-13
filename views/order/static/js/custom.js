///////////////////////// HANDLING INVOICE DETAILS DISPLAY //////////////////////////
 // Function that fetches data from the backend
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

// Function that loops through the result object  setting up the values of item_name, quantity and amount
function addInvoiceItemsToDom(result, invNumber) {
  result.forEach(item => {
    let item_name = item.item_name;
    let quantity = item.quantity;
    let amount = item.amount;

    // Create a table row element
    let tableRow = document.createElement('tr');

    // Create table data and input tag for each of the column values
    let itemTableData = document.createElement('td');
    let itemInputTag = document.createElement('input');
    itemInputTag.classList.add('form-control');
    itemInputTag.setAttribute('type', 'text');
    itemInputTag.setAttribute('disabled', null);
    itemInputTag.value = item_name;

    let quantityTableData = document.createElement('td');
    let quantityInputTag = document.createElement('input');
    quantityInputTag.classList.add('form-control');
    quantityInputTag.setAttribute('type', 'text');
    quantityInputTag.setAttribute('disabled', null);
    quantityInputTag.value = quantity;

    let amountTableData = document.createElement('td');
    let amountInputTag = document.createElement('input');
    amountInputTag.classList.add('form-control');
    amountInputTag.setAttribute('type', 'text');
    amountInputTag.setAttribute('disabled', null);
    amountInputTag.value = amount;

    //append child elements to parent elements
    itemTableData.appendChild(itemInputTag);
    tableRow.appendChild(itemTableData);

    quantityTableData.appendChild(quantityInputTag);
    tableRow.appendChild(quantityTableData);

    amountTableData.appendChild(amountInputTag);
    tableRow.appendChild(amountTableData);

    // Append the node to the document
    document.querySelector('#invItemDetails').appendChild(tableRow);
  });
  document.querySelector('#invNumberDisplay').innerHTML = invNumber;
}

//Add an event listener on the invoice details buttons 
let invDetailsBtn = document.querySelectorAll('.invDetails');
invDetailsBtn.forEach((detailBtn) => {
  detailBtn.addEventListener('click', (ev) => {
    ev.preventDefault();

    // Clearing all item details in the dom before loading new ones
    document.querySelector('#invItemDetails').innerHTML = '';
    
    let invNumber = detailBtn.closest('tr').querySelector('.inv_number').textContent;

    url = '/order/inv_item_details';
    obj = { invNumber: invNumber };
    postJSON(obj, url)
    .then(result => {
      if (result.error) {
        throw Error(result.error);
      } else {
        addInvoiceItemsToDom(result, obj.invNumber);
        console.log(result);
      }
    })
    .catch(error => {
      alert(`Error: ${error}`);
    });
  });
});


// Select all elements with the class "finishButtonClick" and attach event listeners to them.
let finishButtons = document.querySelectorAll('.finishButtonClick');

finishButtons.forEach(finishButton => {
  finishButton.addEventListener('click', (ev) => {
    ev.preventDefault();

    // Get the invoice number from the parent element's parent element (two levels up in the DOM).
    let invNumber = finishButton.parentElement.parentElement.querySelector('#invNumberDisplay').innerHTML;
    obj = { invNumber: invNumber};
    const invStatusURL = '/order/inv_status/';

    postJSON(obj, invStatusURL)
    .then(result => {
      if(result.error) {
        throw new Error(result.error);
      } else {
        let invNumberLabel = document.querySelector('#invNumberDisplay');
        const addTick = document.createElement("span");
        addTick.textContent = 'Done';
        addTick.classList.add("badge", "rounded-pill", "bg-success")
        invNumberLabel.appendChild(addTick);
      }
    })
    .catch(error => {
      alert(`Error: ${error}`);
    });
  });
});
///////////////////////// END OF HANDLING INVOICE DETAILS DISPLAY //////////////////////////


const items = document.getElementsByClassName("item-name");
const itemsName = [].map.call(items, item => item.innerHTML);

const prices = document.getElementsByClassName('item-price');
const itemsPrice = [].map.call(prices, price => price.innerHTML);

//object containing item name and price
let itemsObj = {};
itemsName.forEach((name, index) => {
        let key = name
        let value = itemsPrice[index]
        let newItem = {}
        newItem[key] = value
        Object.assign(itemsObj, newItem);
})

//checkout button event

const checkoutBtn = document.getElementById('btnCheckout');

checkoutBtn.addEventListener('click', (e) => {
	e.preventDefault()
	let checkBoxes = document.querySelectorAll('.item-data .form-check-input');
	checkBoxes.forEach((check, index) => {
		if ( check.checked == true) {
			//Create item name filed
			let itemNameDiv = document.createElement('div')
			let itemNameParagraph = document.createElement('p')
			let parentNameOfItem = document.getElementById('name-of-item')

			itemNameDiv.classList.add('name-value')
			itemNameDiv.setAttribute('id', `${itemsName[index].replace(' ', '_')}`)
			itemNameParagraph.classList.add('form-control')
			itemNameParagraph.innerHTML = itemsName[index]

			itemNameDiv.appendChild(itemNameParagraph)
			parentNameOfItem.lastChild.after(itemNameDiv)

			addQuantityField(index)
			addAmountField(index)
			removeItemField(index)
		 }
	})
})

function addQuantityField(index) {
	//Create quantity field
	let parentQuantity = document.getElementById('quantity')
	let inputBtn = document.createElement('input')
	let divElement = document.createElement('div')

	inputBtn.setAttribute('type', 'number')
	inputBtn.setAttribute('name', 'item-quantity')
	inputBtn.setAttribute('min', '1')
	inputBtn.setAttribute('value', '1')
	inputBtn.setAttribute('id', `${itemsName[index].replace(' ', '_')}`)
        inputBtn.classList.add('mb-3', 'form-control', 'quantity-value')

        //divElement.classList.add('mb-3')
	//divElement.setAttribute('id', `${itemsName[index].replace(' ', '_')}`)
        divElement.appendChild(inputBtn)

        parentQuantity.lastChild.after(divElement)
}

function addAmountField(index, inputBtn) {
	//Adding the amount column value
	let parentAmount = document.getElementById('amount')
	let amountDiv = document.createElement('div')
	let amountParagraph = document.createElement('p')

	amountDiv.classList.add('amount-value', 'mb-3', 'form-control')
	amountDiv.setAttribute('id', `${itemsName[index].replace(' ', '_')}`)
	//amountParagraph.classList.add('form-control')
	amountDiv.innerHTML = +itemsPrice[index]
	
	//amountDiv.appendChild(amountParagraph)
        parentAmount.lastChild.after(amountDiv)

	// Update total Amount
	let subTotalAmount = document.querySelector('#total-amount')
	let newSubTotalAmount= +subTotalAmount.innerHTML + +itemsPrice[index]
	subTotalAmount.innerHTML = newSubTotalAmount
	

}

function removeItemField(index) {
	let parentRemove = document.getElementById('remove')
	let removeDiv = document.createElement('div')
	let removeBtn = document.createElement('button')

	removeDiv.classList.add('mb-3', 'remove-item')
	removeDiv.setAttribute('id', `${itemsName[index].replace(' ', '_')}`)
	removeBtn.classList.add('btn', 'btn-danger', 'remove-button')
	removeBtn.setAttribute('type', 'button')
	removeBtn.innerHTML = 'remove'

	removeDiv.appendChild(removeBtn)
	parentRemove.lastChild.after(removeDiv)
        }


//Another event listener on checkoutBtn that sets the remove item functionality from checkout list

checkoutBtn.addEventListener('click', (ev) => {
	ev.preventDefault()
	let allRemoveButtons = document.querySelectorAll('.remove-item')
	allRemoveButtons.forEach((button, index) => {
		button.addEventListener('click', (event) => {
			event.preventDefault()

			//remove button
			let buttonIdAttribute = button.getAttribute('id').replace(' ', '_')

			document.querySelector(`#${buttonIdAttribute}.remove-item`).remove()
			
			//remove amount
			document.querySelector(`#${buttonIdAttribute}.amount-value`).remove()

			//remove quantity
			document.querySelector(`#${buttonIdAttribute}.quantity-value`).remove()

			//remove item name
			document.querySelector(`#${buttonIdAttribute}.name-value`).remove()
			
		})
	})
})


//event listener for updating amount value in response to quantity change
checkoutBtn.addEventListener('click', (ev) => {
	ev.preventDefault()
	let quantity = document.querySelectorAll('.quantity-value')
	quantity.forEach((field) => {
		field.addEventListener('change', (event) => {
			event.preventDefault()
			let inputTagId = event.target.getAttribute('id')
			let price = itemsObj[`${inputTagId.replace('_', ' ')}`]
			document.querySelector(`#${inputTagId}.amount-value`).innerHTML = +price * event.target.value
		})
	})

})

// Event listener for change in the amount of an item.
// Incase of change, update the total amount
//let itemAmountFields = document.querySelectorAll('.amount-value')

let changeInCheckoutItems = document.querySelector('.checkout-item-row')
changeInCheckoutItems.addEventListener('DOMSubtreeModified', (ev) => {
	ev.preventDefault()

	// Call the function that does recalculation of the Total amount.
	updateTotalAmount()
  });

function updateTotalAmount() {
  let total = 0;
  // Get the the current total amount
  let subTotalAmount = document.querySelector('#total-amount');
  
  // Get all the amount fields for each item in the checkout list
  let itemAmountFields = document.querySelectorAll('.amount-value');
  
  // Add all the amount values for each of the item
  itemAmountFields.forEach((field) => {
    total = +field.innerHTML + total;
    });
  subTotalAmount.innerHTML = total;
}


// Process the order details for final submission
// Add event listener on pay button
let payBtn = document.querySelector('#pay-btn');
payBtn.addEventListener('click', (ev) => {
  ev.preventDefault()

  // Get all the order details
  let counter = document.querySelector('#counter-number').value;
  let tender = document.querySelector('#tender-type').value;
  let waiter = document.querySelector('#waiter-name').value;
  let table = document.querySelector('#table-name').value;
  let total = document.querySelector('#total-amount').innerHTML;
  
  // Set the values in the order submission form
  document.querySelector('#counterNumber').value = counter;
  document.querySelector('#tenderType').value = tender;
  document.querySelector('#waiterName').value = waiter;
  document.querySelector('#tableName').value = table;
  document.querySelector('#totalAmount').value = total;

  // Get item names, quantity, and amount
  let items = []
  let quantities = []
  let amounts = []
  
  document.querySelectorAll('.name-value > p').forEach((name) => {
    items.push(name.innerHTML);
  });
  document.querySelectorAll('.quantity-value').forEach((elem) => {
    quantities.push(+elem.value);
  });
  document.querySelectorAll('.amount-value').forEach((amount) => {
    amounts.push(+amount.innerHTML);
  });


  // Set the values in the order submission form table 
  items.forEach((item, index) => {
    // Create a table row for the details
    let tableRow = document.createElement('tr')

    // Create table data and input tag for each of the column values
    let itemTableData = document.createElement('td');
    let itemInputTag = document.createElement('input');
    itemInputTag.classList.add('form-control');
    itemInputTag.setAttribute('id', `${item.replace(' ', '_')}`);
    itemInputTag.setAttribute('type', 'text');
    itemInputTag.setAttribute('disabled', null);
    itemInputTag.value = item;

    let quantityTableData = document.createElement('td');
    let quantityInputTag = document.createElement('input');
    quantityInputTag.classList.add('form-control');
    quantityInputTag.setAttribute('id', `${item.replace(' ', '_')}`);
    quantityInputTag.setAttribute('type', 'text');
    quantityInputTag.setAttribute('disabled', null);
    quantityInputTag.value = quantities[index];

    let amountTableData = document.createElement('td');
    let amountInputTag = document.createElement('input');
    amountInputTag.classList.add('form-control');
    amountInputTag.setAttribute('id', `${item.replace(' ', '_')}`);
    amountInputTag.setAttribute('type', 'text');
    amountInputTag.setAttribute('disabled', null);
    amountInputTag.value = amounts[index];

    //append child elements to parent elements
    itemTableData.appendChild(itemInputTag)
    tableRow.appendChild(itemTableData)

    quantityTableData.appendChild(quantityInputTag)
    tableRow.appendChild(quantityTableData)

    amountTableData.appendChild(amountInputTag)
    tableRow.appendChild(amountTableData)

    // Append the node to the document
    document.querySelector('#order-item-details').appendChild(tableRow);
  });
});



// Function that validates phone number
function validatePhoneNumber(phoneNumber) {
  // Checks if phoneNumber is a valid phone number if it is it returns the number else returns false'
  if (phoneNumber.length != 10 || phoneNumber[0] != 0 || phoneNumber[1] != 7) {
    return false
  } else if (isNaN(+phoneNumber) == true) {
    return false
  } else {
  return +phoneNumber;
  }
}



// Set on-click event listener on final-pay button
let finalPayBtn = document.querySelector('#final-pay');

finalPayBtn.addEventListener('click', (ev) => {
  ev.preventDefault();
  let customerPhoneNumber = document.querySelector('#customer-phone-number').value;
  let validatedPhoneNumber = validatePhoneNumber(customerPhoneNumber);
  if (validatedPhoneNumber == false) {
    // Flash message 'Wrong Phone Number...'
    document.querySelector('#wrong-number').classList.remove('d-none');
  } else {
    // Submit the form for backend processing
    // retrieve the order details from the final form
    let customer = document.querySelector('#customer-phone-number').value;
    let counter = document.querySelector('#counterNumber').value;
    let tender = document.querySelector('#tenderType').value;
    let waiter = document.querySelector('#waiterName').value;
    let table = document.querySelector('#tableName').value;
    let total = document.querySelector('#totalAmount').value;

    // Get item names, quantity, and amount
    let items = []
    let quantities = []
    let amounts = []

    document.querySelectorAll('.name-value > p').forEach((name) => {
      items.push(name.innerHTML);
    });
    document.querySelectorAll('.quantity-value').forEach((elem) => {
      quantities.push(+elem.value);
    });
    document.querySelectorAll('.amount-value').forEach((amount) => {
      amounts.push(+amount.innerHTML);
    });

    data = {
      customer,
      counter,
      tender,
      waiter,
      table,
      total,
      items,
      quantities,
      amounts,
    }
    let xhr = new XMLHttpRequest();

    xhr.open("POST", "/order/counter-order", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    
    xhr.onreadystatechange = function() {
      if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
        let response = JSON.parse(this.responseText);
	document.querySelector('#loadingSpinner').classList.toggle('d-none');
	document.querySelector('#orderMessage > p').innerHTML = `Order number: ${response[0]}, Payment: ${response[1]} processed...`;
	document.querySelector('#orderMessage').classList.toggle('d-none');
      }
    }
    xhr.send(JSON.stringify(data));
    document.querySelector('#loadingSpinner').classList.toggle('d-none');
  }
});



