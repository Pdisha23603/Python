"""
main.py  (module controller)
-----------------------------
Entry point for the Fruit Market Console Application.
Responsibilities:
  - Display the main welcome menu
  - Route to the correct role module (Manager / Customer)
  - Keep the application running until the user explicitly exits
  - Maintain shared state (stock dict, purchase history list)

PEP 8 compliant | Modular design | Exception-safe
"""

import logging
import sys

from fruit_manager import manager_menu
from customer import customer_menu

# ---------------------------------------------------------------------------
# Application-level logging (shared log file: fruit_store.log)
# ---------------------------------------------------------------------------
logging.basicConfig(
    filename="fruit_store.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def _log(message: str) -> None:
    """Log an application-level event."""
    logging.info(message)


stock: dict = {}

# purchase_history: list of customer transaction dicts for the current session
purchase_history: list = []


# ---------------------------------------------------------------------------
# Main menu
# ---------------------------------------------------------------------------

def display_main_menu() -> None:
    """Print the welcome banner and role selection menu."""
    print("\n" + "=" * 50)
    print(" " * 15 + "WELCOME TO FRUIT MARKET")
    print("=" * 50)
    print("\n  1) Manager")
    print("  2) Customer")
    print("  3) Exit")


def run() -> None:
    """
    Main application loop.
    Keeps running until the user selects 'Exit'.
    """
    _log("APPLICATION | Fruit Market started")

    while True:
        try:
            display_main_menu()
            role = input("\n  Select your Role : ").strip()

            if role == "1":
                # Route to Fruit Manager module
                _log("NAVIGATE | Role selected: Manager")
                manager_menu(stock)

            elif role == "2":
                # Route to Customer module
                _log("NAVIGATE | Role selected: Customer")
                customer_menu(stock, purchase_history)

            elif role == "3":
                print("\n  Thank you for using Fruit Market. Goodbye!\n")
                _log("APPLICATION | Fruit Market exited by user")
                sys.exit(0)

            else:
                print("  [!] Invalid choice. Please enter 1, 2, or 3.")

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n  [!] Interrupted. Returning to main menu...\n")
            _log("WARNING | KeyboardInterrupt caught — returning to main menu")

        except Exception as error:
            # Catch-all to prevent unexpected crashes
            print(f"\n  [!] An unexpected error occurred: {error}")
            print("  Returning to main menu...\n")
            _log(f"ERROR | Unexpected exception in main loop | {error}")


# ---------------------------------------------------------------------------
# Entry point guard (PEP 8 standard)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    run()
