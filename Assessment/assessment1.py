# menu = {
#     1: ("burger" , 75),
#     2: ("sandwich" , 80),
#     3: ("momos" , 120),
#     4: ("dabali" , 45),
#     5: ("pizza" , 110),
#     6: ("Manchurian" , 180),
#     7: ("spring roll" ,80),
#     8: ("pasta" , 100),
#     9: ("hot dog" , 190),
#     10:("pav bhaji" , 90),
#     11: ("tacos" , 85),
#     12: ("donuts" ,55),
#     13: ("wraps" ,95)
# }

# total_amt = 0

# while True:
#     print("      Menu      ")
#     for key, value in menu.items():
#         print(f"{key}.{value[0]} price= {value[1]} rupees")


#     choice = int(input("please place your order: "))
#     if choice in menu:
#         item_name, item_price = menu[choice]

#         print(f" you have selected {item_name}.")
#         quantity = int(input(" how much quantity you require: "))
#         amt = item_price * quantity
#         total_amt += amt
#         print(f"Amount : {amt}")
#         print(f"Total amount : {total_amt}")
#     else:
#         print("Please enter the valid choice!! Select from the menu please...")
#         continue
#     more = input("Do you want to place more order?  yes & no: ").lower()

#     if more =="no":
#         break

# print(f" Final Amount = {total_amt}")
# print(" Thanks for Ordering!! ")
# print("\n\n\n\n\n\n")






menu = {
    1: ("burger", 75),
    2: ("sandwich", 80),
    3: ("momos", 120),
    4: ("dabali", 45),
    5: ("pizza", 110),
    6: ("Manchurian", 180),
    7: ("spring roll", 80),
    8: ("pasta", 100),
    9: ("hot dog", 190),
    10: ("pav bhaji", 90),
    11: ("tacos", 85),
    12: ("donuts", 55),
    13: ("wraps", 95)
}

total_amt = 0

while True:
    print("       Menu       ")
    for key, value in menu.items():
        print(f"{key}. {value[0]}  price = {value[1]} rupees")

    items_count = int(input("\n How many different items you want to order now? : "))
    print("\n")

    for _ in range(items_count):
        choice = int(input("please place your order: "))
        print("\n")

        if choice in menu:
            item_name, item_price = menu[choice]
            print(f"You have selected {item_name}.")

            print("\n")
            quantity = int(input("how much quantity you require: "))
            amt = item_price * quantity
            total_amt += amt

            print(f"Amount : {amt}")
            print(f"Total amount : {total_amt}")

        else:
            print("Please enter the valid choice!! Select from the menu please...")

    more = input("Do you want to place more order? yes & no: ").lower()

    if more == "no":
        break

print("       Final Bill       ")
print(f"Final Amount = {total_amt}")
print("Thanks for Ordering!! ")
print("\n\n\n")
