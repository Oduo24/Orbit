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
