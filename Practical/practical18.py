# Python Program to Find Factorial of Number Using Recursion


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))



# output
# Enter a number: 5
# Factorial of 5 is 120


