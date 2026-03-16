# To add multiple data (use loop and append)
data = []
while True:
    name = input("Enter name: ")
    data.append(name)
    choice = input("Do you want to add more data? (y/n): ")
    if choice.lower() != 'y':
        break
print("Data entered:", data)

