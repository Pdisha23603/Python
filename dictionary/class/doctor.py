# User details
name = input("Enter name: ")
m_no = int(input("Enter mobile number: "))
age = int(input("Enter age: "))


dr_dict = {
    "Dr. Abhay": {"10am": 0, "11am": 0},
    "Dr. Krutarth": {"2pm": 0, "3pm": 0, "4pm": 0}
}

print("Available Doctors:")
for d in dr_dict:
    print(d)

def book_appointment(dr, slot):
    if dr_dict[dr][slot] == 0:
        dr_dict[dr][slot] = 1
        print(f"{name}'s appointment booked with {dr} at {slot}")
    else:
        print("Slot already booked")

def cancel_appointment(dr, slot):
    if dr_dict[dr][slot] == 1:
        dr_dict[dr][slot] = 0
        print(f"{name}'s appointment cancelled with {dr} at {slot}")
    else:
        print("No appointment found to cancel")

while True:
    print("1. Book Appointment")
    print("2. Cancel Appointment")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        pre_dr = input("Enter Preferred Doctor: ")
        print(dr_dict[pre_dr])
        sel_slot = input("Enter Slot: ")

        for d in dr_dict:
            if d == pre_dr:
                book_appointment(d, sel_slot)

    elif choice == "2":
        pre_dr = input("Enter Doctor Name: ")
        print(dr_dict[pre_dr])
        sel_slot = input("Enter Slot to Cancel: ")

        for d in dr_dict:
            if d == pre_dr:
                cancel_appointment(d, sel_slot)

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice")
