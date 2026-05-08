"""
fruit_manager.py
----------------
Business logic module for the Fruit Market Manager role.
Handles: Add Stock, View Stock, Update Stock.
All data is stored in a shared dictionary passed by reference.
"""

import logging

# ---------------------------------------------------------------------------
# Logging setup – writes every transaction to fruit_store.log
# ---------------------------------------------------------------------------
logging.basicConfig(
    filename="fruit_store.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

def _log(message: str) -> None:
    """Write a transaction entry to the log file."""
    logging.info(message)


def _get_positive_float(prompt: str) -> float:
    """Prompt the user until a valid positive float is entered."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                print("  [!] Value must be greater than zero. Please try again.")
            else:
                return value
        except ValueError:
            print("  [!] Invalid input. Please enter a numeric value.")


def _get_positive_int(prompt: str) -> int:
    """Prompt the user until a valid positive integer is entered."""
    while True:
        try:
            value = int(input(prompt).strip())
            if value <= 0:
                print("  [!] Value must be greater than zero. Please try again.")
            else:
                return value
        except ValueError:
            print("  [!] Invalid input. Please enter a whole number.")


def _get_non_empty_string(prompt: str) -> str:
    """Prompt the user until a non-empty string is entered."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  [!] Input cannot be empty. Please try again.")


# ---------------------------------------------------------------------------
# Core manager functions
# ---------------------------------------------------------------------------

def add_fruit_stock(stock: dict) -> None:
    """
    Add a new fruit or increase quantity of an existing one.
    Expects: fruit name, quantity (kg), price (per kg).
    """
    print("\n  --- ADD FRUIT STOCK ---")
    try:
        fruit_name = _get_non_empty_string("  Enter Fruit Name       : ").title()
        qty = _get_positive_int("  Enter qty (in kg)     : ")
        price = _get_positive_float("  Enter price (per kg)  : ")

        if fruit_name in stock:
            # Fruit already exists — accumulate quantity
            stock[fruit_name]["qty"] += qty
            stock[fruit_name]["price"] = price  # update price
            print(f"\n  [✓] '{fruit_name}' stock updated successfully.")
            _log(f"ADD | {fruit_name} | qty={qty} | price={price} | (existing item updated)")
        else:
            stock[fruit_name] = {"qty": qty, "price": price}
            print(f"\n  [✓] '{fruit_name}' added to stock successfully.")
            _log(f"ADD | {fruit_name} | qty={qty} | price={price} | (new item added)")

    except Exception as error:
        print(f"\n  [!] Unexpected error: {error}. Returning to menu.")
        _log(f"ERROR | add_fruit_stock | {error}")


def view_fruit_stock(stock: dict) -> None:
    """
    Display all fruits currently in stock in a formatted table.
    """
    print("\n  --- VIEW FRUIT STOCK ---")
    try:
        if not stock:
            print("  [!] No stock available at the moment.")
            return

        # Print header
        print(f"\n  {'Fruit':<20} {'Qty (kg)':<15} {'Price (per kg)':<15}")
        print("  " + "-" * 50)
        for fruit, details in stock.items():
            print(f"  {fruit:<20} {details['qty']:<15} {details['price']:<15}")
        print("  " + "-" * 50)
        _log(f"VIEW | Manager viewed stock | Total items: {len(stock)}")

    except Exception as error:
        print(f"\n  [!] Unexpected error: {error}. Returning to menu.")
        _log(f"ERROR | view_fruit_stock | {error}")


def update_fruit_stock(stock: dict) -> None:
    """
    Update quantity and/or price for an existing fruit.
    """
    print("\n  --- UPDATE FRUIT STOCK ---")
    try:
        if not stock:
            print("  [!] No stock available to update.")
            return

        fruit_name = _get_non_empty_string("  Enter Fruit Name to update : ").title()

        if fruit_name not in stock:
            print(f"  [!] '{fruit_name}' not found in stock. Please add it first.")
            return

        print(f"  Current — Qty: {stock[fruit_name]['qty']} kg | Price: {stock[fruit_name]['price']}")
        new_qty = _get_positive_int("  Enter new qty (in kg) : ")
        new_price = _get_positive_float("  Enter new price       : ")

        stock[fruit_name]["qty"] = new_qty
        stock[fruit_name]["price"] = new_price
        print(f"\n  [✓] '{fruit_name}' updated successfully.")
        _log(f"UPDATE | {fruit_name} | new_qty={new_qty} | new_price={new_price}")

    except Exception as error:
        print(f"\n  [!] Unexpected error: {error}. Returning to menu.")
        _log(f"ERROR | update_fruit_stock | {error}")


# ---------------------------------------------------------------------------
# Manager menu controller
# ---------------------------------------------------------------------------

def manager_menu(stock: dict) -> None:
    """
    Display and handle the Fruit Market Manager menu loop.
    Keeps running until the user chooses to go back to the main menu.
    """
    while True:
        print("\n" + " " * 20 + "Fruit Market Manager")
        print("\n  1) Add Fruit Stock")
        print("  2) View Fruit Stock")
        print("  3) Update Fruit Stock")
        print("  4) Back to Main Menu")

        choice = input("\n  Enter your choice : ").strip()

        if choice == "1":
            add_fruit_stock(stock)
        elif choice == "2":
            view_fruit_stock(stock)
        elif choice == "3":
            update_fruit_stock(stock)
        elif choice == "4":
            print("\n  Returning to main menu...\n")
            _log("NAVIGATE | Manager exited to main menu")
            break
        else:
            print("  [!] Invalid choice. Please enter 1, 2, 3, or 4.")

        # Ask if the user wants to perform more operations
        again = input("\n  Do you want to perform more operations? (y/n) : ").strip().lower()
        if again != "y":
            print("\n  Returning to main menu...\n")
            _log("NAVIGATE | Manager chose to return to main menu")
            break
