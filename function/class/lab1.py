# menu driven program 

def add(number1,number2):
    return(number1 + number2)
def sub(number1,number2):
    return(number1 - number2)
def mul(number1,number2):
    return(number1 * number2)
def div(number1,number2):
    if number1 == 0:
        print("Cannot be zero")
    if number2 == 0:
        print("Cannot be zero")
    return(number1 / number2)

while True:
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter Choice: "))
    number1 = int(input("Enter Number1: "))
    number2 = int(input("Enter Number2: "))
    
    match choice:
        case 1:
            number1 = int(input("Enter Number1: "))
            number2 = int(input("Enter Number2: "))
            ans = add(number1,number2)
            print(f"sum of {number1} and {number2} is {ans}")
        case 2:
            number1 = int(input("Enter Number1: "))
            number2 = int(input("Enter Number2: "))
            ans = sub(number1,number2)
            print(f"sum of {number1} and {number2} is {ans}")
        case 3:
            number1 = int(input("Enter Number1: "))
            number2 = int(input("Enter Number2: "))
            ans = mul(number1,number2)
            print(f"sum of {number1} and {number2} is {ans}")
        case 4:
            number1 = int(input("Enter Number1: "))
            number2 = int(input("Enter Number2: "))
            ans = div(number1,number2)
            print(f"sum of {number1} and {number2} is {ans}")
        case 5:
            break
        case _:
            print("Invalid choice!")