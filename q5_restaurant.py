# Question 5 - Restaurant Order System

menu = {
    "momo": 180,
    "chowmein": 150,
    "thukpa": 200,
    "dal bhat": 250,
    "sel roti": 60,
    "samosa": 40,
    "lassi": 120,
    "masala tea": 50,
}

SERVICE_CHARGE_RATE = 0.10   # 10% service charge
TAX_RATE = 0.13              # 13% VAT

order = []   # list of {"item", "quantity", "price"}


def display_menu():
    """Print every food item with its price."""
    print("\n---------- MENU ----------")
    for item, price in menu.items():
        print(f"{item.title():<12} Rs.{price}")
    print("--------------------------")


def add_item(item, quantity):
    """Add a food item to the order list (raises KeyError if not on the menu)."""
    price = menu[item]
    for line in order:
        if line["item"] == item:
            line["quantity"] += quantity
            return
    order.append({"item": item, "quantity": quantity, "price": price})


def calculate_bill():
    """Return subtotal, service charge, tax and grand total."""
    subtotal = sum(line["price"] * line["quantity"] for line in order)
    service = subtotal * SERVICE_CHARGE_RATE
    tax = (subtotal + service) * TAX_RATE
    return subtotal, service, tax, subtotal + service + tax


def display_final_order():
    """Print the full order and the final bill."""
    print("\n========== FINAL BILL ==========")
    if not order:
        print("No items were ordered.")
        return
    for line in order:
        cost = line["price"] * line["quantity"]
        print(f"{line['item'].title():<12} {line['quantity']:>2} x Rs.{line['price']:<4} = Rs.{cost}")
    subtotal, service, tax, total = calculate_bill()
    print("--------------------------------")
    print(f"Subtotal            : Rs.{subtotal:.2f}")
    print(f"Service Charge (10%): Rs.{service:.2f}")
    print(f"VAT (13%)           : Rs.{tax:.2f}")
    print(f"Grand Total         : Rs.{total:.2f}")


display_menu()

while True:
    item = input("\nEnter food item (or 'done' to finish): ").strip().lower()
    if item == "done":
        break

    try:
        menu[item]
    except KeyError:
        print(f"Error: '{item}' is not on the menu.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            raise ValueError
    except ValueError:
        print("Error: Invalid quantity. Please enter a positive number like 2, not 'two'.")
        continue

    add_item(item, quantity)
    print(f"Added {quantity} {item}(s) to your order.")

display_final_order()
