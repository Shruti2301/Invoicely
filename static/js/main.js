//static/js/main.js
// Handles adding and removing line item rows in the invoice table

// addRow() is called when the user clicks '+ Add Item'
function addRow() {

    // Grab the table body where all item rows live
    const tbody = document.getElementById('items-body');

    // Grab the first row to use as a template for the new row
    const firstRow = tbody.querySelector('tr');

    // Clone the first row - true means clone everything inside it too
    const newRow = firstRow.cloneNode(true);

    // Clear out the values in the cloned row so it's blank
    // querySelectorALL gets ALL inputs inside the new row
    newRow.querySelectorAll('input').forEach(input => { input.value = ''; });

    // Add the new blank row to the bottom of the table
    tbody.appendChild(newRow);
}

// removeRow() is called when the user clicks x on a row
// 'btn' is the button that was clicked - passed in
function removeRow(btn){

    // Get the table body
    const tbody = document.getElementById('items-body');

    // Only remove the row id there is more than 1 row
    // We always want at least one row visible
    if (tbody.querySelectorAll('tr').length > 1) {
        //.closest('tr') climbs up the DOM from the button to find its row
        btn.closest('tr').remove();
    }
}