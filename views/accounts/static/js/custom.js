const newAccount = document.querySelector("#newAccountForm");

if (newAccount) {
	newAccount.addEventListener('click', async function(event) {
		event.preventDefault();

		// Get the form data
		const accountNumber = document.querySelector('#account_no').value
		const accountName = document.querySelector('#account_name').value
		const accountGroup = document.querySelector('#account_group').value
		const openingAmount = document.querySelector('#opening_amount').value
		const drCr = document.querySelector('#dr_cr').value

		const data = {
			account_no: accountNumber,
			account_name: accountName,
			account_opening_amount: openingAmount,
			group_name: accountGroup,
			drcr: drCr
		};

		const jsonData = JSON.stringify(data);

		try {
			// Performing an asynchronous form submission using Fetch API
			const response = await fetch('/accounts/addNewAccount', {
				method: "POST",
				headers: {
						"Content-Type": "application/json",
						},
				body: jsonData,
				});

			// Handle the response from the server
			const responseData = await response.json();
			alert(responseData);
		} catch (error) {
			alert(error);
		};
	});

} else {
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
			return error;
		}
	}

	// Validate form data for last payment form
	function validateLastPaymentDetailsForm(supplier, payingAccount) {
		if (supplier | payingAccount === '') {
			return false;
		} else {
			return true;
		}
	}

	// Validate form data for payment form
	function validatePaymentForm(supplier, payingAccount, amountPaid) {
		if (supplier | payingAccount | amountPaid === '') {
			return false;
		} else {
			return true;
		}
	}

	// Event listener to load last payment details
	document.querySelector('#getOutstandingBalance').addEventListener('click', (event) => {
		event.preventDefault();
		let supplier = document.querySelector('#nameOfSupplier').value;
		let payingAccount = document.querySelector('#fromAccount').value;
		const url = '/accounts/last_payment_info';

		postData = {
			"supplier": supplier,
			"payingAccount": payingAccount
		}

		const validate1 = validateLastPaymentDetailsForm(supplier, payingAccount);
		
		if (validate1) {
			postJSON(postData, url)
			.then(result => {
				// Display to the dom
				const lastPaymentField = document.querySelector('#lastPaymentDate');
				lastPaymentField.disabled = false;
				lastPaymentField.value = result.date;
				lastPaymentField.disabled = true;

				const currentBalance = document.querySelector('#currentBalance');
				currentBalance.disabled = false;
				currentBalance.value = result.balance;
				currentBalance.disabled = true;
			})
			.catch(error => {
				alert(`Error: ${error}`);
			});
		} else {
			alert("Error: Empty fields present");
		}
	});

	// Event listener for submitting payment details
	document.querySelector('#paymentSaveBtn').addEventListener('click', (event) => {
		event.preventDefault();
		const supplier = document.querySelector('#nameOfSupplier').value;
		const payingAccount = document.querySelector('#fromAccount').value;
		const amountPaid = document.querySelector('#amountPaid').value;
		const url = '/accounts/pay';

		postData = {
			"supplier": supplier,
			"payingAccount": payingAccount,
			"amountPaid": amountPaid
		}

		const validate2 = validatePaymentForm(supplier, payingAccount, amountPaid);
		
		if (validate2) {
			postJSON(postData, url)
			.then(result => {
				alert(result);
				// Clear dom content
				document.querySelector('#nameOfSupplier').value = '';
				document.querySelector('#fromAccount').value = '';
				document.querySelector('#payNarration').value = '';
				document.querySelector('#getOutstandingBalance').value = '';
				document.querySelector('#amountPaid').value = '';
			})
			.catch(error => {
				alert(`Error: ${error}`);
			});
		} else {
			alert("Error: Empty fields present");
		}
	});
}



