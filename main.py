# Generating SKUs
from pyscript import display, document


def generate_sku(e):
    # Clear the previous result container
    document.getElementById('result').innerHTML = ""

    product = ""
    product_code = ""
    quantity = document.getElementById('quantity').value

    # Check Product 1
    if document.getElementById('product1').checked:
        product = "Strawberry Shortcake"
        product_code = "Strawberry Shortcake"

    # Check Product 2
    if document.getElementById('product2').checked:
        product = "Mango Cheesecake"
        product_code = "Mango Cheesecake"

    # Check Product 3
    if document.getElementById('product3').checked:
        product = "Red Velvet Cake"
        product_code = "Red Velvet Cake"

    # Check Product 4
    if document.getElementById('product4').checked:
        product = "Mango Graham Cake"
        product_code = "Mango Graham Cake"

    # Check Product 5
    if document.getElementById('product5').checked:
        product = "Oreo Cheesecake"
        product_code = "Oreo Cheesecake"

    # Check if all information is provided
    if product == "" or quantity == "":
        display("Please complete all fields.", target='result')
        return

    # Generate the SKU
    sku = product_code + quantity

    # Display the generated SKU
    display("Product: " + product, target='result')
    display("Generated SKU: " + sku, target='result')