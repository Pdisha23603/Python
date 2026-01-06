# Write a Python program to add 'ing' at the end of a given string (length shouldbeat least 3). If the given string already ends with 'ing' then add 'ly' instead If thestring length of the given string is less than 3, leave it unchanged
name = input("enter name: ")
if len(name) < 3:
    print(name)
elif name.endswith("ing"):
    print(name + "ly")
else:
    print(name + "ing")


# output
# enter name: disha
# dishaing
# enter name: playing
# playingly
