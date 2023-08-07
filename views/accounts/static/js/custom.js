document.querySelector("#newLedgerForm").addEventListener('click', async function(event) {
	event.preventDefault();

	// Get the form data
	const accountNumber = document.querySelector('#account_no').value
	const ledgerName = document.querySelector('#ledger_name').value
	const accountGroup = document.querySelector('#account_group').value
	const openingAmount = document.querySelector('#opening_amount').value
	const drCr = document.querySelector('#dr_cr').value

	const data = {
		account_no: accountNumber,
		ledger_name: ledgerName,
		ledger_opening_amount: openingAmount,
		group_name: accountGroup,
		drcr: drCr
	};

	const jsonData = JSON.stringify(data);

	try {
		// Performing an asynchronous form submission using Fetch API
		const response = await fetch('/accounts/addNewLedger', {
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
