from Menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    """Display the program menu and handle user input."""
    while True:
        print("\nMenu Options:")
        print("V - View an Item")
        print("A - Add an Item")
        print("D - Delete an Item")
        print("U - Update an Item")
        print("S - Show the Menu")
        print("E - Exit")
        
        choice = input("Enter your choice: ").upper()
        
        if choice == 'V':
            view_item()
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'E':
            show_restaurant_menu()
            break
        else:
            print("Invalid choice. Please try again.")

def add_item_to_menu():
    """Add an item to the menu."""
    name = input("Enter the item name: ")
    try:
        price = float(input("Enter the item price: "))
    except ValueError:
        print("Invalid price. Must be a number.")
        return
    
    item = MenuItem(name, price)
    item.save()
    print("Item was added successfully.")

def remove_item_from_menu():
    """Remove an item from the menu."""
    name = input("Enter the name of the item to remove: ")
    item = MenuItem(name, 0)  # Price is not needed for deletion
    try:
        item.delete()
        print("Item was deleted successfully.")
    except Exception as e:
        print(f"Error deleting item: {e}")

def update_item_from_menu():
    """Update an item in the menu."""
    name = input("Enter the name of the item to update: ")
    new_name = input("Enter the new name for the item (or press Enter to keep the current name): ")
    try:
        new_price = input("Enter the new price for the item (or press Enter to keep the current price): ")
        if new_price:
            new_price = float(new_price)
        else:
            new_price = None
    except ValueError:
        print("Invalid price. Must be a number.")
        return

    item = MenuItem(name, 0)  # Current price is not used for updating
    try:
        item.update(new_name=new_name or None, new_price=new_price)
        print("Item was updated successfully.")
    except Exception as e:
        print(f"Error updating item: {e}")

def show_restaurant_menu():
    """Display the restaurant menu."""
    items = MenuManager.all_items()
    if items:
        print("\nRestaurant Menu:")
        for item in items:
            print(f"ID: {item['item_id']}, Name: {item['item_name']}, Price: ${item['item_price']}")
    else:
        print("No items found in the menu.")

# Run the menu editor
if __name__ == "__main__":
    show_user_menu()
