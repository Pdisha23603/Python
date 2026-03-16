name=input("Enter name: ")
m_no=int(input("Enter mobile number: "))
age=int(input("Enter age: "))
dr_dict={"Dr. Harmi" : {"10am":0,"11am":0},
"Dr. Disha":{"2pm":0,"3pm":0,"4pm":0}
}
print(dr_dict.keys(),end=" ")

pre_dr=input("Enter Prefered Dr. from  ")
print(dr_dict[pre_dr],end=" ")
sel_slot=input("Enter slot  ")
# print(f"current slot {dr_dict[pre_dr][sel_slot]}")
print(f"current slot {dr_dict[pre_dr]}")
print(f"{name} appoinment is booked with {pre_dr} at {sel_slot}")
dr_dict[pre_dr][sel_slot]+=1
# print(f"{name} appointment is booked with {pre_dr} at {sel_slot}")
print(f"{name} appointment is booked with {dr_dict[pre_dr]}")