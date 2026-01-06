# factorial of a number
n = int(input("enter the number: "))
f = 1
if n< 0:
    print("number is invalid or negative")
elif n== 0:
    print("number is 0 and factorial is 1:")
else:
    for i in range(1, n+1):
        f *= i
    print("factorial of ",n," is" ,f)