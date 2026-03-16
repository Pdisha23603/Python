def factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact*=i
    return fact
def checkEven(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"

def palidrome(name):
    if name==name[::-1]:
        return "palidrome"
    else:
        return "non-palidrome"

while True:
    print("1. Factorial")
    print("2. Even / Odd")
    print("3. Palidrome")
    print("4. Exit")

    choice=int(input("enter choice: "))
    
    match(choice):
        case 1:
            number= int(input("enter number: "))
            ans = factorial(number)
            print(f"Factorial of {number} is {ans}")
        case 2:
            number= int(input("enter number: "))
            ans = checkEven(number)
            print(f"{number} is {ans}")
        case 3:
            name = input("enter name: ")
            ans = palidrome(name)
            print(f"{name} is {ans}")
        case 4: break
        case _:
            print("Invalid cchoice!")