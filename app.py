# app.py
# This is a backend server for Invoicely
# Flask is a lightweight Python Web Framework

from flask import Flask, render_template, request, make_response
import datetime

# Create the Flask app instance
# __name__ tells Flask where to look for templates and static files
app = Flask(__name__)

# This is our main route - when someone visits the homepage - it serves the invoice form
@app.route("/")
def index():
    return render_template("index.html")

# This route handles the PDF generation. It only accepts POST requests (form submissions)
@app.route("/generate", methods=["POST"])
def generate():
    # Grab all the form data the user submitted
    data = {
        "from_name"  : request.form.get("from_name"),
        "from_email" : request.form.get("from_email"),
        "to_name"    : request.form.get("to_name"),
        "to_email"   : request.form.get("to_email"),
        "invoice_num": request.form.get("invoice_num"),
        "due_date"   : request.form.get("due_date"),
        # [] at the end matches the input names in index.html
        "items"      : request.form.getlist("item_desc[]"),
        "quantities" : request.form.getlist("item_qty[]"),
        "prices"     : request.form.getlist("item_price[]"),
    }

    # Calculate total for each line item
    line_items = []
    for i in range(len(data['items'])):
        qty   = float(data['quantities'][i])
        price = float(data['prices'][i])
        line_items.append({
            "desc" : data['items'][i],
            "qty"  : qty,
            "price": price,
            "total": qty * price
        })

    # Sum up the grand total
    grand_total = sum(item["total"] for item in line_items)

    # Render the invoice as HTML, passing all the data in
    return render_template("invoice.html",
                           data=data,
                           line_items=line_items,
                           grand_total=grand_total,
                           today=datetime.date.today().strftime("%B %d, %Y")
                           )

# Start the server when we run this file directly
if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=10000)