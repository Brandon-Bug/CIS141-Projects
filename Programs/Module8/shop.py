# Harvest Moon Shop Inventory Module

# Initial inventory (item name: {price, stock})
inventory = {
    "Turnip Seeds": {"price": 50, "stock": 10},
    "Cabbage Seeds": {"price": 100, "stock": 5},
    "Asparagus Seeds": {"price": 80, "stock": 8},
    "Tomato Seeds": {"price": 75, "stock": 12},
    "Chicken Feed": {"price": 200, "stock": 4}
}

def view_inventory():
    """Displays the current inventory with prices and stock."""
    print("\n--- Harvest Moon Shop Inventory ---")
    for item, details in inventory.items():
        print(f"{item}: {details['stock']} in stock, {details['price']}G each")
    print("----------------------------------")

def buy_item(item_name, quantity):
    """Handles buying an item, reducing stock, and returning the total cost."""
    if item_name in inventory:
        if inventory[item_name]["stock"] >= quantity:
            total_cost = inventory[item_name]["price"] * quantity
            inventory[item_name]["stock"] -= quantity
            print(f"Purchased {quantity} {item_name}(s) for {total_cost}G.")
            return total_cost
        else:
            print(f"Sorry, not enough stock for {item_name}.")
            return None
    else:
        print(f"{item_name} is not available in the shop.")
        return None

def restock_item(item_name, quantity):
    """Adds stock to an item in the inventory."""
    if item_name in inventory:
        inventory[item_name]["stock"] += quantity
        print(f"{item_name} restocked. New stock: {inventory[item_name]['stock']}")
    else:
        print(f"{item_name} is not in the shop.")
