# Write a python program to sum of the first n positive integers.
n = int(input("enter the n positive number:" ))
sum = 0
if n > 0:
    for i in range(1, n+1):
        sum = sum+i
    print("sum of first",n,"positive number is",sum)
else:
    print("please enter the valid number!!")