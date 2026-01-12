# Final Project to show an Online Shopping Cart - Module 8
# Asks the end user for name, date, give items to add to cart, cost, and quantity
# The user will be presented with a Main Menu to add, remove, change, display the descriptions of the items, and output the full cart
# Make sure to use Float for price to have decimals

class ItemToPurchase:
    def __init__(self, item_name="none", item_description="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
# Calculate the item cost 
    def print_item_cost(self):
        item_total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${item_total:.2f}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
# Add Items
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)
# Remove an Item
    def remove_item(self, item_name):
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                self.cart_items.pop(i)
                return
        print("Item not found in cart. Nothing removed.")
# Change an item
    def modify_item(self, item_to_purchase):
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                # Update only non-default values
                if item_to_purchase.item_description != "none":
                    item.item_description = item_to_purchase.item_description
                if item_to_purchase.item_price != 0.0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                return
        print("Item not found in cart. Nothing modified.")
# Get how many items are in the shopping cart
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
# Get total cost
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
# Time to print the customer name, date, items, quantity and cost
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
# Is the cart empty?
        if len(self.cart_items) == 0:
            print("\nSHOPPING CART IS EMPTY")
            print(f"\nTotal: ${0.00:.2f}")
            return

        for item in self.cart_items:
            item.print_item_cost()

        print(f"\nTotal: ${self.get_cost_of_cart():.2f}")
# Print Customer Name, item descriptions
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


def read_float(prompt):
    # Make sure float is being used
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a price like 2.14.")

def read_int(prompt):
    
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a whole number like 3.")

# Main Menu that will display as the user makes changes to the cart
def print_menu(cart):
    choice = ""
    while choice != "q":
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option:\n").strip().lower()

        if choice == "a":
            print("\nADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = read_float("Enter the item price:\n")
            quantity = read_int("Enter the item quantity:\n")
            cart.add_item(ItemToPurchase(name, description, price, quantity))

        elif choice == "r":
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)

        elif choice == "c":
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = read_int("Enter the new quantity:\n")
            # Hint: make a new ItemToPurchase object before ModifyItem()
            cart.modify_item(ItemToPurchase(item_name=name, item_quantity=quantity))

        elif choice == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == "o":
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

        elif choice == "q":
            pass  # Quit

        else:
            # Invalid choice -> keep prompting
            continue

def main():
    # Ask end user for name and date, then display them
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)


if __name__ == "__main__":
    main()
