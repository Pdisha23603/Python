# Find maximum number using ternary operator.

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
maximum = num1 if num1 > num2 else num2
print(f"maximum number is: {maximum}")