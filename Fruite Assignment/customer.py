"""
customer.py
-----------
Business logic module for the Customer role.
Handles: View Available Fruits, Buy Fruit, View Purchase History.
"""

import logging

# ---------------------------------------------------------------------------
# Logging reuses the same fruit_store.log configured in fruit_manager.py
# ---------------------------------------------------------------------------
logger = logging.getLogger()


def _log(message: str) -> None:
    """Write a customer transaction to the log file."""
    logging.info(message)


def _get_positive_int(prompt: str) -> int:
    """Prompt until a valid positive integer is entered."""
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
    """Prompt until a non-empty string is entered."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  [!] Input cannot be empty. Please try again.")


# ---------------------------------------------------------------------------
# Core customer functions
# ---------------------------------------------------------------------------

def view_available_fruits(stock: dict) -> None:
    """
    Display all fruits currently available for purchase.
    """
    print("\n  --- AVAILABLE FRUITS ---")
    try:
        if not stock:
            print("  [!] No fruits available at the moment. Please check back later.")
            return

        print(f"\n  {'Fruit':<20} {'Available (kg)':<20} {'Price (per kg)':<15}")
        print("  " + "-" * 55)
        for fruit, details in stock.items():
            print(f"  {fruit:<20} {details['qty']:<20} {details['price']:<15}")
        print("  " + "-" * 55)
        _log(f"VIEW | Customer viewed available fruits | Total: {len(stock)}")

    except Exception as error:
        print(f"\n  [!] Unexpected error: {error}. Returning to menu.")
        _log(f"ERROR | view_available_fruits | {error}")


def buy_fruit(stock: dict, purchase_history: list) -> None:
    """
    Allow the customer to purchase a fruit from available stock.
    Deducts from stock and records the transaction in purchase_history.
    """
    print("\n  --- BUY FRUIT ---")
    try:
        if not stock:
            print("  [!] No fruits available for purchase.")
            return

        # Show available stock first
        view_available_fruits(stock)

        fruit_name = _get_non_empty_string("\n  Enter Fruit Name to buy  : ").title()

        if fruit_name not in stock:
            print(f"  [!] '{fruit_name}' is not available in stock.")
            return

        available_qty = stock[fruit_name]["qty"]
        price_per_kg = stock[fruit_name]["price"]

        print(f"  Available: {available_qty} kg @ {price_per_kg} per kg")
        qty_to_buy = _get_positive_int("  Enter quantity (kg)      : ")

        if qty_to_buy > available_qty:
            print(f"  [!] Insufficient stock. Only {available_qty} kg available.")
            return

        # Deduct from stock
        stock[fruit_name]["qty"] -= qty_to_buy
        total_cost = qty_to_buy * price_per_kg

        # Record purchase
        transaction = {
            "fruit": fruit_name,
            "qty": qty_to_buy,
            "price_per_kg": price_per_kg,
            "total": total_cost,
        }
        purchase_history.append(transaction)

        print(f"\n  [✓] Purchase successful!")
        print(f"      Fruit    : {fruit_name}")
        print(f"      Quantity : {qty_to_buy} kg")
        print(f"      Total    : {total_cost}")
        _log(f"BUY | {fruit_name} | qty={qty_to_buy} | total={total_cost}")

    except Exception as error:
        print(f"\n  [!] Unexpected error: {error}. Returning to menu.")
        _log(f"ERROR | buy_fruit | {error}")


def view_purchase_history(purchase_history: list) -> None:
    """
    Display the customer's purchase history for the current session.
    """
    print("\n  --- PURCHASE HISTORY ---")
    try:
        if not purchase_history:
            print("  [!] No purchases made in this session yet.")
            return

        grand_total = 0
        print(f"\n  {'#':<5} {'Fruit':<20} {'Qty (kg)':<12} {'Price/kg':<12} {'Total':<10}")
        print("  " + "-" * 60)
        for i, record in enumerate(purchase_history, start=1):
            print(
                f"  {i:<5} {record['fruit']:<20} {record['qty']:<12} "
                f"{record['price_per_kg']:<12} {record['total']:<10}"
            )
            grand_total += record["total"]
        print("  " + "-" * 60)
        print(f"  {'Grand Total':<49} {grand_total}")
        _log(f"HISTORY | Customer viewed history | Grand total={grand_total}")

    except Exception as error:
        print(f"\n  [!] Unexpected error: {error}. Returning to menu.")
        _log(f"ERROR | view_purchase_history | {error}")


# ---------------------------------------------------------------------------
# Customer menu controller
# ---------------------------------------------------------------------------

def customer_menu(stock: dict, purchase_history: list) -> None:
    """
    Display and handle the Customer menu loop.
    Keeps running until the user chooses to go back to the main menu.
    """
    while True:
        print("\n" + " " * 20 + "Customer Menu")
        print("\n  1) View Available Fruits")
        print("  2) Buy Fruit")
        print("  3) View Purchase History")
        print("  4) Back to Main Menu")

        choice = input("\n  Enter your choice : ").strip()

        if choice == "1":
            view_available_fruits(stock)
        elif choice == "2":
            buy_fruit(stock, purchase_history)
        elif choice == "3":
            view_purchase_history(purchase_history)
        elif choice == "4":
            print("\n  Returning to main menu...\n")
            _log("NAVIGATE | Customer exited to main menu")
            break
        else:
            print("  [!] Invalid choice. Please enter 1, 2, 3, or 4.")

        # Ask if the user wants to perform more operations
        again = input("\n  Do you want to perform more operations? (y/n) : ").strip().lower()
        if again != "y":
            print("\n  Returning to main menu...\n")
            _log("NAVIGATE | Customer chose to return to main menu")
            break
