# Generating Receipts
from pyscript import display, document


def generate_receipt(e):
    # Clear the previous result container
    document.getElementById('result').innerHTML = ""

    subtotal = 0.0
    receipt_text = "================================\n"
    receipt_text += " OBMC ENTREP FAIR: CAKE SHOP\n"
    receipt_text += "================================\n"

    # Check Item 1
    if document.getElementById('dessert1').checked:
        receipt_text += "Strawberry Shortcake  P150.00\n"
        subtotal += 150.00

    # Check Item 2
    if document.getElementById('dessert2').checked:
        receipt_text += "Mango Cheesecake      P150.00\n"
        subtotal += 150.00

    # Check Item 3
    if document.getElementById('dessert3').checked:
        receipt_text += "Red Velvet Cake       P150.00\n"
        subtotal += 150.00

    # Check Item 4
    if document.getElementById('dessert4').checked:
        receipt_text += "Mango Graham Cake     P150.00\n"
        subtotal += 150.00

    # Check Item 5
    if document.getElementById('dessert5').checked:
        receipt_text += "Oreo Cheesecake       P150.00\n"
        subtotal += 150.00

    # Calculate VAT (12%) and Total Amount
    vat = subtotal * 0.12
    total_amount = subtotal + vat

    # Build the pricing breakdown section
    receipt_text += f"SUBTOTAL:             P{subtotal:>7.2f}\n"
    receipt_text += f"VAT (12%):            P{vat:>7.2f}\n"
    receipt_text += f"TOTAL AMOUNT:         P{total_amount:>7.2f}\n"
    receipt_text += " Thank you for your support!"

    # Display the final receipt
    display(receipt_text, target='result')