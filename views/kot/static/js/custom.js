// Add an event listener on the order details buttons

let orderDetailsBtn = document.querySelectorAll('.orderDetails')

orderDetailsBtn.forEach((detailBtn) => {
  detailBtn.addEventListener('click', (ev) => {
    ev.preventDefault();
    let orderNumber = detailBtn.parentElement.previousElementSibling.previousElementSibling
		  .previousElementSibling.previousElementSibling.previousElementSibling.previousElementSibling.innerHTML;
    
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/kot/order-details", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    
    xhr.onreadystatechange = function() {
      if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
        let response = JSON.parse(this.responseText);	
        // document.querySelector('#orderDetailsloadingSpinner').classList.toggle('d-none');
	console.log(response)
        
      }
    }
    xhr.send(JSON.stringify(orderNumber));
    // document.querySelector('#orderDetailsloadingSpinner').classList.toggle('d-none');
  });
});
