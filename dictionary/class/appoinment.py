# name = input("enter name: ")
# mo = int (input("enter number: "))
# age = int(input("enter age: "))
# pre_dr = {"Dr. Abhay":{"9am":0, "10am":0, "11am":0},
#           "Dr.Krutarth": {"1pm":0, "2pm":0,"3pm":0}}
# print(pre_dr.keys(), end = " ")
# pre_dr= input("enter prefer doctor: ")

# lab task: assessment booking appoinment and also try using outside of for loop.


name = input("Enter name: ")
mo = input("Enter mobile number: ")
age = int(input("Enter age: "))


doctors = {
    "Dr. Abhay": {"9am": 0, "10am": 0, "11am": 0},
    "Dr. Krutarth": {"1pm": 0, "2pm": 0, "3pm": 0}
}

print("Available Doctors:")
for d in doctors.keys():
    print(d)

preferred_doctor = input("Enter preferred doctor name: ")

def book_appointment(doctor_name, slots, patient_name):
    print("Available Slots:")
    for s, status in slots.items():
        if status == 0:
            print(s)

    chosen_slot = input("Choose slot: ")

    if chosen_slot in slots and slots[chosen_slot] == 0:
        slots[chosen_slot] = 1
        print(f"Appointment booked successfully!")
        print(f"Patient: {patient_name}")
        print(f"Doctor: {doctor_name}")
        print(f"Time: {chosen_slot}")
    else:
        print("Slot not available!")

for doc, slot_data in doctors.items():
    if doc == preferred_doctor:
        book_appointment(doc, slot_data, name)
        break
else:
    print("Doctor not found")
