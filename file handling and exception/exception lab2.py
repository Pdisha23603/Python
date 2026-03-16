# multiple except block and custom exception

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a + b)

except ValueError:
    print("Please enter only numbers")

except Exception:
    print("Something went wrong")