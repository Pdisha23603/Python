#find factorial number
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact= fact * i
    return fact
num = int(input("enter number: "))
ans = factorial(num)
print(ans)