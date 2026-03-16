# write a python program to manage a phone store
# class Phone:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price
#     # def display(self):
#     #     print(self.brand,self.model,self.price)

#     def __str__(self):
#         return f"{self.brand} - {self.model} - {self.price}"


# # class PhoneInventory:

# #     def __init__(self,inventory):
# #         self.inventory=inventory
# #         print(type(inventory))
# #     def add_phone(self,phone):
# #         self.phone=phone
# #         self.inventory.append(phone)
# #     def display(self):
# #         print(self.inventory)
# #         return self.inventory


# def add_phone(p):
#     p_inventory.append(p)

# def displayInvetory(p_inventory):
#     for i in p_inventory:
#         #CALL __str__
#         print(i)

# def search_phone(b_name):
#     for i in p_inventory:
#         if b_name==i.brand:
#             print(i)


# p_inventory=[]
# while True:
#     print("1. Add Phone ")    
#     print("2. Update Phone ")    
#     print("3. Remove Phone ")    
#     print("4. Display all Phone ")    
#     print("5. Search Phone" )
#     print("6. exit ")    
#     choice=int(input("Enter choice "))
#     match choice:
#         case 1:
#             b_name=input("Enter brand name ")
#             m_name=input("Enter model ")
#             price=input("Enter price ")
#             # calll __init__
#             p1=Phone(b_name,m_name,price)
#             add_phone(p1)

#         case 4:
#             displayInvetory(p_inventory)
#         case 5:
#             b_name=input("Enter brand name that you want to search ")
#             search_phone(b_name)
#             #displayInvetory(lst)
#         case _:break






class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.brand} - {self.model} - ₹{self.price}"


# List to store phones
p_inventory = []


# Add Phone
def add_phone(p):
    p_inventory.append(p)
    print("Phone Added Successfully ✅")


# Display Inventory
def displayInventory():
    if not p_inventory:
        print("Inventory is empty ❌")
    else:
        print("\n--- Phone Inventory ---")
        for i in p_inventory:
            print(i)


# Search Phone
def search_phone(b_name):
    found = False
    for i in p_inventory:
        if b_name.lower() == i.brand.lower():
            print("Phone Found:", i)
            found = True
    if not found:
        print("Phone not found ❌")


# Update Phone
def update_phone(b_name):
    for i in p_inventory:
        if b_name.lower() == i.brand.lower():
            new_model = input("Enter new model: ")
            new_price = input("Enter new price: ")

            i.model = new_model
            i.price = new_price

            print("Phone Updated Successfully ✅")
            return
    print("Phone not found ❌")


# Remove Phone
def remove_phone(b_name):
    for i in p_inventory:
        if b_name.lower() == i.brand.lower():
            p_inventory.remove(i)
            print("Phone Removed Successfully ✅")
            return
    print("Phone not found ❌")


# Main Program
while True:
    print("\n1. Add Phone")
    print("2. Update Phone")
    print("3. Remove Phone")
    print("4. Display All Phones")
    print("5. Search Phone")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    match choice:

        case 1:
            b_name = input("Enter brand name: ")
            m_name = input("Enter model: ")
            price = input("Enter price: ")

            p1 = Phone(b_name, m_name, price)
            add_phone(p1)

        case 2:
            b_name = input("Enter brand name to update: ")
            update_phone(b_name)

        case 3:
            b_name = input("Enter brand name to remove: ")
            remove_phone(b_name)

        case 4:
            displayInventory()

        case 5:
            b_name = input("Enter brand name to search: ")
            search_phone(b_name)

        case 6:
            print("Exiting program ")
            break

        case _:
            print("Invalid choice ")








        
