/*
const items = document.getElementsByClassName("item-name");
const prices = document.getElementsByClassName('item-price');

const itemsName = [].map.call(items, item => item.innerHTML);
const itemsPrice = [].map.call(prices, price => price.innerHTML);
let itemsObj = {};

itemsName.forEach((name, index) => {
	let key = name
	let value = itemsPrice[index]
	let newItem = {}
	newItem[key] = value
	Object.assign(itemsObj, newItem);
});
*/
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

	//Change quantity event listener
	//let quantity = document.getElementById(`${itemsName[index].replace(' ', '_')}`)
	//quantity.addEventListener('change', (event) => {
	//	event.preventDefault()
	//	amountParagraph.innerHTML = +itemsPrice[index] * +event.target.value

	//})
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


