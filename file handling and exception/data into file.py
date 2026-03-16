#  write a data into file untill user not enter "END"

# without using with keyword
file = open("first.txt", "w")
while True:
    data = input("Enter data (type END to stop): ")
    if data == "END":
        break    
    file.write(data + "\n")
file.close()
print("Data written to file successfully!")









# using with keyword
# with open("data.txt", "w") as file:
#     while True:
#         data = input("Enter data (type END to stop): ")
#         if data == "END":
#             break
#         file.write(data + "\n")
# print("Data written to file successfully!")


# 1️) open("data.txt", "w")
# Opens file in write mode
# Creates file if it doesn’t exist
# Clears old content if file already exists

# 2️) while True:
# Creates an infinite loop
# Keeps asking user for input

# 3️) input("Enter data...")
# Takes input from the user

# 4️) if data == "END":
# Checks stop condition
# When user types END, loop stops

# 5️) file.write(data + "\n")
# Writes input to file
# \n moves cursor to next line

# 6️) File auto-closes
# with ensures file is closed safely