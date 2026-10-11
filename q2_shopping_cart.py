# Question 2 - Shopping Cart

products = {
    "apple": {"price": 50, "quantity": 20},
    "banana": {"price": 10, "quantity": 30},
    "milk": {"price": 120, "quantity": 10},
    "bread": {"price": 80, "quantity": 5},
    "eggs": {"price": 15, "quantity": 24},
    "rice": {"price": 150, "quantity": 3},
}

cart = {}


def add_to_cart(name, quantity):
    """Add a product to the cart and reduce the stock."""
    products[name]["quantity"] -= quantity
    cart[name] = cart.get(name, 0) + quantity


def calculate_total():
    """Return the total price of everything in the cart."""
    total = 0
    for name, quantity in cart.items():
        total += products[name]["price"] * quantity
    return total


def display_cart():
    """Print every item in the cart with its cost."""
    print("\n---------- FINAL BILL ----------")
    if not cart:
        print("Your cart is empty.")
        return
    for name, quantity in cart.items():
        price = products[name]["price"]
        print(f"{name.title():<10} {quantity:>3} x Rs.{price:<5} = Rs.{price * quantity}")
    print("--------------------------------")
    print(f"Total Price: Rs.{calculate_total()}")


print("Available products:", ", ".join(products))

while True:
    name = input("\nEnter product name (or 'done' to finish): ").strip().lower()
    if name == "done":
        break

    try:
        product = products[name]
    except KeyError:
        print(f"Error: '{name}' does not exist in the store.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            raise ValueError
    except ValueError:
        print("Error: Invalid quantity. Please enter a positive number like 2, not 'two'.")
        continue

    if quantity > product["quantity"]:
        print(f"Sorry, only {product['quantity']} {name}(s) available.")
        continue

    add_to_cart(name, quantity)
    print(f"Added {quantity} {name}(s) to the cart.")

display_cart()
