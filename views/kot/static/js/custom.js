// Add an event listener on the order details buttons

let orderDetailsBtn = document.querySelectorAll('.orderDetails')

orderDetailsBtn.forEach((detailBtn) => {
  detailBtn.addEventListener('click', (ev) => {
    ev.preventDefault();
    //let orderNumber = detailBtn.parentElement.previousElementSibling.previousElementSibling
//		  .previousElementSibling.previousElementSibling.previousElementSibling.previousElementSibling.previousElementSibling.innerHTML;
    let orderNumber = detailBtn.closest('tr').querySelector('.order_number').textContent 
    	  
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/kot/order-details", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    
    xhr.onreadystatechange = function() {
      if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
        let response = JSON.parse(this.responseText);	
        // document.querySelector('#orderDetailsloadingSpinner').classList.toggle('d-none');
	// console.log(response)
	// Loop through the response which is an array object setting up the values of item_name, quantity and amount
	for (let i = 0; i < response.length; i += 3) {
	  let item_name = response[i];
          let quantity = response[i + 1];
	  let amount = response[i + 2];

	  // Create a table row element
	  let tableRow = document.createElement('tr');

	  // Create table data and input tag for each of the column values
	  let itemTableData = document.createElement('td');
    	  let itemInputTag = document.createElement('input');
    	  itemInputTag.classList.add('form-control');
	  //itemInputTag.setAttribute('id', `${item.replace(' ', '_')}`);
    	  itemInputTag.setAttribute('type', 'text');
    	  itemInputTag.setAttribute('disabled', null);
    	  itemInputTag.value = item_name;

	  let quantityTableData = document.createElement('td');
    	  let quantityInputTag = document.createElement('input');
    	  quantityInputTag.classList.add('form-control');
    	  //quantityInputTag.setAttribute('id', `${item.replace(' ', '_')}`);
    	  quantityInputTag.setAttribute('type', 'text');
    	  quantityInputTag.setAttribute('disabled', null);
    	  quantityInputTag.value = quantity;

	  let amountTableData = document.createElement('td');
    	  let amountInputTag = document.createElement('input');
    	  amountInputTag.classList.add('form-control');
    	  //amountInputTag.setAttribute('id', `${item.replace(' ', '_')}`);
    	  amountInputTag.setAttribute('type', 'text');
    	  amountInputTag.setAttribute('disabled', null);
    	  amountInputTag.value = amount;

	  //append child elements to parent elements
    	  itemTableData.appendChild(itemInputTag)
    	  tableRow.appendChild(itemTableData)

    	  quantityTableData.appendChild(quantityInputTag)
    	  tableRow.appendChild(quantityTableData)

    	  amountTableData.appendChild(amountInputTag)
    	  tableRow.appendChild(amountTableData)

    	  // Append the node to the document
    	  document.querySelector('#orderItemDetails').appendChild(tableRow);

	  // Add order Number to the details form
	  //let orderNumber = detailBtn.parentElement.previousElementSibling.previousElementSibling
          //        .previousElementSibling.previousElementSibling.previousElementSibling.previousElementSibling.innerHTML;
	  
	  document.querySelector('#orderNumberDisplay').innerHTML = orderNumber;
	}
        
      }
    }
    xhr.send(JSON.stringify(orderNumber));
  });
});



/**
 * This script section adds event listeners to all elements with the class "finishButtonClick"
 * to handle the click event and query an API endpoint using the Fetch API.
 */

/**
 * Select all elements with the class "finishButtonClick" and attach event listeners to them.
 */
let finishButtons = document.querySelectorAll('.finishButtonClick');

finishButtons.forEach(finishButton => {
  /**
   * Event listener function to handle the click event on each "finishButtonClick" button.
   * @param {Event} ev - The click event object.
   */
  finishButton.addEventListener('click', async (ev) => {
    // Prevent the default behavior of the click event, such as form submission.
    ev.preventDefault();

    // Get the order number from the parent element's parent element (two levels up in the DOM).
    let orderNumber = finishButton.parentElement.parentElement.querySelector('#orderNumberDisplay').innerHTML;

    // Define the URL for the API endpoint to query the order status.
    const orderStatusURL = '/kot/order-status/';

    // Use fetch API to POST the order number which will be used in the view to set the order status to 1(served).
    try {
      const response = await fetch(orderStatusURL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ 'order_number': orderNumber }),
      });
      const result = await response.json();
      let orderNumberLabel = document.querySelector('#orderNumberDisplay');
      const addTick = document.createElement("span");
      addTick.textContent = 'Done';

      //Adding a new class to the created element
      addTick.classList.add("badge", "rounded-pill", "bg-success")
      orderNumberLabel.appendChild(addTick);

    } catch (error) {
      console.error("Error:", error);
    }
  });
});



let orderNumberSearchBox = document.querySelector('#order_number_search');
let searchList = document.querySelectorAll('.order_number');

orderNumberSearchBox.addEventListener('input', (ev) => {
  ev.preventDefault();
  let searchTerm = orderNumberSearchBox.value;
  console.log(searchTerm)
  

  // Loop through the list items and hide/show them based on the search term
  searchList.forEach((td) => {
    const text = td.innerText;
    console.log(text);
    if (text.includes('searchTerm')) {
      td.parentElement.style.display = 'block';
      //td.style.display = 'block';
    } else {
      td.parentElement.style.display = 'none';
    }
  });
});
