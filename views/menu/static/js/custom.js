//Submit add-new-uom form
let uomSubmitBtn = document.querySelector('#submit_uom_form')

uomSubmitBtn.addEventListener('click', (event) => {
	event.preventDefault()
	document.querySelector('#add_uom_form').submit()
})

//Submit add-new-uom form
let categorySubmitBtn = document.querySelector('#submit_category_form')

categorySubmitBtn.addEventListener('click', (event) => {
        event.preventDefault()
        document.querySelector('#add_category_form').submit()
})

//Submit add-new-item form
let itemSubmitBtn = document.querySelector('#submit_item_form')

itemSubmitBtn.addEventListener('click', (event) => {
        event.preventDefault()
        document.querySelector('#add_item_form').submit()
})



// Event listener for submitting new stock item details
document.querySelector('#submit_stock_item_form').addEventListener('click', event => {
	event.preventDefault();

	// Getting the form details
	const stock_item_name = document.querySelector('#stock_item_name').value;
	const part_no = document.querySelector('#part_no').value;
	const stock_item_description = document.querySelector('#stock_item_description').value;
	const item_uom = document.querySelector('#item_uom').value;

	const newStockItem = {
		item_name: stock_item_name,
		part_no: part_no,
		item_description: stock_item_description,
		base_unit: item_uom
	};
	postJSON(newStockItem);

});

// Function that POSTS the data to the view
async function postJSON(data) {
  try {
    const response = await fetch("/purchases/add_stock_item", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    const result = await response.json();

    // I will customize this message alert
    alert(`Message: ${result}`);
  } catch (error) {
    alert(`Error:, ${error}`);
  }
}
