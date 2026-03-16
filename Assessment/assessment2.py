# Restaurant Ordering System
# Design a Python class RestaurantSystem to simulate a basic restaurant order
# management process. The system should support:
# Functional Requirements:
# ➔ Display Menu:
# ◆ Show a list of food items with prices and item codes.
# ➔ Take Order:
# ◆ Allow users to select multiple items by item code and quantity.
# ◆ Calculate total price and generate a unique order ID.
# ➔ View Order:
# ◆ Look up details of an order using the order ID.
# ➔ Cancel Order:
# ◆ Cancel an existing order using the order ID.
# ➔ Exit the system


# import uuid

# class RestaurantSystem:
    
#     def __init__(self):
#         self.menu = {
#             101: ("Pizza", 250),
#             102: ("Burger", 120),
#             103: ("Pasta", 180),
#             104: ("Sandwich", 100),
#             105: ("Cold Drink", 60)
#         }
        

#         self.orders = {}


#     def display_menu(self):
#         print("\n------ MENU ------")
#         for code, item in self.menu.items():
#             print(f"Code: {code} | Item: {item[0]} | Price: ₹{item[1]}")
#         print("------------------")


#     def take_order(self):
#         order_items = []
#         total_price = 0

#         while True:
#             try:
#                 code = int(input("Enter item code (0 to stop): "))
                
#                 if code == 0:
#                     break
                
#                 if code not in self.menu:
#                     print("Invalid item code!")
#                     continue
                
#                 qty = int(input("Enter quantity: "))
                
#                 item_name, price = self.menu[code]
#                 subtotal = price * qty
#                 total_price += subtotal
                
#                 order_items.append((item_name, qty, subtotal))
                
#             except ValueError:
#                 print("Please enter valid numbers.")

#         if order_items:
#             order_id = str(uuid.uuid4())[:8] 
#             self.orders[order_id] = {
#                 "items": order_items,
#                 "total": total_price
#             }
            
#             print("\nOrder placed successfully!")
#             print("Your Order ID:", order_id)
#             print("Total Amount: ₹", total_price)
#         else:
#             print("No items selected.")

#     def view_order(self):
#         order_id = input("Enter Order ID: ")
        
#         if order_id in self.orders:
#             print("\nOrder Details:")
#             for item in self.orders[order_id]["items"]:
#                 print(f"{item[0]} | Qty: {item[1]} | Subtotal: ₹{item[2]}")
#             print("Total: ₹", self.orders[order_id]["total"])
#         else:
#             print("Order not found.")

#     def cancel_order(self):
#         order_id = input("Enter Order ID to cancel: ")
        
#         if order_id in self.orders:
#             del self.orders[order_id]
#             print("Order cancelled successfully.")
#         else:
#             print("Order not found.")


# system = RestaurantSystem()

# while True:
#     print("\n       Restaurant Ordering System        ")
#     print("1. Display Menu")
#     print("2. Take Order")
#     print("3. View Order")
#     print("4. Cancel Order")
#     print("5. Exit")
    
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         system.display_menu()
#     elif choice == "2":
#         system.display_menu()
#         system.take_order()
#     elif choice == "3":
#         system.view_order()
#     elif choice == "4":
#         system.cancel_order()
#     elif choice == "5":
#         print("Thank you! Visit again 😊")
#         break
#     else:
#         print("Invalid choice. Try again.")


import uuid

class RestaurantSystem:

    def __init__(self):
        self.menu = {
            101: ("Pizza", 250),
            102: ("Burger", 120),
            103: ("Pasta", 180),
            104: ("Sandwich", 100),
            105: ("Cold Drink", 60)
        }
        self.orders = {}


    def display_menu(self):
        print("\n      MENU      ")
        for code, item in self.menu.items():
            print(f"{code} - {item[0]} - ₹{item[1]}")
        print("")


    def take_order(self):
        order_items = []
        total = 0

        while True:
            try:
                code = int(input("Enter item code (0 to stop): "))

                if code == 0:
                    break

                if code not in self.menu:
                    print("Invalid item code!")
                    continue

                qty = int(input("Enter quantity: "))
                
                if qty <= 0:
                    print("Quantity must be greater than 0")
                    continue

                name, price = self.menu[code]
                subtotal = price * qty
                total += subtotal

                order_items.append((name, qty, subtotal))

            except ValueError:
                print("Please enter valid number!")

        if order_items:
            order_id = str(uuid.uuid4())[:8]
            self.orders[order_id] = {
                "items": order_items,
                "total": total
            }

            print("\nOrder placed successfully!")
            print("Order ID:", order_id)
            print("Total Amount: ₹", total)
        else:
            print("No items selected!")

    def view_order(self):
        order_id = input("Enter Order ID: ").strip()

        if order_id in self.orders:
            print("\nOrder Details:")
            for item in self.orders[order_id]["items"]:
                print(f"{item[0]} | Qty: {item[1]} | ₹{item[2]}")
            print("Total: ₹", self.orders[order_id]["total"])
        else:
            print("Order not found!")

    def cancel_order(self):
        order_id = input("Enter Order ID to cancel: ").strip()

        if order_id in self.orders:
            del self.orders[order_id]
            print("Order cancelled successfully!")
        else:
            print("Order not found!")



system = RestaurantSystem()

while True:
    print("\n===== Restaurant Ordering System =====")
    print("1. Display Menu")
    print("2. Take Order")
    print("3. View Order")
    print("4. Cancel Order")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        system.display_menu()
    elif choice == "2":
        system.display_menu()
        system.take_order()
    elif choice == "3":
        system.view_order()
    elif choice == "4":
        system.cancel_order()
    elif choice == "5":
        print("Thank you! Visit again!")
        break
    else:
        print("Invalid choice! Please enter 1 to 5 only.")
